---
layout: post
current: post
cover:  assets/images/20180110232157858.png
navigation: True
title: 视频镜头分割和关键帧提取
date: 2018-2-21 00:00:05 +800
tags: [OpenCV]
class: post-template
subclass: 'post tag-opencv'
author: yuyujunjun
---

[TOC]


## 1. Project Introduction
### (1)	选题
视频镜头边缘检测与镜头内关键帧提取
### (2) 工作简介
视频逐帧进行直方图绘制并按照$X^2$做差
根据当前帧所处环境进行自适应阈值防缩得到镜头边缘帧
优化镜头边缘帧
进行自适应关键帧提取
### (3) 开发环境
c++ opencv3.3.1 
## 2. Technical Detailss
### (1) 理论知识
#### 边缘检测
基于直方图差异进行边缘检测，差异越大的帧越有可能是镜头边界处，且使用直方图的方法可以很好的避免镜头内对象运动而造成的差异，提高一定鲁棒性。同时算法应该兼顾几个方面的问题。
 + 相邻两个镜头边缘不应该太靠近
 + 镜头边缘帧与前一帧的差值应该是当前镜头所有帧差值中最大的
 + 镜头边缘帧与前一帧的差值应该普遍大于该镜头中所有帧的平均差值的倍数
 + 下一个镜头中，靠近这个镜头的部分的两帧之间的差值不应该出现明显大于这个镜头边缘帧与前一帧的差值的情况
#### 关键帧提取
动态进行关键帧提取，不应该根据当前镜头的长短而应该根据当前镜头的变化剧烈程度，当前镜头变化越剧烈，则应该提取越多的关键帧，即便当前镜头并不长。相反，即便是一段很长的镜头，如果画面基本没变，我们也应该提取较少的关键帧。
如果当前镜头画面为全黑，我们不应该提取任何关键帧。

### (2) 具体算法
+ 对于每一帧我们用以下结构保存
```
struct m_frame {
	int index_frame;
	float distance;//与上一帧的差值
	bool M;//是否有可能是镜头分界帧
	bool KeyFrame;//是否是关键帧
};
```
```cpp
//定义最小镜头长度
#define m_MinLengthOfShot 4
```
#### 镜头边缘检测
##### 计算帧与帧之间的差值
+ 直方图差异利用如下公式计算
  $X^2=\begin{equation} \begin{cases} \sum_{i=1}^k \dfrac{(h_m(i)-h_n(i))^2}{max(h_m(i),h_n(i))}, (h_m(i)!= 0||h_n(i)!=0) \\ 0,else \end{cases} \end{equation}$
  将差值保存在结构中
```
m_frame::distance=X^2
```
##### 三次筛选进行自适应阈值的边界帧的判断
+ 对于镜头边界帧的选取，我们进行了三次筛选：
  +  （1） 制作一个大小为10帧的窗口，步长为8，所以窗口重叠次数为2。我们寻找窗口内```distance```最大的帧定义为可能的$M$帧，并判断它距离上一个$M$帧的距离。如果距离小于```m_MinLengthOfShot```（最小镜头长度），我们取消它的$M$帧资格，否则它是一个新的$M$帧。
  +  （2）进一步判断$M$是否是边缘帧。我们计算两个M帧之间帧的```distance```的平均值，并判断$M$帧是否远大于这个平均值，这里选择的$threshold$为6，即，当且仅当$M$帧的```distance```大于平均值的6倍，才得以保留。经过了这一步，已经能得到基本合理的镜头边缘了。
  +  （3） 进一步优化镜头边缘。判断该$M$帧后的小区间内是否有比$M$帧更合适的帧。方法如下：
    1. 从$M$帧开始，往后寻找8帧中的最大帧，若最大帧的```distance```小于$M$，则M帧得以保留。否则进行下一步
    2. 若存在大于$M$帧的帧，我们将其命名为$P$
    3. 计算$M$和$P$之间帧```distance```的平均值
    4. 判断$P$是否大于平均值的倍数，若没有大于，则M得以保留，否则P为新的M帧，并接下来继续判断。 


选择了其中一次筛选的函数的一部分：
```
//1. 从M帧开始，往后找8帧，如果没有比M更大的，则M得以幸存
//2. 若有，为P，则判断P是否大于M和P之间的数的平均值的阈值倍数，若并没有大于，则M得以幸存，否则，P为新的M
//3. 我们紧接着找下一个M，直到到末尾
void m_ThirdDelete(m_frame* temp) {
	while (true) {
		//首先找到下一个M的坐标
		for ( i = index_M+1; i < m_TestFrameNum; i++) {
			......
		}
		//如果没找到呢？
		if (i >= m_TestFrameNum)break;
		//找到后续间隔最大值及对应的P帧
		float max_behindinterval = temp[index_M].distance;
		int index_P = index_M;
		//找到往后数窗口间隔个数的最大值或者到最后一位的最大值
		for (int i = index_M; i < index_M+m_WindowInterval&&i<m_TestFrameNum; i++) {
			......
		}
		//如果没有大于M的，则M得以幸存
		//else 计算M和P帧的平均值
		{
			......
			//P帧就在M帧的后一个，那M帧就挂了
			if (sum == 0) {
				......
			}
			else {
				//如果P帧大于平均值的阈值倍，M帧也挂了
				if (temp[index_P].distance > average*m_threshold) {
					......
				}
				//如果P没有大于平均值的阈值倍，M得以幸存
				else {
				}
			}
		}
	}
}
```




#### 镜头内关键帧提取
我们根据镜头内帧的变化程度来确定关键帧的数量。
1. 首先计算所有镜头内的帧的平均```distance```
2. 找出镜头内帧的```distance```大于平均值的倍数的帧
3. 如果没有这样的帧，则证明该镜头变化过于平缓，我们选择镜头的中间帧
4. 排除亮度过于黑暗的帧

```
	while (true) {
		float sum = 0;
		int i = lastM + 1;
		//先统计在两个镜头边缘所有帧差别的平均值
		......	
		float average = sum / (i - lastM - 1);
		bool isFlappy = true;
		//如果期间帧变化挺快的，那么我们保存变化最快的几个位置
		......
		//如果两个帧之间几乎没有变化，则取两帧的中间值
		......
	}
	//删除那些颜色过暗的
	for (int i = 0; i < m_TestFrameNum; i++) {
		if (temp[i].KeyFrame == true) {
			float sum = mean(m_FrameImg[i])[0];
			if (sum < 5)temp[i].KeyFrame = false;
		}
	}
```
## Experiment Results
### 复仇者联盟预告片
#### 镜头（基本令人满意）
该视频镜头共有：56个
误判的镜头有：7个（因为全黑的过场也被判定成了一个镜头）
>提取关键帧的时候对全黑的镜头有所判定，于是实际上基本没有误判镜头

没判到的镜头有：2个
#### 关键帧（效果很不错）
镜头中本该存在关键帧（即镜头不是全黑的过场），但是没有提取到的有：0个镜头
关键帧存在的问题是：对于明暗变化明显的镜头，关键帧提取偏多
比如：
![这里写图片描述](http://img.blog.csdn.net/20180110232041151?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzQxMjIxOTQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20180110232049381?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzQxMjIxOTQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


但是这种结果并不是完全不可行
例如：
![这里写图片描述](http://img.blog.csdn.net/20180110231955762?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzQxMjIxOTQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![这里写图片描述](http://img.blog.csdn.net/20180110232024607?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzQxMjIxOTQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

这些漫画虽然被算作一个镜头，但是理应有多个关键帧才能表达这个镜头的含义。
文件截图：

可以看出结果还是很令人满意的
>下划线前面的数字代表其属于第几个镜头，后面的数字代表它在视频第几帧
>![这里写图片描述](http://img.blog.csdn.net/20180110232157858?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzQxMjIxOTQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

+ References:
  《基于窗口最大值和自适应阈值的视频镜头分割算法》 刘佳兵 《福建电脑杂志》2007年第8期
  《镜头边界检测及关键帧提取》 谭枫 哈尔滨工程大学

























 
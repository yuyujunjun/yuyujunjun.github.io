---
layout: post
current: post
cover:  false
navigation: True
title: 贝塞尔曲线的性质
date: 2018-2-20 00:00:03 +800
tags: [Graphics,Animation]
class: post-template
subclass: 'post tag-Graphics-and-Games'
author: yuyujunjun
---

#### 贝塞尔曲线的性质
+ 与Hermite曲线通过始末两点和亮点的方向来绘制曲线不同，贝塞尔样条曲线是通过多个关键控制点构成曲线，曲线有如下良好的性质，这些性质决定了FFD最终使用贝塞尔样条曲线而非Hermite曲线。
> 1. 对于给定关键点的贝塞尔曲线，曲线穿过最开始和最后的关键点
> 2. 曲线的大致趋势与关键点相契合
> 3. 曲线在关键点的包围之中，不会伸出到关键点以外

+ 现提出两个问题：

1. 为什么说这样的性质很契合FFD变形思想呢？
  <br>
  正如贝塞尔曲线关键点可以很好控制曲线的形状趋势一样，三维的贝塞尔曲线也可以很好的控制包围在关键点的物体，我们可以轻易控制关键点来获得包围在里面的物体的形状
  <br>
2. 为什么贝塞尔曲线具有这样的性质？
  <br>
  经过对贝塞尔曲线的观察，我认为贝塞尔曲线实际上是利用多个关键点进行加权插值的结果。
  先引入如下表达式：$((1-t)+t)^n=1^n$
  这其实是n阶贝塞尔曲线的表达式的权重比例分配。由于这个式子始终是等于1的，所以可以用来分配关键点的权重比例。例如：当$n=1$的时候，贝塞尔曲线的表达式为：
  $(1-t)P_1+tP_2$，那么对应于关键点$P_1$的权重比例就是$(1-t)$。当t从0开始变化到1时，$P_1$点对整个曲线的影响也越来越大，等于0的时候，$P_1$对曲线毫无影响，这时候$P_2$点对曲线影响最大，于是对应曲线的点和$P_2$重合。
  同理可得，当n变大的时候，我们可以同时使用多个关键点进行更灵活的操控，且当t等于0的时候，除了第一个关键点外其余关键点都不会对曲线产生任何影响，同理t等于1的时候只有最后一个关键点有影响。所以曲线一定会穿过首尾两个关键点。
  另外根据多项式的性质我们知道，对于中间的关键点，它不存在完全影响曲线的情况，即便是影响最大的时候，也会和相近的关键点同时影响，所以最终曲线是如此的性质。
```cs
      public void InitMesh()
    {
        //先获取对象的网格
        mesh = GetComponent<MeshFilter>().mesh;

        //获取对象的边界并创建包围盒的长宽高
        S = mesh.bounds.size.x;
        T = mesh.bounds.size.y;
        U = mesh.bounds.size.z;

        // 得到包围盒的两个相隔距离最远的点
        p0 = -new Vector3(S / 2, T / 2, U / 2);
        pN = new Vector3(S / 2, T / 2, U / 2);

        // 获取每个对象顶点的相对FFD包围盒的局部坐标
        for (int i = 0; i < mesh.vertexCount; i++)
        {
            float s = ((mesh.vertices[i].x - p0.x) / (pN.x - p0.x));
            float t = ((mesh.vertices[i].y - p0.y) / (pN.y - p0.y));
            float u = ((mesh.vertices[i].z - p0.z) / (pN.z - p0.z));
            meshCoordinates.Add(new Vector3(s, t, u));
        }
    }
```
```c#
    // Place control points around the object
    void InitCPs()
    {
        int i = 0;
        float x, y, z;

        // place n control points across the object at appropriate intervals
        for (x = 0.0f; x < 1.0f; x += 1.0f / CPs_s)
        {
            for (y = 0.0f; y < 1.0f; y += 1.0f / CPs_t)
            {
                for (z = 0.0f; z < 1.0f; z += 1.0f / CPs_u, i++)
                {
                    GameObject Node = Instantiate(CPNode, transform.position, Quaternion.identity) as GameObject;
                    Node.transform.parent = transform;
                    Node.transform.localPosition = (p0 + new Vector3(x * S, y * T, z * U)); // position is min node + % across the object * scale
                    Node.tag = "KeyPoints";
                    controlPoints.Add(Node);
                    initcontrolPoints.Add(Node.transform.localPosition);


                }
            }
        }
    }
```
```c#
    // connectors lines for visual clarity
    void InitConnectors()
    {
        int i, j, k;
        for (i = 0; i < CPs_s - 1; i++)
        {
            for (j = 0; j < CPs_t; j++)
            {
                for (k = 0; k < CPs_u; k++)
                {
                    GameObject connection = Instantiate(connector, transform.position, Quaternion.identity) as GameObject;
                    connection.transform.parent = transform;
                    LineRenderer lr = connection.GetComponent<LineRenderer>();
                    lr.SetVertexCount(2);
                    lr.SetWidth(0.01f, 0.01f);
                    lr.SetPosition(0, controlPoints[k + (j * 4) + (i * (CPs_t * CPs_u))].transform.position);
                    lr.SetPosition(1, controlPoints[k + (j * 4) + ((i + 1) * (CPs_t * CPs_u))].transform.position);
                    connectors.Add(connection);
                }
            }
        }

        for (i = 0; i < CPs_s; i++)
        {
            for (j = 0; j < CPs_t - 1; j++)
            {
                for (k = 0; k < CPs_u; k++)
                {
                    GameObject connection = Instantiate(connector, transform.position, Quaternion.identity) as GameObject;
                    connection.transform.parent = transform;
                    LineRenderer lr = connection.GetComponent<LineRenderer>();
                    lr.SetVertexCount(2);
                    lr.SetWidth(0.01f, 0.01f);
                    lr.SetPosition(0, controlPoints[k + (j * 4) + (i * (CPs_t * CPs_u))].transform.position);
                    lr.SetPosition(1, controlPoints[k + ((j + 1) * 4) + (i * (CPs_t * CPs_u))].transform.position);
                    connectors.Add(connection);
                }
            }
        }

        for (i = 0; i < CPs_s; i++)
        {
            for (j = 0; j < CPs_t; j++)
            {
                for (k = 0; k < CPs_u - 1; k++)
                {
                    GameObject connection = Instantiate(connector, transform.position, Quaternion.identity) as GameObject;
                    connection.transform.parent = transform;
                    LineRenderer lr = connection.GetComponent<LineRenderer>();
                    lr.SetVertexCount(2);
                    lr.SetWidth(0.01f, 0.01f);
                    lr.SetPosition(0, controlPoints[k + (j * 4) + (i * (CPs_t * CPs_u))].transform.position);
                    lr.SetPosition(1, controlPoints[(k + 1) + (j * 4) + (i * (CPs_t * CPs_u))].transform.position);
                    connectors.Add(connection);
                }
            }
        }
    }
```
```c#
   void MakeBernsteinCoefficients(int index)
    {
        float s = meshCoordinates[index].x;
        float t = meshCoordinates[index].y;
        float u = meshCoordinates[index].z;

        Bs[0] = (1.0f - s) * (1.0f - s);
        Bs[1] = 2.0f * s * (1.0f - s);
        Bs[2] = s * s;

        Bt[0] = (1.0f - t) * (1.0f - t) * (1.0f - t);
        Bt[1] = 3.0f * t * (1.0f - t) * (1.0f - t);
        Bt[2] = 3.0f * t * t * (1.0f - t);
        Bt[3] = t * t * t;

        Bu[0] = (1.0f - u) * (1.0f - u) * (1.0f - u);
        Bu[1] = 3.0f * u * (1.0f - u) * (1.0f - u);
        Bu[2] = 3.0f * u * u * (1.0f - u);
        Bu[3] = u * u * u;
    }
```

```c#
    public Vector3 EvalVertex(int index)
    {
        MakeBernsteinCoefficients(index);

        Vector3 point = new Vector3(0, 0, 0);

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                for (int k = 0; k < 4; k++)
                {
                    point += controlPoints[k + (j * 4) + (i * 4 * 4)].transform.localPosition * (Bs[i] * Bt[j] * Bu[k]);
                }
            }
        }

        return point;
    }
}
```
```c#
   private void GetInteraction()
    {//朝鼠标点击的 位置 发射一条射线  
        Ray interactionRay = UnityEngine.Camera.main.ScreenPointToRay(Input.mousePosition);//场景中必须含有 Canvas，否则无效  
        RaycastHit[] interactionInfo;//互动物体 碰撞到的物体  
        interactionInfo = Physics.RaycastAll(interactionRay, Mathf.Infinity);
        foreach (RaycastHit hit in interactionInfo)//发射一条3D射线  
        {
            GameObject interactedObject = hit.collider.gameObject;//获得射线 碰撞 到的物体  

            if (interactedObject.tag == "KeyPoints")//判断物体 的标签  
            {
                currentNode = interactedObject;
            }

        }
    }
```
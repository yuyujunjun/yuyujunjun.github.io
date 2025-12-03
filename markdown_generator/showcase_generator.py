import os
import yaml

# 定义输入和输出路径
INPUT_FOLDER = "_showcase"
OUTPUT_FILE = "_data/showcase_content.yml"

# 定义内容类型和对应的文件夹名称
CONTENT_TYPES = {
    "游记": "travel",
    "小说": "novel",
    "照片": "photo",
    "视频": "video"
}

# 初始化数据结构
showcase_data = []
def generate_excerpt(file_path, max_length=50):
    """从 Markdown 文件中提取正文的前几行作为 excerpt，保留换行"""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        content_started = False
        content = []
        for line in lines:
            # 跳过 YAML 前置数据部分
            if line.strip() == "---":
                if content_started:  # 如果已经遇到第二个 "---"，说明 YAML 结束
                    content_started = False
                else:
                    content_started = True
                continue
            if not content_started and line.strip():  # 读取正文内容
                content.append(line.strip())  # 保留每一行内容

        # 合并正文并截取前 max_length 个字符，保留换行符
        full_content = "\n".join(content)  # 使用换行符连接内容
        if len(full_content) > max_length:
            return full_content[:max_length] + "..."  # 截断并添加省略号
        return full_content
# 函数：读取 Markdown 文件的 YAML 前置数据
def read_yaml_front_matter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if lines[0].strip() == "---":
            yaml_lines = []
            for line in lines[1:]:
                if line.strip() == "---":
                    break
                yaml_lines.append(line)
            return yaml.safe_load("\n".join(yaml_lines))
    return {}

import os

def process_novel_or_travel(folder_path, folder_name):
    """处理小说和游记类型的内容"""
    items = []
    for folder in os.listdir(folder_path):
        content_path = os.path.join(folder_path, folder)
        if os.path.isdir(content_path):
            folder_items = []
            for item_file in sorted(os.listdir(content_path)):
                if item_file.endswith(".md"):
                    item_path = os.path.join(content_path, item_file)
                    front_matter = read_yaml_front_matter(item_path)
                    chapter_excerpt = generate_excerpt(item_path)

                    item_title = front_matter.get("title", os.path.splitext(item_file)[0])
                    item_url_path = os.path.splitext(item_file)[0]
                    item_url = f"/showcase/{folder_name}/{folder}/{item_url_path}/"
                    folder_items.append({"title": item_title, "url": item_url, "excerpt": chapter_excerpt})

            # 添加数据
            items.append({
                "title": folder,
                "type": folder_name,
                "series": folder if folder == "novel" else None,  # 小说有系列，游记没有
                "chapters" if folder == "novel" else "entries": folder_items
            })
    return items


import os
import yaml  # 用于写入 YAML 文件


def process_media(folder_path, folder_name):
    """处理媒体类型的内容，包括图片、视频、文字和外链，并生成 Markdown 文件"""
    medias = []

    for folder in os.listdir(folder_path):
        content_path = os.path.join(folder_path, folder)
        if os.path.isdir(content_path):
            # 初始化媒体数据
            media = {
                "title": folder,
                "url": f"/showcase/{folder_name}/{folder}_/",
                "markdown_path": os.path.join(folder_path, f"{folder}_.md"),
                "photos": [],
                "videos": [],
                "texts": [],
                "external_videos": []
                
            }
            if os.path.exists(os.path.join(content_path, "title.md")):
                media["title"] = generate_excerpt(os.path.join(content_path, "title.md"), max_length=200)
            
            # 遍历文件夹中的所有文件
            for file_name in sorted(os.listdir(content_path)):
                file_path = os.path.join(content_path, file_name)

                # 处理图片
                if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif")):
                    photo_url = f"/showcase/{folder_name}/{folder}/{file_name}"
                    media["photos"].append(photo_url)

                # 处理视频
                elif file_name.lower().endswith((".mp4", ".avi", ".mov", ".mkv", ".webm")):
                    video_url = f"/showcase/{folder_name}/{folder}/{file_name}"
                    media["videos"].append(video_url)

                # 处理文字（Markdown 文件）
                elif file_name.lower().endswith(".md"):
                    text_content = generate_excerpt(file_path, max_length=20000)
                    # with open(file_path, "r", encoding="utf-8") as f:
                    #     text_content = f.read()
                    media["texts"].append({"filename": file_name, "content": text_content})

                # 处理外链视频（video.txt）
                elif file_name.lower() == "video.txt":
                    with open(file_path, "r", encoding="utf-8") as f:
                        external_links = f.readlines()
                    for link in external_links:
                        link = link.strip()
                        if link:
                            media["external_videos"].append(link)

            # 生成 Markdown 文件
            md_content = generate_media_album_md(media)
            with open(media["markdown_path"], "w", encoding="utf-8") as f:
                f.write(md_content)
            print(f"Generated Markdown file: {media['markdown_path']}")
            media['type'] = "media"
            del media['texts']
            # 添加媒体数据到列表
            medias.append(media)

    return medias


def generate_media_album_md(media):
    """生成媒体相册的 Markdown 文件内容"""
    photos_yaml = "\n".join([f"  - {photo}" for photo in media["photos"]])
    videos_yaml = "\n".join([f"  - {video}" for video in media["videos"]])
    texts_yaml = "\n".join([f"  - filename: '{text['filename']}'\n    content: '{text['content']}'" for text in media["texts"]])
    external_videos_yaml = "\n".join([f"  - {video}" for video in media["external_videos"]])

    md_content = f"""---
layout: album
title: '{media['title']}'
photos:
{photos_yaml if photos_yaml else '  []'}
videos:
{videos_yaml if videos_yaml else '  []'}
texts:
{texts_yaml if texts_yaml else '  []'}
external_videos:
{external_videos_yaml if external_videos_yaml else '  []'}
---

这是 {media['title']} 相册的描述。
"""
    return md_content


def generate_showcase_data(folder_path, folder_name):
    """根据内容类型生成 showcase 数据"""
    if folder_name in ["novel", "travel"]:
        return process_novel_or_travel(folder_path, folder_name)
    elif folder_name == "media":
        return process_media(folder_path, folder_name)



# 主逻辑
showcase_data = []
all_folder_names = os.listdir("_showcase")
pre_order = ["media", "travel", "novel"]

for folder_name in pre_order:
    folder_path = os.path.join("_showcase", folder_name)
    if os.path.isdir(folder_path):
        showcase_data += generate_showcase_data(folder_path, folder_name)

# 将 showcase_data 写入 YAML 文件
yaml_output_path = "_data/showcase_content.yml"
with open(yaml_output_path, "w", encoding="utf-8") as yaml_file:
    yaml.dump(showcase_data, yaml_file, allow_unicode=True, default_flow_style=False)

print(f"YAML file written to: {yaml_output_path}")
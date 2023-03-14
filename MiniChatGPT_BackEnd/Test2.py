import json
import os

import jieba.analyse
from stanfordcorenlp import StanfordCoreNLP

# 读取json文件并提取sender为Me的content
folder_path = r'D:\user\hbh\Downloads\element-plus-vite-starter-main\element-plus-vite-starter-main\src\components\chatdata'
file_path = os.path.join(folder_path, ' 玥玥 可爱 于皇 存在.json')

contents = []
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
    for d in data:
        if d["sender"] == "Me":
            contents.append(d["content"])

# 处理每个content
jieba.load_userdict(r"C:\Users\hbh\Desktop\Mini_chatGPT\Mini chatGPT\MiniChatGPT_BackEnd\hbh_dir.txt")
# 处理每个content
keywords = {}  # 关键词及其出现次数的字典
for content in contents:
    # 分词并提取关键词

    words = jieba.analyse.extract_tags(content, topK=20, withWeight=True,allowPOS=('n','adj','ns'))
    print(words)
    for word, weight in words:
        # 去除标点符号
        if word.isalpha() or word.isdigit():
            # 句法句意理解后的处理，此处略过
            # 统计关键词出现次数
            if word in keywords:
                keywords[word] += 1
            else:
                keywords[word] = 1

# 返回出现次数最多的前三个关键词
top_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:4]
print("Top 3 keywords:")
for keyword in top_keywords:
    print(keyword[0])
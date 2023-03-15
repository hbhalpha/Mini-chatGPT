## 客户需求

> Mini-ChatGPT  
> ChatGPT（全名：Chat Generative Pre-trained Transformer），美国OpenAI研发的聊天机器人程序 ，于2022年11月30日发布 。ChatGPT是人工智能技术驱动的自然语言处理工具，它能够通过理解和学习人类的语言来进行对话，还能根据聊天的上下文进行互动，真正像人类一样来聊天交流，甚至能完成撰写邮件、视频脚本、文案、翻译、代码，写论文等任务。  
> 本作业要求使用javascript技术，编写一个交互界面更加友好的聊天机器人。基本要求如下：  
> （1）不需要接入ChatGPT后台，也不必需采用人工智能技术进行自然语言处理。  
> （2）针对目前ChatGPT交互性为基本文本对话框的方式，进行改进。采用合适的javascript前端技术编写WEB页面，实现 自拖动、自调整布局，自动推荐补齐，历史聊天记录分类、分层次呈现，根据输入内容（几句  话、一段话、一篇文章等）区分不同输入方式，等至少两种前端效果。  
> （3）后端不要求必须使用javascript，要求使用MySQL数据库存放确切的聊天答案，能够根据输入要求，输出确切的答案。对于不符合输入要求的问题，能够做出判断并拒绝回答。对于大量的并发访问需求，能够判断连接数过多（如大于5、大于10）并拒绝连接。  
> （4）按照个人软件编程习惯，形成完整的软件流程文档，记录个人软件开发过程。  
> 加分项目：  
> （1）采用成熟的前端或者后端javascript框架，加速作业的完成。  
> （2）具有热点问题排名、最多提问者排名、最佳提问等热榜。  
> （3）后端能够调用简单的Python程序，处理分词等简单的人工智能任务。  
> 3月21日公开演示答辩，答辩前将所有资料（含源代码、文档、过程素材等）发邮件给dahogn@sdu.edu.cn，大附件请发网盘链接。

## 本项目本地运行
1.首先需要下载Python后端的依赖
2.在文件保存记录/图片识别等后端，你需要将路径更换为本地
## 功能与完成情况
|功能|完成情况|
|:---:|:---:|
|采用成熟的Javascrip框架(vue)|√|
|实现了自由拖动聊天框，自由调整布局|√|
|做到了聊天记录分类展示|√|
|聊天记录分类保存标准按照Phthon的NLP分词处理|√|
|实现了分层次呈现|√|
|后端采用了Mysql，设置最大连接池与线程锁|√|
|对未查到的消息实现了提示无法回答|√|
|实现了热榜排名|√|
|采用Python NLP对Json|√|
## 拓展
|拓展功能|完成情况|
|:---:|:---:|
|实现支持图输入|√|
|实现对图进行识别并分类的特异功能|√|
|实现了基于Openai api的强AI对话并给AI设立了人设|√|

## 实际展示如下
### 界面展示:
![](https://github.com/hbhalpha/Mini-chatGPT/blob/main/images/%E7%95%8C%E9%9D%A2%E5%B1%95%E7%A4%BA1.png)
![](https://github.com/hbhalpha/Mini-chatGPT/blob/main/images/%E7%95%8C%E9%9D%A2%E5%B1%95%E7%A4%BA2.png)
### 聊天界面展示:
![](https://github.com/hbhalpha/Mini-chatGPT/blob/main/images/%E8%81%8A%E5%A4%A9%E7%95%8C%E9%9D%A2%E5%B1%95%E7%A4%BA.png)
### 聊天界面与热榜:
![](https://github.com/hbhalpha/Mini-chatGPT/blob/main/images/%E8%81%8A%E5%A4%A9%E7%95%8C%E9%9D%A2%E4%B8%8E%E7%83%AD%E6%A6%9C.jpg)
### 历史记录分类与聊天框拖动:
![](https://github.com/hbhalpha/Mini-chatGPT/blob/main/images/%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95%E5%88%86%E7%B1%BB%E4%B8%8E%E8%81%8A%E5%A4%A9%E6%A1%86%E6%8B%96%E5%8A%A8.jpg)
### 垃圾分类识别展示:
![](https://github.com/hbhalpha/Mini-chatGPT/blob/main/images/%E5%9E%83%E5%9C%BE%E5%88%86%E7%B1%BB%E8%AF%86%E5%88%AB%E5%B1%95%E7%A4%BA.png)
### 强AI展示:
![](https://github.com/hbhalpha/Mini-chatGPT/blob/main/images/%E5%BC%BAAI%E5%B1%95%E7%A4%BA.png)
### 侧边栏展示
![]()

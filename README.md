# Mini chatGPT
这是山东大学泰山学堂22级计科第一次大作业
# 项目介绍
 ChatGPT是由美国OpenAI研发的人工智能技术驱动的自然语言处理工具，本项目旨在使用javascript技术编写一个交互界面更加友好的聊天机器人。
 
# 整体架构
为了实现Mini-ChatGPT聊天机器人的需求，我们将架构分为前端、后端和数据库三个部分。

## 前端部分
前端部分使用JavaScript技术，通过合适的前端框架编写Web页面，实现以下需求：
 * 自拖动、自调整布局
 * 自动推荐补齐
 * 历史聊天记录分类、分层次呈现
 * 根据输入内容（几句话、一段话、一篇文章等）区分不同输入方式，实现不同的前端效果
 * 我们可以使用Vue.js或React等前端框架，通过组件化、响应式等技术实现前端的各种交互需求。
 
 ## 后端部分
后端部分使用JavaScript或其他后端语言，我们建议使用Node.js，同时可以调用Python程序进行分词等简单的人工智能任务。后端通过以下技术实现：
* 接收前端发送的请求，并对请求进行处理
* 根据请求的内容，从数据库中获取聊天答案
* 判断连接数是否过多，若连接数过多则拒绝连接
* 调用Python程序进行分词等简单的人工智能任务
* 我们可以使用Express框架等后端框架，通过路由、中间件等技术实现后端的各种处理需求。

## 数据库部分
数据库部分使用MySQL存放确切的聊天答案，根据输入要求，输出确切的答案。我们可以使用以下技术实现：
* 使用MySQL作为数据库存储聊天答案
* 根据输入要求，从数据库中获取确切的答案
* 我们可以使用MySQL数据库，通过SQL语句等技术实现对数据库的各种操作。

# 技术栈
* 前端部分：Vue.js或React等前端框架
* 后端部分：Node.js、Express框架
* 数据库部分：MySQL数据库
* 人工智能处理：Python程序

# 项目总结

以上是Mini-ChatGPT聊天机器人的架构实现方法以及技术栈。我们通过合适的前端框架、后端框架、数据库和Python程序等技术，实现了聊天机器人的各种交互需求，同时使用MySQL数据库存储聊天答案，实现了对聊天答案的准确输出。


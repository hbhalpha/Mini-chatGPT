<template>
  <div class="chat" >
    <div class="chat-input-container" style="background-image: url(src/assets/Background4.webp)" >
      <div  draggable="true" id="Putting"
            :style="{cursor: isDragging ? 'move' : 'default', position: 'absolute', left: dragX + 'px', top: dragY + 'px'}">
        <el-autocomplete type="text" id="Inputt" v-model="message" placeholder="say something" @keydown.enter="sendMessage"
              :fetch-suggestions="getSuggestions"    :style="{ background: isMessageEmpty ? ' #589ef8' : 'green', width: '100%'}" />
      </div>
      <el-button @keydown.enter="sendMessage" @click="sendMessage" :disabled="isMessageEmpty" style="background: #589ef8 ; color: antiquewhite">Send</el-button>
      <el-input placeholder="请输入聊天记录名" v-model="chatingname" @input="BeingInput" @keydown.enter="getrecord" style="background: #589ef8;"></el-input>
      <el-button @click="getrecord(chatingname)" style="background: #589ef8 ; color: antiquewhite">确定选择聊天记录</el-button>
      <el-button @click="clear" style="background: #589ef8 ; color: antiquewhite">清空聊天记录</el-button>
    </div>
    <div class="chat-window" style="background-image: url(src/assets/Background3.webp) ;background-size: cover; ">
      <div v-for="(msg, index) in messages" :key="index"
           :class="{ 'chat-message': true, 'my-message': msg.sender === 'Me', 'reply-message': msg.sender === 'Reply' }">
        <div v-if="msg.Type === 'Text'">{{ msg.content }}</div>
        <div v-else><img src="src/assets/Background.jpg" height="123" width="123" ></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, computed, watch, onMounted, provide} from 'vue';
import useDraggable from './useDraggable';
import axios from 'axios';
import * as fs from 'fs'
import * as string_decoder from "string_decoder";



export interface Message {
  content: string;
  Type:'Pic'|'Text'
  sender: 'Me' | 'Reply';
}
interface DataPost{
  Indicator : string;
  JsonData : string;
}
interface Option{
  value:string;
  answer:string;
}
interface DataItem {
  id:number;
  questions: string;
  answers:string;
  HotValue: number;
}

export default defineComponent({
      name: 'Chat',
      props: {
        data: {
          type: Array as () => DataItem[],
          required: true,
        },
        Mode: {
          type: String,
          required: true
        }
      },

      setup(props) {
        const message = ref('');
        var chatingname = ref('');
        const messages = ref<Message[]>([]);
        const isMessageEmpty = computed(() => message.value.trim() === '');
        onMounted(async () =>{ // 初始挂载函数，用来提示
          if(props.Mode == "Chat")
          messages.value.push({
            content: '你好我是玥玥，是一个聊天机器人，我可以与您进行简单的对话捏，当然我也会回答您一些问题捏（可以回答的看热榜），玥玥超喜欢你喵！',
            Type:'Text',
            sender: 'Reply',
          });
          if(props.Mode =="Rubbish")
            messages.value.push({
              content: '你好我是玥玥，是一个聊天机器人，现在是垃圾分类与识别模式，玥玥会帮助你捏，玥玥超喜欢你喵！',
              Type:'Text',
              sender: 'Reply',
            });
          if(props.Mode =="AI")
            messages.value.push({
              content: '你好我是玥玥，是一个聊天机器人，现在是强AI模式，玥玥作为一个高中生，将回复你各种问题',
              Type:'Text',
              sender: 'Reply',
            });
        })

        async function getrecord(): Promise<void>
        {
          console.log(chatingname.value);
          try {
            const getRec = await axios.get('http://localhost:8080/GetRecNum', {
              params: {
                str: '12345678' ,
              }
            });
            const newname =getRec.data.replace('.json','');
            if(newname == '') console.log(chatingname.value)
              else
            {
              console.log(newname)
              chatingname.value = newname
            }

            console.log(getRec)
          }
          catch (error)
          {
            console.log(error)
          }
          try {

            const response = await axios.get('http://localhost:8080/ReadingFiles', {
              params: {
                str:chatingname.value
              }
            });
            const dataread = response.data;
            messages.value=[];
            for(var i=0;i<=dataread.length-1;i++)
            {
              messages.value.push(dataread[i])
            }

            console.log(dataread);
          } catch (error) {
            console.error(error);
          }
        };
        provide('getrecord',getrecord);
        const sendRequest = async (strrr:string) => { //这个函数是为了计数，更新某个问题被问了多少次
          try {
            const result = await axios.get('http://localhost:8080/data2?str='+strrr);
            console.log(result.data)
            return result.data
          } catch (error) {
            console.error(error);
          }
        };
        const clear = () =>{
          messages.value = [];
          messages.value.push({
              content: '你好我是玥玥，是一个聊天机器人，我可以与您进行简单的对话捏，当然我也会回答您一些问题捏（可以回答的看热榜），玥玥超喜欢你喵！',
              Type:'Text',
              sender: 'Reply',
        })
        }


        const getReply = (msg:string) =>{ // 这个函数是用来确定答复函数的
          var flag=0;
          var ReplyText :string ="";
          console.log(props.Mode)
          if(props.Mode === 'AI')
          {
            axios.get<string>('http://localhost:8080/AI', {
              params: {
                str: msg
              }
            })
                .then(function(response) {
                  const resp: string = response.data;
                  ReplyText = resp
                  console.log(resp);
                })
                .catch(function(error) {
                  console.error(error);
                });
            return ReplyText
          }
          for(var i=0;i<=props.data.length-1;i++)
          {
            if(props.data[i].questions==msg)
            {
              flag=1;
              sendRequest(props.data[i].questions);
              ReplyText = props.data[i].answers;
              break;
            }
          }


          if(flag==1)
          {
            return ReplyText;
          }
          else {
            if(msg.includes('超喜欢玥玥')||msg.includes('超喜欢你')) return '玥玥也超喜欢你捏（'
            if (msg === '你好'|| msg ==='你好玥玥') {
              return '你好,我是一个由山东大学泰山学堂hbh开发的简单聊天机器人，我可以与你进行简单的逻辑对话，对于排行榜中存在的问题，我将给您解答，对于不符合规范的内容我将无法识别，抱歉喵。请问有什么能帮到你的吗?';
            }
            else {
              const tempMessage = msg;

              if (msg.includes("?")||msg.includes("？")) {
                msg= msg.replaceAll("?", "!");
                msg= msg.replaceAll("？", "!");
              }
              if (msg.includes("是不是")) {
                msg= msg.replace("是不是", "是");
              }
              if (msg.includes("告诉")) {
                msg= msg.replace("告诉", "回答");
              }
              if (msg.includes("吗")) {
                msg= msg.replace("吗", "（肯定）");
              }
              if (msg.includes("你")||msg.includes("我")) {
                msg= msg.replace("你", "xx").replace("我", "你").replace("xx","我");
              }
              if (msg.includes("玥玥")||msg.includes("我")) {
                msg= msg.replace("玥玥", "我");
              }
              if(tempMessage.includes("?")==false&&tempMessage.includes("？")==false&&tempMessage.includes("是不是")==false) {
                return '你好,我是一个由山东大学泰山学堂hbh开发的简单聊天机器人，我可以与你进行简单的逻辑对话，对于排行榜中存在的问题，我将给您解答，对于不符合规范的内容我将无法识别，抱歉'
              }
              else return msg
            }
          }


        };
        const sendMessage = async () => {
          if (isMessageEmpty.value) {
            return;
          }
          console.log(JSON.stringify(messages.value) )
          messages.value.push({
            content: message.value,
            Type:'Text',
            sender: 'Me',
          });
          var temp = message.value;
          message.value = '';

          messages.value.push({

            content: getReply(temp),
            Type:'Text',
            sender: 'Reply',
          });
          //发送更新聊天记录的请求
          const dataPost: DataPost = {
            Indicator: "update",
            JsonData: JSON.stringify(messages.value),
          };
          axios.post('http://localhost:8080/DataPost', JSON.stringify(dataPost), {
            headers: {
              'Content-Type': 'application/json',
            },
          })
              .then(response => {
                console.log(response.data);
              })
              .catch(error => {
                console.error(error);
              });
        };

        const { isDragging, dragX, dragY, enableDragging } = useDraggable()
        const selectedValue = ref('');
        // 所有数据
        function getSuggestions  (queryString: string, cb: (results: Option[]) => void)  {
          const options = ref<Option[]>([]);
          for(var i=0;i<=props.data.length-1;i++)
          {
            options.value.push({
              value:props.data[i].questions,
              answer:props.data[i].answers
            })
          }
          const results = queryString
              ? options.value.filter(createFilter(queryString))
              : options.value

          cb(results)
        }
        function createFilter(queryString: string) {
          return (option: Option) =>
              option.value.toLowerCase().indexOf(queryString.toLowerCase()) !== -1
        }

        // 监听输入框的值
        watch(message, (newValue, oldValue) => {
          if (newValue === '') {
            selectedValue.value = '';
          }
        });

        // 输入框输入时的回调函数
        const onInput = (value: string) => {
          message.value = value;
        };
        const BeingInput = (value:string ) =>{
          chatingname.value = value
        }

        return {
          message,// 单条消息
          clear,//清屏函数
          messages, // 消息列表
          isMessageEmpty, // 判断消息是否为空
          chatingname, // 聊天记录名（输入）
          sendMessage,//发送信息
          BeingInput, // 控制聊天记录名的输入
          isDragging, // 拖动
          dragX,
          dragY,
          enableDragging,
          selectedValue, // 选择内容
          onInput,
          getSuggestions,
          getrecord// 获取记录
        };
      },
    }
);
</script>

<style>
.chat {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
  height: 100%;
  width: 100%;
  padding: 10px;
}

[v-draggable] {
  user-select: none;
}

el-input[type='text'] {
  width: 100%;
  padding: 5px;
  border: none;
  border-radius: 3px;
  font-size: 32px;
  outline: none;
}

el-select
{
  width: 100%;
  padding: 5px;
  border: none;
  border-radius: 3px;
  font-size: 32px;
  outline: none;
}
el-button {
  padding: 5px 10px;
  background-color: #0077cc;
  border: none;
  border-radius: 3px;
  color: #0077cc;
  cursor: pointer;
}
el-option{
  width: 100%;
  padding: 5px;
  border: none;
  border-radius: 3px;
  font-size: 32px;
  outline: none;
}
.chat-window {
  display: flex;
  float: left;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
  height: 89%;
  overflow-y: auto;
  border-radius: 3px;
  padding: 10px;
}
#Putting
{
  width: 100%;
  height: 100%;
}

.chat-message {
  max-width: 70%;
  word-break: break-all;
  padding: 5px 10px;
  margin-bottom: 5px;
  border-radius: 3px;
}

.my-message {
  background-color: #50ea4b;
  color: #fff;
  align-self: flex-end;
}

.reply-message {
  background-color: #fff;
  color: #000;
  align-self: flex-start;
  text-align:left;
}

.chat-input-container {
  display: flex;
  align-items: center;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  background-color: white;
}
.el-input::placeholder {
  color: red;
}

</style>
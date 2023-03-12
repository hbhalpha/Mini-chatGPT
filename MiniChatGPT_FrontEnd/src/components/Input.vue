<template>
  <div class="chat" >
    <div class="chat-input-container" style="background-image: url(src/assets/Background4.webp)" >
      <div  draggable="true" id="Putting"
            :style="{cursor: isDragging ? 'move' : 'default', position: 'absolute', left: dragX + 'px', top: dragY + 'px'}">
        <el-input type="text" v-model="message" placeholder="say something" @input="onInput" @keydown.enter="sendMessage"
                  :style="{ background: isMessageEmpty ? ' #589ef8' : 'green'}"/>
        <el-select v-model="selectedValue" @change="onChange" style="width: 100%;background: #3cbbe5">
          <el-option v-for="(item, index) in filteredData" :key="index" :label="item.questions" :value="item.questions" style="width: 100%;"></el-option>
        </el-select>
      </div>
      <el-button @keydown.enter="sendMessage" @click="sendMessage" :disabled="isMessageEmpty" style="background: #589ef8 ; color: antiquewhite">Send</el-button>
    </div>
    <div class="chat-window" style="background-image: url(src/assets/Background3.webp) ;background-size: cover; ">
      <div v-for="(msg, index) in messages" :key="index"
           :class="{ 'chat-message': true, 'my-message': msg.sender === 'Me', 'reply-message': msg.sender === 'Reply' }">
        {{ msg.content }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, computed, watch, onMounted} from 'vue';
import useDraggable from './useDraggable';
import axios from 'axios';




export interface Message {
  content: string;
  sender: 'Me' | 'Reply';
}
interface DataPost{
  Indicator : string;
  JsonData : string;
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
      },
      setup(props) {
        const message = ref('');
        const chatingname = ref('');
        const messages = ref<Message[]>([]);
        const isMessageEmpty = computed(() => message.value.trim() === '');
        onMounted(async () =>{
          messages.value.push({
            content: '你好我是玥玥，是一个聊天机器人，我可以与您进行简单的对话捏，当然我也会回答您一些问题捏（可以回答的看热榜），玥玥超喜欢你喵！',
            sender: 'Reply',
          });})
        const sendRequest = async (strrr:string) => {
          try {
            const result = await axios.get('http://localhost:8080/data2?str='+strrr);
            console.log(result.data)
            return result.data
          } catch (error) {
            console.error(error);
          }
        };



        const getReply = (msg:string) =>{
          var flag=0;
          var ReplyText :string ="";
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
        const sendMessage = () => {
          if (isMessageEmpty.value) {
            return;
          }
          console.log(JSON.stringify(messages.value) )
          messages.value.push({
            content: message.value,
            sender: 'Me',
          });
          var temp = message.value;
          message.value = '';
          messages.value.push({

            content: getReply(temp),
            sender: 'Reply',
          });
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
        const filteredData = computed(() => {
          if (message.value === '') {
            return [];
          } else {
            console.log(props.data[0])
            console.log(props.data.filter(item => item.questions.includes(message.value))[0].questions);
            return props.data.filter(item => item.questions.includes(message.value));
          }
        });

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

        // 选中值改变时的回调函数
        const onChange = (value: string) => {
          message.value = value;
          selectedValue.value = value;
        };
        return {
          message,
          messages,
          isMessageEmpty,
          sendMessage,
          isDragging,
          dragX,
          dragY,
          enableDragging,
          selectedValue,
          filteredData,
          onInput,
          onChange,
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
<template>
  <div class="chat" >
    <div class="chat-input-container" style="background-image: url(src/assets/Background4.webp)" >
      <div>
        <el-button @click="showFileDialog">选择图片</el-button>
        <el-dialog v-model="dialogVisible" title="选择图片" width="30%">
          <el-upload
              class="upload-demo"
              action="#"
              :show-file-list="false"
              :on-change="handleUploadChange"
              :before-upload="beforeUpload"
          >
            <el-button slot="trigger" size="large" type="primary">
              选择文件
            </el-button>
            <div slot="tip" class="el-upload__tip">
              只能选择图片文件
            </div>
          </el-upload>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取消</el-button>
            <el-button type="primary" @click="confirmSelection();getRubbishData();sendMessage()">确认</el-button>
          </div>
        </el-dialog>

      </div>

    </div>
    <div class="chat-window" style="background-image: url(src/assets/Background3.webp) ;background-size: cover; ">
      <div v-for="(msg, index) in messages" :key="index"
           :class="{ 'chat-message': true, 'my-message': msg.sender === 'Me', 'reply-message': msg.sender === 'Reply' }">
        <div v-if="msg.Type === 'Text'">{{ msg.content }}</div>
        <div v-else>
          <div v-if="msg.content" >
            <img  :src="msg.content" height="123" width="123">
          </div>
        </div>
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
        const dialogVisible = ref(false);
        var ReplyText = ref('')
        const selectedImage = ref('');
        const message = ref('');
        var chatingname = ref('');
        const messages = ref<Message[]>([]);
        const isMessageEmpty = computed(() => message.value.trim() === '');
        onMounted(async () =>{
          if(props.Mode == "Chat")
            messages.value.push({
              content: '你好我是玥玥，是一个聊天机器人，我可以与您进行简单的对话捏，当然我也会回答您一些问题捏（可以回答的看热榜），玥玥超喜欢你喵！',
              Type:'Text',
              sender: 'Reply',
            });
          if(props.Mode =="Rubbish")
            messages.value.push({
              content: '你好我是玥玥，是一个聊天机器人，现在是垃圾分类与识别模式，在选择图片后请等待三秒，玥玥会帮助你捏，玥玥超喜欢你喵！',
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
        const sendRequest = async (strrr:string) => {
          try {
            const result = await axios.get('http://localhost:8080/data2?str='+strrr);
            console.log(result.data)
            return result.data
          } catch (error) {
            console.error(error);
          }
        };
        //下面是垃圾桶的代码
        const handleUploadChange = (file: Blob) => {
          if (!file) {
            console.error('No file provided!');
            return;
          }


          selectedImage.value = 'src/imagesTest/'+file.name;
          console.log(selectedImage.value)
        };

        const beforeUpload = (file: File) => {
          const isImage = file.type.indexOf('image') !== -1;
          if (!isImage) {

          }
          return isImage;
        };

        const confirmSelection = () => {
          // 处理选择图片后的逻辑
          console.log('选中的图片：', selectedImage.value);
          dialogVisible.value = false;
        };
        const showFileDialog = () => {
          dialogVisible.value = true;
        };
//到此为止
        async function getRubbishData() {
          try {

            const response = await axios.get('http://localhost:8080/GetRubbish?str=' + selectedImage.value);

           ;console.log('成功获取字符串数据',response.data)
            ReplyText.value = response.data;
          } catch (error) {
            console.error('请求错误', error);
          }
        }

        const sendMessage = async () => {
          await new Promise(resolve => setTimeout(resolve, 3000));
          console.log(JSON.stringify(messages.value) )
          messages.value.push({
            content: selectedImage.value,
            Type:'Pic',
            sender: 'Me',
          });
          var temp = message.value;
          selectedImage.value = ''
          messages.value.push({

            content: ReplyText.value,
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
        const BeingInput = (value:string ) =>{
          chatingname.value = value
        }
        // 选中值改变时的回调函数
        const onChange = (value: string) => {
          message.value = value;
          selectedValue.value = value;
        };
        return {
          message,
          messages,
          isMessageEmpty,
          chatingname,
          sendMessage,
          BeingInput,
          isDragging,
          dragX,
          dragY,
          getRubbishData,
          enableDragging,
          selectedValue,
          filteredData,
          onInput,
          onChange,
          getrecord,
          dialogVisible,
          selectedImage,
          showFileDialog,
          handleUploadChange,
          beforeUpload,
          confirmSelection,
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
.upload-demo {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  border: 1px solid #d9d9d9;
  border-radius: 2px;
  background-color: #fafafa;
  margin-bottom: 20px;
}
</style>
<template>
  <div class="chat" >
    <div class="chat-input-container" style="background-image: url(src/assets/Background2.jpg)" >
      <div  draggable="true" id="Putting"
            :style="{cursor: isDragging ? 'move' : 'default', position: 'absolute', left: dragX + 'px', top: dragY + 'px'}">
      <el-input type="text" v-model="message" placeholder="say something" @input="onInput" @keydown.enter="sendMessage"
                :style="{ background: isMessageEmpty ? 'cyan' : 'green'}"/>
      <el-select v-model="selectedValue" @change="onChange" style="width: 100%;background: cyan">
        <el-option v-for="(item, index) in filteredData" :key="index" :label="item" :value="item" style="width: 100%;"></el-option>
      </el-select>
      </div>
      <el-button @keydown.enter="sendMessage" @click="sendMessage" :disabled="isMessageEmpty" style="background: #589ef8 ; color: antiquewhite">Send</el-button>
    </div>
    <div class="chat-window" style="background-image: url(src/assets/Background.jpg) ;background-size: cover; ">
      <div v-for="(msg, index) in messages" :key="index"
           :class="{ 'chat-message': true, 'my-message': msg.sender === 'Me', 'reply-message': msg.sender === 'Reply' }">
        {{ msg.content }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, computed,watch} from 'vue';
import useDraggable from './useDraggable';



interface Message {
  content: string;
  sender: 'Me' | 'Reply';
}

export default defineComponent({
      name: 'Chat',

      setup() {
        const message = ref('');
        const messages = ref<Message[]>([]);

        const isMessageEmpty = computed(() => message.value.trim() === '');

        const sendMessage = () => {
          if (isMessageEmpty.value) {
            return;
          }
          messages.value.push({
            content: message.value,
            sender: 'Me',
          });
          message.value = '';
          messages.value.push({
            content: '发送成功',
            sender: 'Reply',
          });
        };
        const { isDragging, dragX, dragY, enableDragging } = useDraggable()
        const selectedValue = ref('');
        // 所有数据
        const data = ['我是学生', '你是老师','戴圣是神','xxn是坏女人'];
        // 过滤后的数据
        const filteredData = computed(() => {
          if (message.value === '') {
            return [];
          } else {
            return data.filter(item => item.includes(message.value));
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
          onChange
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
  height: 100%;
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
</style>
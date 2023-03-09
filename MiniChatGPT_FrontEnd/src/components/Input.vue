<template>
  <div class="chat">
    <div class="chat-input-container">
      <el-input type="text" draggable="true" v-model="message" placeholder="say something"
                :style="{ background: isMessageEmpty ? '#ddd' : 'green', cursor: isDragging ? 'move' : 'default', position: 'absolute', left: dragX + 'px', top: dragY + 'px'}"/>
      <el-button @click="sendMessage" :disabled="isMessageEmpty">Send</el-button>
    </div>
    <div class="chat-window">
      <div v-for="(msg, index) in messages" :key="index"
           :class="{ 'chat-message': true, 'my-message': msg.sender === 'Me', 'reply-message': msg.sender === 'Reply' }">
        {{ msg.content }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, computed} from 'vue';
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



        return {
          message,
          messages,
          isMessageEmpty,
          sendMessage,
          isDragging,
          dragX,
          dragY,
          enableDragging,
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
  width: 130%;
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
  color: #fff;
  cursor: pointer;
}

.chat-window {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
  height: 100%;
  overflow-y: auto;
  background-color: #eee;
  border-radius: 3px;
  padding: 10px;
}

.chat-message {
  max-width: 70%;
  word-break: break-all;
  padding: 5px 10px;
  margin-bottom: 5px;
  border-radius: 3px;
}

.my-message {
  background-color: #0077cc;
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
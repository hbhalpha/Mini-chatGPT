<script setup lang="ts">
import {inject, onMounted, provide, ref} from "vue";
import {ElMessage} from 'element-plus'
import component from "*.vue";
import axios from 'axios';
// export default {
//   name: "ChatWorld"
// }
var data = ref([]);
defineProps<{ msg: string }>();
onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8080/data');
    const jsonData = response.data;
    data.value = jsonData;
  } catch (error) {
    console.error(error);
    ElMessage.error('Failed to fetch data2 from server');
  }
});
const count = ref(0);
const input = ref("element-plus");

const curDate = ref('')

const toast = () => {
  ElMessage.success('Hello')

}


</script>

<template>

  <div id="main" v-if="msg === 'Chat'">

    <Input :data="data" :Mode="msg"></Input>
  </div>
  <div id="main"  v-else-if="msg === 'Rubbish' ">
    <RubbishInput :data="data" :Mode="msg"></RubbishInput>
  </div>
  <div id="main" v-else-if="msg === 'AI '">
    <Input :data="data" :Mode="msg"></Input>
  </div>


</template>

<style>
.ep-button {
  margin: 4px;
}

.ep-button + .ep-button {
  margin-left: 0;
  margin: 4px;
}

#main {
  display: flex;
  align-items: center;
  height: 100vh;
}

</style>

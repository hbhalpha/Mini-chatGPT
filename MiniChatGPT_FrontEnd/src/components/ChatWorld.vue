<script setup lang="ts">
import {ref} from "vue";
import {ElMessage} from 'element-plus'
// export default {
//   name: "ChatWorld"
// }

defineProps<{ msg: string }>();

const count = ref(0);
const input = ref("element-plus");

const curDate = ref('')

const toast = () => {
  ElMessage.success('Hello')
}
</script>

<template>
  <!--
  <div id="main">
    <h1>{{ msg }}</h1>

        <p>
          See
          <a href="https://element-plus.org" target="_blank">element-plus</a> for
          more information.
        </p>

        example components
    <div class="mb-4">
      <el-button size="large" @click="toast"><a href="www.baidu.com" >El Message</a></el-button>
    </div>

    <div class="my-2 text-center flex flex-wrap justify-center items-center">
      <el-button @click="count++">count is: {{ count }}</el-button>
      <el-button type="primary" @click="count++">count is: {{ count }}</el-button>
      <el-button type="success" @click="count++">count is: {{ count }}</el-button>
      <el-button type="warning" @click="count++">count is: {{ count }}</el-button>
      <el-button type="danger" @click="count++">count is: {{ count }}</el-button>
      <el-button type="info" @click="count++">count is: {{ count }}</el-button>
    </div>


    <div>
      <el-tag type="success" class="m-1">Tag 1</el-tag>
      <el-tag type="warning" class="m-1">Tag 1</el-tag>
      <el-tag type="danger" class="m-1">Tag 1</el-tag>
      <el-tag type="info" class="m-1">Tag 1</el-tag>
    </div>
  -->
  <div id="main">
    <Input ></Input>
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

<style scoped>

</style>
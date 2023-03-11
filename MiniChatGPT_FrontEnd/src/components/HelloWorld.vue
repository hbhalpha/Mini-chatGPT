<script setup lang="ts">
import { ref } from "vue";
import { ElMessage } from 'element-plus'

defineProps<{ msg: string }>();

const count = ref(0);
const input = ref("element-plus");

const curDate = ref('')

const toast = () => {
  ElMessage.success('Hello')
}
</script>

<template>
  <h1>{{ msg }}</h1>


  <p>TaiShanCollege,SDU,Hou BoHan</p>
  <!-- example components -->
  <div class="mb-4">
    <a href="chatIndex.html" > <el-button size="large" @click="toast">Try it Now </el-button></a>
  </div>

  <div class="my-2 text-center flex flex-wrap justify-center items-center">
    <a href="http://www.github.com" target="_blank"><el-button >github</el-button></a>
    <a href="http://www.baidu.com" target="_blank"><el-button type="primary">百度</el-button></a>
    <a href="http://www.google.com" target="_blank"><el-button type="success">google</el-button></a>
    <a href="http://www.bilibili.com" target="_blank"><el-button type="warning">b站</el-button></a>
    <a href="http://www.sdu.edu.cn" target="_blank"><el-button type="danger">山大</el-button></a>
    <a href="http://www.zhihu.com" target="_blank"><el-button type="info">知乎</el-button></a>
  </div>


  <div>
    <el-tag type="success" class="m-1">hbh</el-tag>
    <el-tag type="warning" class="m-1">Minichat</el-tag>
    <el-tag type="danger" class="m-1">hbh</el-tag>
    <el-tag type="info" class="m-1">Minichat</el-tag>
  </div>
  <p>项目介绍 这是一个项目介绍，点击Try it Now 进行尝试吧！</p>

</template>

<style>
.ep-button {
  margin: 4px;
}
.ep-button + .ep-button {
  margin-left: 0;
  margin: 4px;
}
</style>

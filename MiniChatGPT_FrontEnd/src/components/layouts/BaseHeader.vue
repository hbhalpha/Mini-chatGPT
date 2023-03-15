<script lang="ts" setup>
import { toggleDark } from '~/composables';
</script>

<template>
  <el-menu class="el-menu-demo" mode="horizontal">
    <el-menu-item index="1"><a href="index.html"> 返回主页</a></el-menu-item>
    <el-sub-menu index="2">
      <template #title>AI模式</template>
      <el-menu-item index="2-1"><a href="AI.html">AI女高</a></el-menu-item>
      <el-menu-item index="2-2">更多功能敬请期待</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="3" ><a href="chatIndex.html">聊天界面</a> </el-menu-item>
    <el-menu-item index="4"><a href="Rubbish.html">垃圾分类识别</a> </el-menu-item>
    <el-menu-item>

  </el-menu-item>
    <el-menu-item h="full" @click="toggleDark()">
      <button class="border-none w-full bg-transparent cursor-pointer" style="height: var(--ep-menu-item-height);">
        <i inline-flex i="dark:ep-moon ep-sunny" />
      </button>
    </el-menu-item>

  </el-menu>
</template>

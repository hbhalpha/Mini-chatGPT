<template>
  <el-menu
    default-active="2"
    class="el-menu-vertical-demo"
    :collapse="isCollapse"
    @open="handleOpen"
    @close="handleClose"
  >
    <el-sub-menu index="1">
      <template #title>
        <el-icon><location /></el-icon>
        <span>Navigator One</span>
      </template>
      <el-menu-item-group>
        <template #title><span>Group One</span></template>
        <el-menu-item v-for="(link, index) in links" :key="index" :index="index">
          <a :href="link.url">{{ link.name }}</a>
        </el-menu-item>
        <button @click="saveLink">Save</button>
      </el-menu-item-group>
      <el-menu-item-group title="Group Two">
        <el-menu-item index="1-3">item three</el-menu-item>
      </el-menu-item-group>
      <el-sub-menu index="1-4">
        <template #title><span>item four</span></template>
        <el-menu-item index="1-4-1">item one</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="2">
      <el-icon><icon-menu /></el-icon>
      <template #title>Navigator Two</template>
    </el-menu-item>
    <el-menu-item index="3" disabled>
      <el-icon><document /></el-icon>
      <template #title>Navigator Three</template>
    </el-menu-item>
    <el-menu-item index="4">
      <el-icon><setting /></el-icon>
      <template #title>Navigator Four</template>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import {
  Location,
  Document,
  Menu as IconMenu,
  Setting,
} from '@element-plus/icons-vue'

interface Link {
  name: string,
  url: string,
}
const isCollapse = ref(true)
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const links = ref<Link[]>([
  { name: 'item one', url: 'http://example.com/1' },
  { name: 'item two', url: 'http://example.com/2' },
])

const saveLink = () => {
  const name = 'item ' + (links.value.length + 1)
  const url = 'http://example.com/' + (links.value.length + 1)
  links.value.push({ name, url })
}
</script>

<style>
.ep-button {
  margin: 4px;
}

.ep-button + .ep-button {
  margin-left: 0;
  margin: 4px;
}

#main
{

  background-color: #eee;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  flex-direction: row;
  justify-content: end;
}

</style>

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
          <el-button @click="getRec(link.name)">{{ link.name }}</el-button>
        </el-menu-item>
        <el-button @click="saveLink">Save</el-button>
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
    <el-menu-item index="5"  >
      <Music style="width: 10%;display: flex;
  justify-content: center;"></Music>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
import {onMounted, ref} from 'vue'
import {
  Location,
  Document,
  Menu as IconMenu,
  Setting,
} from '@element-plus/icons-vue'
import axios from "axios";
import {inject} from "vue";
import path from 'path';
interface Link {
  name: string,
  url: string,
}
interface DataPost{
  Indicator : string;
  JsonData : string;
}
const isCollapse = ref(true)
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const links = ref<Link[]>([])
onMounted(() => {
  axios.get('http://localhost:8080/get_file_names')
      .then(response => {
        const fileList = response.data as string[];
        fileList.forEach(fileName => {
          links.value.push({
            name: fileName,
            url: `www.example.com`
          });
        });
      })
      .catch(error => {
        console.error(error);
      });
})
var name='';

const saveLink =async () => {


  const dataPost: DataPost = {
    Indicator: 'hbh',
    JsonData: JSON.stringify({}),
  };
  console.log("hbhhhhhhhhh")
  axios.post('http://localhost:8080/DataPost', JSON.stringify(dataPost), {
    headers: {
      'Content-Type': 'application/json',
    },
  })
      .then(response => {
        console.log(response.data);
        links.value=[];
        axios.get('http://localhost:8080/get_file_names')
            .then(response => {
              const fileList = response.data as string[];
              fileList.forEach(fileName => {
                links.value.push({
                  name: fileName,
                  url: `www.example.com`
                });
              });
            })
            .catch(error => {
              console.error(error);
            });
      })
      .catch(error => {
        console.error(error);
      });


}
async function getRec(arg:string) //应用于处理点击事件 和input中确定选择结合
{
  try {
    const response = await axios.get('http://localhost:8080/GetRecNum', {
      params: {
        str: arg ,
      }
    });
    console.log(arg)
  }
  catch (error)
  {
    console.log(error)
  }

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

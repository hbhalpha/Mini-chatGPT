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
        <el-icon><document /></el-icon>
        <span>Navigator One</span>
      </template>
      <el-menu-item-group>
        <template #title><span>谈论人</span></template>
        <el-menu-item v-for="(link, index) in links1" :key="index" :index="index">
            <el-button @click="getRec(link.name)">{{ link.name }}</el-button>
        </el-menu-item>

      </el-menu-item-group>
      <el-menu-item-group title="谈论事">
        <el-menu-item v-for="(link, index) in links2" :key="index" :index="index">
          <el-button @click="getRec(link.name)">{{ link.name }}</el-button>
        </el-menu-item>
      </el-menu-item-group>
      <el-menu-item index="1-4">
        <template #title><span>保存</span></template>
        <el-button @click="saveLink">Save</el-button>
      </el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="2">
      <template #title><el-icon><icon-menu /></el-icon></template>
      <el-menu-item>
        <a href="http://www.github.com" target="_blank"><el-button >github</el-button></a>
      </el-menu-item>
      <el-menu-item>
        <a href="http://www.baidu.com" target="_blank"><el-button type="primary">百度</el-button></a>
        </el-menu-item>
          <el-menu-item>
        <a href="http://www.google.com" target="_blank"><el-button type="success">google</el-button></a>
            </el-menu-item>
              <el-menu-item>
        <a href="http://www.bilibili.com" target="_blank"><el-button type="warning">b站</el-button></a>
                </el-menu-item>
                  <el-menu-item>
        <a href="http://www.sdu.edu.cn" target="_blank"><el-button type="danger">山大</el-button></a>
                    </el-menu-item>
                      <el-menu-item>
        <a href="http://www.zhihu.com" target="_blank"><el-button type="info">知乎</el-button></a>
                        </el-menu-item>


    </el-sub-menu>
    <el-sub-menu index="3" >
      <template #title><el-icon><watch /></el-icon></template>

      <el-menu-item-group> <el-date-picker class="m-2" v-model="curDate" type="date" placeholder="Pick a day"></el-date-picker></el-menu-item-group>

    </el-sub-menu>
    <el-menu-item index="4">
      <el-icon><setting /></el-icon>
      <template #title>关于作者：本项目由泰山学堂2022级计算机侯博涵开发</template>
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
  Setting, Clock, Timer, Watch, Aim,
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
const links1 = ref<Link[]>([])
const links2 = ref<Link[]>([])
onMounted(() => {
  axios.get('http://localhost:8080/get_file_names')
      .then(response => {
        const fileList = response.data as string[];
        fileList.forEach(fileName => {
          if(fileName.includes('玥玥'))
            links1.value.push({
              name: fileName,
              url: `www.example.com`
            });
          else
          {
            links2.value.push({
              name: fileName,
              url: `www.example.com`
            });
          }
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
        links1.value=[];
        links2.value=[]
        axios.get('http://localhost:8080/get_file_names')
            .then(response => {
              const fileList = response.data as string[];
              fileList.forEach(fileName => {
                if(fileName.includes('玥玥'))
                links1.value.push({
                  name: fileName,
                  url: `www.example.com`
                });
                else
                {
                  links2.value.push({
                    name: fileName,
                    url: `www.example.com`
                  });
                }
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

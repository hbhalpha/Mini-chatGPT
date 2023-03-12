<template>
  <div>
    <RankingList title="热点问题排行榜" :data="data" />
    <el-button @click="refreshData" >刷新</el-button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import RankingList from "~/components/RankingList.vue";
import axios from "axios";

export default defineComponent({
  components: {
    RankingList,
  },
  setup() {
    var data = ref([
    ]);

    const refreshData = async () => {
      try {
        const response = await axios.get('http://localhost:8080/data');
        data.value = response.data;
        console.log(data)
      } catch (error) {
        console.log(error);
      }
    };

    return {
      data,
      refreshData,
    };
  },
});
</script>

<style>
/* 样式可以自行定义 */
</style>

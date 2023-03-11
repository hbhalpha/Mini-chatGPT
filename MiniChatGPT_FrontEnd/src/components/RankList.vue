<template>
  <div >
    <RankingList title="热点问题排行榜" :data="data" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import RankingList from "~/components/RankingList.vue";


export default defineComponent({
  components: {
    RankingList,
  },
  data() {
    return {
      data: [
        { name: '我是人吗？', value: 3 },
        { name: 'lxy是坏女人吗？', value: 15000000 },
        { name: '戴圣是神吗？', value: 5 },
      ],
    };
  },
});
</script>

<style>
/* 样式可以自行定义 */
</style>

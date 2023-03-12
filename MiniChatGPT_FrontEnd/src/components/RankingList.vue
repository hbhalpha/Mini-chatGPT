<template>
  <div>
    <div style="background-image: url(src/assets/RankBack.png) ;background-size: cover">
    <h2 style="color: #42b8dd">{{ title }}</h2></div>
    <div >
    <ol>
      <li v-for="(item, index) in sortedData" :key="item.questions" style="color: white">
        {{ item.questions}} 热度 {{ item.HotValue }} <img src="src/assets/Fire.png">
      </li>
    </ol>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';

interface DataItem {
  id:number;
  questions: string;
  answers:string;
  HotValue: number;
}

export default defineComponent({
  props: {
    title: {
      type: String,
      required: true,
    },
    data: {
      type: Array as () => DataItem[],
      required: true,
    },
  },
  setup(props) {
    const sortedData = computed(() => {
      return props.data.sort((a, b) => b.HotValue - a.HotValue);
    });

    return {
      sortedData,
    };
  },
});
</script>

<style>
/* 样式可以自行定义 */
</style>

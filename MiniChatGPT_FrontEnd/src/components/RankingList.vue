<template>
  <div>
    <div style="background-image: url(src/assets/rktitle.webp) ;background-size: cover">
    <h2 style="color: #42b8dd">{{ title }}</h2></div>
    <div style="background-image: url(src/assets/RankBack.png);background-size: cover">
    <ol>
      <li v-for="(item, index) in sortedData" :key="item.name" style="color: white">
        {{ item.name }} 热度 {{ item.value }} <img src="src/assets/Fire.png">
      </li>
    </ol>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';

interface DataItem {
  name: string;
  value: number;
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
      return props.data.sort((a, b) => b.value - a.value);
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

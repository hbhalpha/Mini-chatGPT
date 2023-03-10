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

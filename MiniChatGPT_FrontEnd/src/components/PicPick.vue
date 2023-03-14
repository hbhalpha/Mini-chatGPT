<template>
  <div>
    <el-button @click="showFileDialog">选择图片</el-button>
    <el-dialog v-model="dialogVisible" title="选择图片" width="30%">
      <el-upload
          class="upload-demo"
          action="#"
          :show-file-list="false"
          :on-change="handleUploadChange"
          :before-upload="beforeUpload"
      >
        <el-button slot="trigger" size="large" type="primary">
          选择文件
        </el-button>
        <div slot="tip" class="el-upload__tip">
          只能选择图片文件
        </div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="confirmSelection">确认</el-button>
      </div>
    </el-dialog>
    <div v-if="selectedImage">
      <img  :src="selectedImage">
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'ImageSelector',
  setup() {
    const dialogVisible = ref(false);
    const selectedImage = ref('');
    var path:string;
    const showFileDialog = () => {
      dialogVisible.value = true;
    };

    const handleUploadChange = (file: Blob) => {
      if (!file) {
        console.error('No file provided!');
        return;
      }


      selectedImage.value = 'src/assets/'+file.name;
      console.log(selectedImage.value)
    };

    const beforeUpload = (file: File) => {
      const isImage = file.type.indexOf('image') !== -1;
      if (!isImage) {

      }
      return isImage;
    };

    const confirmSelection = () => {
      // 处理选择图片后的逻辑
      console.log('选中的图片：', selectedImage.value);
      dialogVisible.value = false;
    };

    return {
      dialogVisible,
      selectedImage,
      showFileDialog,
      handleUploadChange,
      beforeUpload,
      confirmSelection,
    };
  },
});
</script>

<style scoped>
.upload-demo {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  border: 1px solid #d9d9d9;
  border-radius: 2px;
  background-color: #fafafa;
  margin-bottom: 20px;
}
</style>



<style scoped>
.upload-demo {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  border: 1px solid #d9d9d9;
  border-radius: 2px;
  background-color: #fafafa;
  margin-bottom: 20px;
}
</style>

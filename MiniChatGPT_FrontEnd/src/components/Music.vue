<template>
  <div>
    <audio ref="audioPlayer" loop :src="musicUrl" autoplay></audio>
    <el-button @click="togglePlaying" style="width: 10%;display: flex;
  justify-content: center;background: #589ef8;color: white" >{{ isPlaying ? '暂停' : '播放' }}</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      musicUrl: 'src/assets/Taylor Swift - Cornelia Street.mp3', // 替换成你要播放的音乐地址
      isPlaying: true
    };
  },
  methods: {
    togglePlaying() {
      const audio = this.$refs.audioPlayer;
      if (this.isPlaying) {
        audio.pause();
      } else {
        audio.play();
      }
      this.isPlaying = !this.isPlaying;
    }
  }
};
</script>
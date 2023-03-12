<template>

  <el-config-provider namespace="ep">
    <div style="display: flex">
      <div style="background-image: url(src/assets/RankBack.png);background-size: cover"> <BaseHeader /></div>
    </div>
    <div style="display: flex">
      <div style="background-image: url(src/assets/RankBack2.webp);background-size: cover">  <BaseSide /></div>
      <div id="main1">
        <!-- <img alt="Vue logo" class="element-plus-logo" src="./assets/logo.png" />-->
       <ChatWorld  msg="这是练习项目1"  />
      </div>
    </div>

  </el-config-provider>
</template>
<script>

</script>
<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.element-plus-logo {
  width: 50%;
}
#main1
{
  height: calc(100vh - 58px);
  width: 95%;
  background-color: #eee;

  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
#main2
{
  width: 100%;
}
</style>

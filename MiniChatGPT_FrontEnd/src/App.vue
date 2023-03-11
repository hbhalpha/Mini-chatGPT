<template>
  <el-config-provider namespace="ep">
    <BaseHeader />

    <div style="display: flex">
      <BaseSide />
      <div id="main1">
       <img alt="Vue logo" class="element-plus-logo" src="./assets/SDULogo3.png" />
        <img alt="Vue logo"  src="./assets/hbhLogo.png" height="107" width="107" style="margin: auto"/>
        <HelloWorld msg="MiniChatGPT"  />
      </div>
    </div>
  </el-config-provider>
</template>
<script>
 //通讯

</script>
<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.element-plus-logo {
  margin: auto;
  width: 60%;

}
#main1
{
  height:100%;
  width: 100%;
  display: flex;
  flex-direction: column;

}
</style>

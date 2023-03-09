<template>
  <el-config-provider namespace="ep">
    <BaseHeader />
    <div style="display: flex">
      <BaseSide />
      <div id="main1">
      <!--  <img alt="Vue logo" class="element-plus-logo" src="./assets/logo.png" />-->
        <HelloWorld  msg="MiniChatGPT"  />
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
  width: 50%;
}
#main1
{
 height: calc(100vh - 58px);
  width: 100%;
  background-color: #eee;

  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
</style>

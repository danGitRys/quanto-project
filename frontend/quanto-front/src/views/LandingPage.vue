<template>
  <div>
     <TopBar></TopBar>
     <ProjectOverview></ProjectOverview>
      <SideBar class="sideBarPosition"/>
  </div>
</template>

<script setup>
  import TopBar from '@/components/TopBar.vue';
  import ProjectOverview from '@/components/ProjectOverview.vue';
  import SideBar from '@/components/SideBar.vue';
</script>

<style scoped>
.sideBarPosition {
    position: absolute;
    top: -100px;
    left: -120px;
   
}

</style>
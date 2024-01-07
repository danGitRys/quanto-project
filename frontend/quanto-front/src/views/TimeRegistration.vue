<template>
  <div>
  <TopBar />
<TimeRegistrationCo /> 
<SideBar class="sideBarPosition"/> 
  </div>
</template>

<script setup>
import TimeRegistrationCo from '../components/TimeRegistrationComponent.vue'
import TopBar from '@/components/TopBar.vue';
import SideBar from '@/components/SideBar.vue';
</script>

<style scoped>
.sideBarPosition {
    position: absolute;
    top: -100px;
    left: -120px;
   
}

</style>
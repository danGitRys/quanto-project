<template>
    <div>
    <TopBar />
    <NewProject />
    <SideBar class="sideBarPosition"/>
    </div>
</template>




<script setup>
import Default from '@/layouts/default/Default.vue';
import SideBar from '@/components/SideBar.vue';
import TopBar from '@/components/TopBar.vue';

import NewProject from '@/components/NewProject.vue';
import SubmitFooter from '@/components/SubmitFooter.vue';
</script>



<style scoped>
.sideBarPosition {
    position: absolute;
    top: -100px;
    left: -120px;
   
}

</style>


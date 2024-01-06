<template>

    <div>
         
        <TopBar />
      
        <BackgroundScreen />
        <ManageProjectTabelle />
        <ManageProject />
        <!-- <MitarbeiterTabelle /> -->
 
        <!-- <DropDownProjects /> -->
     <SideBar class="sideBarPosition"/>    
    </div>


</template>

<script setup>
import SideBar from '../components/SideBar.vue'
import ManageProject from '../components/ManageProject.vue'
// import DropDownProjects from '@/components/DropDownProjects.vue';
import TopBar from '@/components/TopBar.vue';
import ManageProjectTabelle from '@/components/ManageProjectTabelle.vue';
import MitarbeiterTabelle from '@/components/MitarbeiterTabelle.vue';
import BackgroundScreen from '@/components/BackgroundScreen.vue';
</script>




<style scoped>
.sideBarPosition {
    position: absolute;
    top: -100px;
    left: -120px;
   
}

</style>
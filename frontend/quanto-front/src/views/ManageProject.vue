<template>
    <div>
        <TopBar />
        <BackgroundScreen />
        <!-- <ManageProjectTabelle /> -->
        <ManageProject />
        <!-- <MitarbeiterTabelle /> -->
        <SideBarManager />
        <!-- <DropDownProjects /> -->
    </div>
</template>

<script setup>
import SideBarManager from '../components/SideBarManager.vue'
import ManageProject from '../components/ManageProject.vue'
// import DropDownProjects from '@/components/DropDownProjects.vue';
import TopBar from '@/components/TopBar.vue';
import ManageProjectTabelle from '@/components/ManageProjectTabelle.vue';
import MitarbeiterTabelle from '@/components/MitarbeiterTabelle.vue';
import BackgroundScreen from '@/components/BackgroundScreen.vue';
</script>

<style></style>
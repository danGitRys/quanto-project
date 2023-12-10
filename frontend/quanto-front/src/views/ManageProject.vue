<template>
    <div>
        <TopBar />
        <BackgroundScreen />
        <SideBarManager />
        <ManageProject />
        <MitarbeiterTabelle />
        <DropDownProjects />
    </div>
</template>

<script setup>
import SideBarManager from '../components/SideBarManager.vue'
import ManageProject from '../components/ManageProject.vue'
import DropDownProjects from '@/components/DropDownProjects.vue';
import TopBar from '@/components/TopBar.vue';
import MitarbeiterTabelle from '@/components/MitarbeiterTabelle.vue';
import BackgroundScreen from '@/components/BackgroundScreen.vue';
</script>

<style></style>
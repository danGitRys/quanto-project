<template>
    <div>
        <SideBarManager></SideBarManager>
        <TopBar />
        <BackgroundScreen />
        <ManageProject />
    </div>
</template>

<script setup>
import SideBarManager from '../components/SideBarManager.vue'
import ManageProject from '../components/ManageProject.vue'
import TopBar from '@/components/TopBar.vue';
import BackgroundScreen from '@/components/BackgroundScreen.vue';
</script>

<style></style>
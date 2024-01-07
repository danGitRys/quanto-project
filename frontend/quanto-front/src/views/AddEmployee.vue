<template>
    <Sidebar class="sideBarPosition"/>
    <TopBar />
    <AddEmployee />
</template>

<script setup>
import AddEmployee from '../components/AddEmployee.vue';
import Sidebar from '@/components/SideBar.vue';
import TopBar from '@/components/TopBar.vue';
</script>

<style>
.sideBarPosition {
    position: absolute;
    top: -100px;
    left: -120px;
   
}
</style>
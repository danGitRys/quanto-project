<script setup>
import SingleProject from '@/components/SingleProject.vue';
import Default from '@/layouts/default/Default.vue';
import SideBarManager from '@/components/SideBarManager.vue';
</script>

<template>

    <div>
    <Default />
     <div class="singleProjectStyle">
    <SingleProject/>
    </div>
     <SideBarManager/>
    </div>
</template>

<style scoped>

.singleProjectStyle{
    margin-left: 80px ;
    margin-top: 10px ;
}


</style>
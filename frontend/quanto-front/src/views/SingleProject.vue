<script setup>
import SingleProject from '@/components/SingleProject.vue';
import Default from '@/layouts/default/Default.vue';
import SideBar from '@/components/SideBar.vue';
</script>

<template>

    <div>
    <Default />
        <div class="singleProjectStyle">
            <SingleProject/>
        </div>
    <SideBar />
    </div>
</template>

<style scoped>

.singleProjectStyle{
    margin-left: 80px ;
    margin-top: 10px ;
}

</style>
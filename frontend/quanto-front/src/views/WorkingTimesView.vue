<template>
    <div class="container">
        
           <Default/>
        <WorkingTimesPlus class="workingTimes"  />
       <SideBarManager/>
       <!-- SideBar aus dem Default Layout entfernt damit sie die andere Ansicht überdeckt-->
    </div>
</template>

<script setup>
import WorkingTimesPlus from '@/components/WorkingTimesPlus.vue';
import Default from '@/layouts/default/Default.vue';
import Test from '@/components/Test.vue';
import SideBarManager from '@/components/SideBarManager.vue';
</script>

<style scoped>



.workingTimes{
    margin-top: 12px;
    margin-left: 100px;

}

</style>

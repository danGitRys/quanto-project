<template>
    <div class="container">
        
           <Default/>
        <!-- <component :is="getWorkingTimesComponent" class="workingTimes" /> -->
        <!-- <WorkingTimes class="workingTimes"/> -->
        <WorkingTimesPlus class="workingTimes"/>
       <SideBarManager/>
       <!-- SideBar aus dem Default Layout entfernt damit sie die andere Ansicht überdeckt-->
    </div>
</template>

<script setup>
import WorkingTimesPlus from '@/components/WorkingTimesPlus.vue';
import Default from '@/layouts/default/Default.vue';
import Test from '@/components/Test.vue';
import SideBarManager from '@/components/SideBarManager.vue';
import WorkingTimes from '@/components/WorkingTimes.vue';



const getWorkingTimesComponent = () => {
    // Hier könntest du die Logik für die Anzeige der richtigen Komponente basierend auf dem Benutzer implementieren
    const isManager = false;
    console.log('isManager:', isManager); // Überprüfe den Wert von isManager
    console.log('test') // Beispiel: Hier solltest du die wirkliche Logik verwenden
    return isManager ? WorkingTimesPlus : WorkingTimes;
};






</script>

<style scoped>



.workingTimes{
    margin-top: 12px;
    margin-left: 100px;

}

</style>

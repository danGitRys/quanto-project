<template>
  <div>
     <TopBar></TopBar>
     <ProjectOverview></ProjectOverview>
     <SideBarMitarbeiter />
  </div>
</template>

<script setup>
  import TopBar from '@/components/TopBar.vue';
  import ProjectOverview from '@/components/ProjectOverview.vue';
  import SideBarMitarbeiter from '@/components/SideBarMitarbeiter.vue';
</script>


<template>
    <div>
        <div class="dropDown">
            <!-- Dropdown-Komponente mit v-model, options und optionLabel -->
            <Dropdown v-model="selectedProject" :options="projects" placeholder="Select a Project"
                 class="w-full md:w-14rem" @update:modelValue="test"/>
        </div>
    </div>
</template>

<script setup>
import Dropdown from 'primevue/dropdown';
import { ref, onUpdated, onMounted } from 'vue';
import axios from 'axios';

const selectedProject = ref();
const projects = [];
let chosenProject = "";

onUpdated(() => {
    chosenProject = selectedProject.value;
    console.log(chosenProject);
});

onMounted(() => {
    //getDataFromBackend();
    getProjectsFromBackend();
})

const getProjectsFromBackend = () => {
    const url = 'http://localhost:8000/getAllProjects/'
    axios.get(url)
    .then(response => {
      //console.log(response.data.data[0]);
      for(let i = 0; i < response.data.data.length; i++) {
        projects.push(response.data.data[i].name);
      }
    });
}

function test() {
    console.log("test");
}
</script>

<style>
.p-dropdown {
    left: 20em;
    width: 30em;
    text-align: center;
    bottom: 0.5em;
}
</style>

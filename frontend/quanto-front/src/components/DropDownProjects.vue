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
    getDataFromBackend();
})

async function getDataFromBackend() {
    const url = "http://localhost:8000/getProject/2";
    const response = await axios.get(url);
    console.log(response.data.data.name);
    projects.push(response.data.data.name);
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

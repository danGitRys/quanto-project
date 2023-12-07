<template>
    <div class="container">
        <v-app>
            <v-container>
                <v-select label="Project" :items="items" variant="outlined"></v-select>
            </v-container>
        </v-app>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAppStore } from '@/store/app';

const selectedProjectName = ref('');
const selectedProjectPosition = ref('');
const appStore = useAppStore();
const optionsData = appStore.names;

let items = [];

for (let i = 0; i < optionsData.length; i++) {
    items[i] = optionsData[i];
}

</script>

<style scoped>
.v-application__wrap {
    min-height: 0vh !important;
}

.v-container {
    width: 80%;
}
</style>
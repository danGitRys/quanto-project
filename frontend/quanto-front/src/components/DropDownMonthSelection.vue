<template>
    <div>
        <div class="card flex justify-content-center">
            <!-- Dropdown-Komponente mit v-model, options und optionLabel -->
            <Dropdown v-model="selectedMonth" :options="months" optionLabel="name" placeholder="Select a Month"
                 class="w-full md:w-14rem" />
        </div>
    </div>
</template>

<script setup>
import Dropdown from 'primevue/dropdown';
import { ref, onUpdated } from 'vue';

const selectedMonth = ref();

const months = ref([
   { name: "Januar", code: "1" },
    { name: "Februar", code: "2" },
    { name: "März", code: "3" },
    { name: "April", code: "4" },
    { name: "Mai", code: "5" },
    { name: "Juni", code: "6" },
    { name: "Juli", code: "7" },
    { name: "August", code: "8" },
    { name: "September", code: "9" },
    { name: "Oktober", code: "10" },
    { name: "November", code: "11" },
    { name: "Dezember", code: "12" },
]);

let chosenMonth ="";

onUpdated(() => {
    console.log('Update');
    chosenMonth = selectedMonth.value.code; // Nutze die reaktive Variable direkt
    console.log(chosenMonth);

});

</script>



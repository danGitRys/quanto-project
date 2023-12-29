<template>
    <div>
        <DataTable :value="[tuesday]" tableStyle="min-width: 10rem">
            <Column field="planned" header="Planned"></Column>
            <Column field="working" header="Working"></Column>
            <Column field="break" header="Break"></Column>
            <Column field="sum" header="Summe"></Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref, defineProps, watch } from 'vue';

const props = defineProps(['tuesday']);



</script>

<template>
    <div>
        <DataTable :value="mittwoch" tableStyle="min-width: 10rem">
            <Column field="planned" header="Planned"></Column>
            <Column field="working" header="Working"></Column>
            <Column field="break" header="Break"></Column>
            <Column field="sum" header="Summe"></Column>
        </DataTable>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps(['mittwoch']);



</script>

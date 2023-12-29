<template>
    <div>
        <DataTable :value="data" tableStyle="min-width: 10rem">
            <Column field="code" header="Montag">
                <template #body="slotProps">
                    {{ console.log(slotProps) }}
                    <InnerTable2 :people="slotProps.data" />
                </template>
            </Column>
            <Column field="name" header="Dienstag">
                <template #body="slotProps">
                    {{ console.log("Dienstag " + slotProps) }}
                    <InnerTable3 :tuesday="slotProps.data" />
                </template>
            </Column>
            <Column field="category" header="Mittwoch">
                <template #body="slotProps">
                 
                    <InnerTable4  :mittwoch="xx" />
                </template>
            </Column>
            <Column field="quantity" header="Quantity"></Column>
        </DataTable>
    </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import InnerTable2 from './InnerTable2.vue';
import InnerTable3 from './InnerTable3.vue';
import InnerTable4 from './InnerTable4.vue';

const monday = [
    { planned: '8', working: '8', break: '0', sum: '8' },
    { planned: '2', working: '0', break: '1', sum: '7' },
    { planned: '1177', working: '28', break: '0', sum: '899' },
];

const tuesday = [
    { planned: '2444', working: '888', break: '111', sum: '22222' },
    // other Tuesday data...
];
const data = ref([...monday, ...tuesday]);


const xx = ref([
    { planned: '1', working: '00', break: '111', sum: '22222' },
    { planned: '2', working: '00', break: '111', sum: '22222' },
    { planned: '3', working: '0', break: '111', sum: '22222' },
])
   
    // other Tuesday data...





</script>

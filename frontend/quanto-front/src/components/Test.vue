<template>
    <div>
        <DataTable :value="products" tableStyle="min-width: 10rem">
            <Column field="code" header="Code">
                <template #body="slotProps">
                    <DataTable :value="innerTable" tableStyle="min-width: 10rem">
                        <Column field="code" header="Überschrift"></Column>
                        <Column field="name" header="Autor"></Column>
                        <Column field="working" header="Working"></Column>
                        <Column field="planed" header="Planed"></Column>
                    </DataTable>
                </template>
            </Column>
            <Column field="name" header="Name"></Column>
            <Column field="category" header="Category"></Column>
            <Column field="quantity" header="Quantity"></Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const products = ref([
    { code: '1000', name: 'Samsung', category: 'Cellphone', quantity: 10 },
    { code: '1001', name: 'Huawei', category: 'Cellphone', quantity: 15 },
]);

const innerTable = ref([
    { code: '1000', name: 'Samsung', working: '8', planed: 10 },
    { code: '1001', name: 'Huawei', working: '27', planed: 800 },
]);

const newTable = ref([
    { code: '2000', name: 'Apple', category: 'Tablet', quantity: 5 },
    { code: '2001', name: 'Sony', category: 'TV', quantity: 20 },
]);

newTable.value[0].name = 'Test'

// Funktion zum Austauschen der Tabellen aufrufen
replaceTable();

function replaceTable() {
    // Ersetze die gesamte Tabelle durch eine andere
    innerTable.value = [...newTable.value];
}
</script>

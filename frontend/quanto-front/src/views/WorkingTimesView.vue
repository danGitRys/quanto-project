<template>
    <div class="card">
        <DataTable :value="products" tableStyle="min-width: 50rem">
            <Column field="code" header="Code"></Column>
            <Column field="name" header="Name">
                <template #body="{ row }">
                    <DataTable :value="innerTable">
                        <Column field="innerCode" header="Inner Code"></Column>
                        <!-- Weitere Spalten für die innere Tabelle -->
                    </DataTable>
                </template>
            </Column>
            <Column field="category" header="Category"></Column>
            <Column field="quantity" header="Quantity"></Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const products = ref([]);
const innerTable = ref([]);

onMounted(() => {
    getDataFromBackend();
});

async function getDataFromBackend() {
    try {
        const url = "http://localhost:8000/getPositionsOfProjectOfEmployee/2008"
        const response = await axios.get(url);
        processData(response.data.positions);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


const data = ref({innerCode: "XXXX"}) 
    


function processData(backendData) {
    products.value = backendData.map(item => ({
        code: item.id,
        name: innerTable.value.push(data.value)
        
        
    }));

    


}
</script>

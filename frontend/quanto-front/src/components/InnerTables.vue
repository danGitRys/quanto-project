
<template>
    <div class="card">
        <DataTable :value="products" tableStyle="min-width: 50rem">
            <Column field="code" header="Code"></Column>
            <Column field="name" header="Name"></Column>
            <Column field="category" header="Category"></Column>
            <Column field="quantity" header="Quantity"></Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import { useMyStore } from '@/store/innerTable';

const x = useMyStore();


    const z = x.fetchBookingTimes(3013, '25.12.2023')
    .then(z => {
       const dataArray = z.data.bookingTimes
       dataArray.forEach((element) => {
            products.value.push({
                code: element.start_time,
                name: element.end_time,
                category: element.forecast_start,
                quantity: element.pause,
            });

       }) 
    })






const products = ref([]);




</script>

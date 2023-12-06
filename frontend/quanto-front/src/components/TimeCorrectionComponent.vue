<template>
    <div class="card p-fluid">
        <DataTable :value="products" editMode="cell" @cell-edit-complete="onCellEditComplete" :pt="{
            table: { style: 'min-width: 50rem' },
            column: {
                bodycell: ({ state }) => ({
                    class: [{ 'pt-0 pb-0': state['d_editing'] }],
                }),
            },
        }">
            <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" style="width: 25%">
                <template #body="{ data, field }">
                    
                    <template v-if="field === 'date'">
                         <div>
                               <div v-for="(value, index) in data[field]" :key="index">
                        <InputText v-model="data[field][index]" />
                        </div>
                                </div>
                        </template>



                     
                    <!--Planed Spalte wird dynamisch mit Werten gefüllt aus <service/ProductService> (planed)  -->
                    <template v-else-if="field === 'planed'">
                        <div>
                           <div v-for="(value, index) in data[field]" :key="index">
                        <InputNumber v-model="data[field][index]" @input="onInput" />

                        </div>
                            </div>
                    </template>
                    

                    
                   <!-- Hier wird die WorkedSpalte dyamisch mit Daten gefüllt aus <service/ProductService> --> 
                    <template v-else-if="field === 'worked'">
        <div>
            <div v-for="(value, index) in data[field]" :key="index">
                <InputNumber v-model="data[field][index]" @input="onInput" />
            </div>
        </div>
    </template>
 



    </template>
            </Column>
        </DataTable>
    </div>
    
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { ProductService } from '@/service/ProductService';
import InputText from 'primevue/inputtext'
// Muss importiert werden, um Nummer eingeben zu können in der
import InputNumber from 'primevue/inputnumber';

const products = ref();
const columns = ref([
    { field: 'date', header: 'Date' },
    { field: 'planed', header: 'Planed' },
    { field: 'worked', header: 'Worked' },
    { field: 'positions', header: 'Pos' },
]);

onMounted(() => {
    ProductService.getProductsMini().then((data) => (products.value = data));
});




</script>

<style scoped>

.p-inputnumber, .p-inputtext{
    
    background-color:red;
    font-size: 20px;
  
}

</style>

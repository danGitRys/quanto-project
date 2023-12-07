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
 
        <template v-else-if="field === 'positions'">
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
import { ref, onMounted, reactive } from 'vue';
//import { ProductService } from '@/service/ProductService';
import InputText from 'primevue/inputtext'
// Muss importiert werden, um Nummer eingeben zu können in der
import InputNumber from 'primevue/inputnumber';
import axios from 'axios';



const products = ref();
const columns = ref([
    { field: 'date', header: 'Date' },
    { field: 'planed', header: 'Planed' },
    { field: 'worked', header: 'Worked' },
    { field: 'positions', header: 'Pos' },
]);


const data = reactive([
    {
        date:   [],
        planed: [],
        worked: [],
        positions:[]
    },

])

products.value = data;

onMounted(() => {
    getDataFromBackend();
    
});



let resArray = [];

async function getDataFromBackend(){
    const url = "http://localhost:8000/getForecastOfEmployee/1002";
    const response = await axios.get(url);
    console.log(response)
    resArray = response.data.forecast;
    console.log(resArray);
    resArray.forEach((element,index) => {
       data[0].date.push(element.date)
       data[0].planed.push(element.duration)
       data[0].worked.push(element.worked)
       data[0].positions.push(element.fk_position)
    

    })

}



</script>

<style scoped>

.p-inputnumber, .p-inputtext{
    
    background-color:red;
    font-size: 20px;
  
}

</style>

<template>
    <div class="card p-fluid">
        <DataTable :value="[people]" editMode="cell" @cell-edit-complete="onCellEditComplete" :pt="{
            table: { style: 'min-width: 15rem' },
            column: {
                bodycell: ({ state }) => ({
                    class: [{ 'pt-0 pb-0': state['d_editing'] }]
                })
            }
        }">
            <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" style="width: 5%">
                <template #body="{ data, field }">
                    {{ field === 'price' ? formatCurrency(data[field]) : data[field] }}
                </template>
                <template #editor="{ data, field }">
                    <template v-if="field == 'working'">
                        <InputText v-model="data[field]" autofocus />
                    </template>
                    <template v-else>

                    </template>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const props = defineProps(['people']);


const columns = ref([
    { field: 'planned', header: 'Planed' },
    { field: 'working', header: 'Working' },
    { field: 'break', header: 'Break' },
    { field: 'sum', header: 'Summe' }
]);


const onCellEditComplete = async (event) => {
    let { data, newValue, field } = event;

    try{
        if(field === 'working') {
            event.preventDefault();
         //if (newValue.trim().length > 0) data[field] = newValue;
        const x = event.newData
        console.log(x)
        const working = x.working;
        const start =  working.slice(0, 5);
            const end =  working.slice(6, 11);
            console.log(start)
            console.log(end)
            const testDate = x.selectedDate;


            const data = {
                fk_employee: 15,
                fk_position: 1,
                start: '2023-12-28' + ' ' + start + ':00' ,
                end: '2023-12-28' + ' ' + end + ':00',
                pause: '1'
            }
        console.log(data)

        const url = 'http://localhost:8000/updateBooking/3020';
        const response = await axios.put(url, data); 
        console.log(response)
    }
    }
    catch(error){
        console.log(error);
    }


};




</script>

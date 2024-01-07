<template>
<div class="card p-fluid">
        <DataTable :value="[people]" editMode="cell" @cell-edit-complete="onCellEditComplete"
            :pt="{
                table: { style: 'min-width: 5rem' },
                column: {
                    bodycell: ({ state }) => ({
                        class: [{ 'pt-0 pb-0': state['d_editing'] }]
                    })
                }
            }"
        >
            <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" style="width: 25%">
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
const props = defineProps(['people']);


const columns = ref([
    { field: 'planned', header: 'Planed' },
    { field: 'working', header: 'Working' },
    { field: 'break', header: 'Break' },
    { field: 'sum', header: 'Summe' }
]);


const onCellEditComplete = (event) => {
    let { data, newValue, field } = event;

    switch (field) {
        case 'quantity':
        case 'price':
            if (isPositiveInteger(newValue)) data[field] = newValue;
            else event.preventDefault();
            break;

        default:
            if (newValue.trim().length > 0) data[field] = newValue;
            else event.preventDefault();
            break;
    }
};




</script>

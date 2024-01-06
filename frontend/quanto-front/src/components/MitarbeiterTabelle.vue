<template>
  <DataTable
    class="dataTable"
    v-model:editingRows="editingRows"
    :value="tableData"
    editMode="row"
    dataKey="id"
    @row-edit-save="onRowEditSave"
    :pt="{
      table: { style: 'min-width: 10em'  },
      column: {
        bodycell: ({ state }) => ({
          style: state['d_editing'] && 'padding-top: 0.6rem; padding-bottom: 0.6rem',
        }),
      },
    }"
  >
    <Column field="hours_all_project" header="Hours all Project" style="width: 20%">
      <template>
        <InputText v-if="field !== 'hours_all_project'" v-model="data[field]" />
        <InputText v-else :value="data[field]" readonly />
      </template>
    </Column>
    <Column field="hours_this_project" header="Hours this Project" style="width: 20%">
      <template #editor="{ data, field }">
        <InputText v-model="data[field]" />
      </template>
    </Column>
    <Column field="pos" header="Pos" style="width: 20%">
      <template #editor="{ data, field, index }">
        <Dropdown
          v-model="data[field]"
          :options="getPositionsForDate(data.date)"
          option-label="label"
          placeholder="Select a Position"
        >
          <template #option="slotProps">
            <Tag :value="slotProps.option.value" />
          </template>
        </Dropdown>
      </template>
      <template #body="slotProps">
        <div slotProps.data.pos></div>
        <div v-for="(pos, index) in Object.values(posArray)" :key="index">
        <Tag :value="pos.label" />
      </div>
      </template>
    </Column>
    <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center"></Column>
  </DataTable>
</template>

<script setup>
import { ref, defineProps } from 'vue';
import InputText from 'primevue/inputtext';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Tag from 'primevue/tag';
import Dropdown from 'primevue/dropdown';

const { name, tableData, generatedDate, selectedProject, allProjects } = defineProps([
  'name',
  'tableData',
  'generatedDate',
  'selectedProject',
  'allProjects',
]);

// console.log(generatedDate);
const editingRows = ref([]);
const tableArray = tableData;
let posArray = ref([]);
posArray.value.push({label: "test"});

// console.log("TABLEARRAY");
// console.log(tableArray);
const pos = ref([])

const getPositionsForDate = (date) => {
  const dateItem = tableData.find(item => {
    const itemDate = new Date(item.date).toISOString().split('T')[0];
    // console.log(itemDate)
    return itemDate === date.toISOString().split('T')[0];
  });
  // console.log(dateItem)
  return dateItem ? dateItem.pos : "Test";
};


const onRowEditSave = (event) => {
  let { newData, index } = event;
  // if(tableArray[index].pos == tableData[index].pos) {
  //   posArray = tableData[index].pos;
  // }
  console.log(tableArray[index].pos);
  console.log(posArray);
  let _data = tableData[index];
  _data.pos
  console.log(pos.value);
  console.log(newData);
  _data.pos = pos.value;
  tableData[index] = _data;
  tableData[index].hours_this_project = newData.hours_this_project;
};
</script>



<style>
.card {
  position: absolute;
  left: 10em;
  top: 15em;
}

ul {
  list-style: none;
}

.dates {
  position: absolute;
  top: 1.4em;
  font-size: larger;
  line-height: 1.72;
  width: 10em;
}

.containerProjectMonth {
  display: flex;
  flex-direction: column;
  align-items:center;
}

.monthPicker {
position: relative;
border: 1px solid black;
right: 17em;
text-align: center;
top: 1em;

}

.p-datatable {
width: 50em;
left: 10em;
  
}

.p-datatable .p-datatable-tbody td,
.p-datatable .p-datatable-thead th,
.p-datatable .p-datatable-tfoot td {
text-align: center; /* Center align the content within cells */
}

.names {
position: absolute;
top: -1.5em;
left: 15em;
}

</style>
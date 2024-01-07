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
    <div v-if="slotProps.data.inProjectDetail && slotProps.data.inProjectDetail.length > 0">
      <!-- Display positions from InProjectDetail -->
      <div v-for="detail in slotProps.data.inProjectDetail">
        <Tag :value="detail.info.position_name" />
      </div>
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

const { name, tableData, generatedDate, chosenProjectId, allProjects } = defineProps([
  'name',
  'tableData',
  'generatedDate',
  'chosenProjectId',
  'allProjects',
]);

// console.log(generatedDate);
const editingRows = ref([]);
const tableArray = tableData;
console.log(name);
console.log(tableData);
console.log(generatedDate);
console.log(chosenProjectId);
console.log(allProjects);

// console.log("TABLEARRAY");
// console.log(tableArray);

const getPositionsForDate = (date) => {
  const dateItem = tableData.find(item => {
    const itemDate = new Date(item.date).toISOString().split('T')[0];
    return itemDate === date.toISOString().split('T')[0];
  });

  return dateItem ? dateItem.pos.map(pos => ({ label: pos.name, value: pos.name })) : [];
};



const onRowEditSave = (event) => {
  let { newData, index } = event;
  const url = 'http://localhost:8000/createForecast';
  console.log(tableArray[index].pos);

  let _data = tableData[index];
  console.log(tableData[index]);
  console.log(newData);
  
  let fk_pos;

  // Find the corresponding date in dataTable
  // const dateInDataTable = tableData.find(item => {
  //   const itemDate = new Date(item.date).toISOString().split('T')[0];
  //   return itemDate === newData.date.toISOString().split('T')[0];
  // });

  // // If dateInDataTable exists, update the selected position based on it
  // if (dateInDataTable && dateInDataTable.inProjectDetail) {
  //   const positions = dateInDataTable.inProjectDetail.map(detail => detail.info.position_name);
  //   _data.pos = positions.length > 0 ? positions[0] : null; // Set to the first position or null if no positions
  // }
  _data.inProjectDetail = newData.pos;
  
  if(newData.pos.label==_data.pos.name) {
    fk_pos = _data.pos.value;
  }

  const requestData = {
    fk_employee: newData.empId,
    fk_position: fk_pos,
    start: "2024-01-01",
    end: "2024-01-01",
    info: ""
  }

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
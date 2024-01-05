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
      <template #editor="{ data, field }">
        <Dropdown
          v-model="data[field]"
          :options="getPositionsForDate(data.date)"
          optionLabel="name"
          optionValue="value"
          placeholder="Select a Position"
        >
          <template #option="slotProps">
            <Tag :value="slotProps.option.value" :severity="getStatusLabel(slotProps.option.value)" />
          </template>
        </Dropdown>
      </template>
      <template #body="slotProps">
        <Tag :value="slotProps.data.pos" :severity="getStatusLabel(slotProps.data.pos)" />
      </template>
    </Column>
    <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center"></Column>
  </DataTable>
</template>

<script setup>
import { ref, watch, defineProps } from 'vue';
import InputText from 'primevue/inputtext';
import Dropdown from 'primevue/dropdown';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Tag from 'primevue/tag';

const { name, tableData, generatedDate, selectedProject, allProjects } = defineProps([
  'name',
  'tableData',
  'generatedDate',
  'selectedProject',
  'allProjects',
]);

console.log(generatedDate);
const editingRows = ref([]);
let statuses = ref([]);
const tableArray = tableData;
console.log("TABLEARRAY");
console.log(tableArray);

const getPositionsForDate = (date) => {
  const dateItem = tableData.find(item => {
    const itemDate = new Date(item.date).toISOString().split('T')[0];
    return itemDate === date.toISOString().split('T')[0];
  });

  return dateItem ? dateItem.pos : [];
};



watch(() => selectedProject, (newProject) => {
  console.log('IN WATCH' + allProjects.length);
  console.log(allProjects);
  employeesData.value = [];
  generatedDate.value = [];

  if (allProjects.length > 0) {
    for (let i = 0; i < allProjects.length; i++) {
      if (newProject == allProjects[i].name) {
        // chosenProjectId = allProjects[i].id;
        console.log(allProjects[i].id);
      }
    }
  }
});

const onRowEditSave = (event) => {
  let { newData, index } = event;
  console.log(newData);
  newData.pos = [newData.pos];

  tableData[index] = newData;
};

const getStatusLabel = (status) => {
  console.log(status);
  switch (status) {
    case `${tableData[0].pos[0].value}`:
      return 'success';

    case 'LOWSTOCK':
      return 'warning';

    case 'OUTOFSTOCK':
      return 'danger';

    default:
      return null;
  }
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
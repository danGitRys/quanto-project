<template>
    <div class="containerProjectMonth">
      <!-- Dropdowns for project selection -->
        <div class="dropdownProject">
          <Dropdown
            v-model="selectedProject"
            :options="projects"
            placeholder="Select a Project"
            style="width: 20em;"
          />
        </div>
      <!-- Calendar for month selection -->
      <div class="monthPicker">
        <Calendar
          v-model="dateMonthPicker"
          view="month"
          dateFormat="mm/yy"
          placeholder="Select a Date"
          @update:model-value="generateDatesForSelectedMonthTEST"
        ></Calendar>
      </div>
    </div>
    <div class="card p-fluid">
        <div class="dates">
            <ul>
                <li v-for="(dateItem, index) in generatedDate" :key="index">
                    {{ formatDateTime(dateItem.date) }}
                </li>
            </ul>
        </div>
    <div >
        <DataTable class="dataTable" v-model:editingRows="editingRows" :value="tableData" editMode="row" dataKey="id" @row-edit-save="onRowEditSave" 
            :pt="{
                table: { style: 'min-width: 10em' },
                column: {
                    bodycell: ({ state }) => ({
                        style:  state['d_editing']&&'padding-top: 0.6rem; padding-bottom: 0.6rem' 
                    })
                }
            }"
        >
            <Column field="hours_all_project" header="Hours all Project" style="width: 20%">
                <template #editor="{ data, field }">
                    <InputText v-model="data[field]" />
                </template>
            </Column>
            <Column field="hours_this_project" header="Hours this Project" style="width: 20%">
                <template #editor="{ data, field }">
                    <InputText v-model="data[field]" />
                </template>
            </Column>
            <Column field="pos" header="Pos" style="width: 20%">
                <template #editor="{ data, field }">
                    <Dropdown v-model="data[field]" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status">
                        <template #option="slotProps">
                            <Tag :value="slotProps.option.value" :severity="getStatusLabel(slotProps.option.value)" />
                        </template>
                    </Dropdown>
                </template>
                <template #body="slotProps">
                    <Tag :value="slotProps.data.inventoryStatus" :severity="getStatusLabel(slotProps.data.inventoryStatus)" />
                </template>
            </Column>
            <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center">ha</Column>
        </DataTable>
    </div>
</div>
</template>

<script setup>
import { ref, onMounted, onUpdated, watch } from 'vue';
import Calendar from 'primevue/calendar';
import axios from 'axios';
import InputText from 'primevue/inputtext';
import Dropdown from 'primevue/dropdown';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Tag from 'primevue/tag';

const generatedDate = ref([]);
const dateMonthPicker = ref(new Date());
const selectedProject = ref();
const projects = [];
const allProjects = [];
let chosenProject = '';
let chosenProjectId = '';

const tableData = ref();
const editingRows = ref([]);
const statuses = ref([
    { label: 'In Stock', value: 'INSTOCK' },
    { label: 'Low Stock', value: 'LOWSTOCK' },
    { label: 'Out of Stock', value: 'OUTOFSTOCK' }
]);

onMounted(() => {
    getProjectsFromBackend();
    generateDatesForSelectedMonthTEST();
});

const getProjectsFromBackend = async () => {
    console.log('AUCH HIER');
    
    const url = 'http://localhost:8000/getAllProjects/';
    await axios.get(url).then((response) => {
      for (let i = 0; i < response.data.data.length; i++) {
        projects.push(response.data.data[i].name);
        allProjects.push(response.data.data[i]);
        console.log('allProjects');
        console.log(allProjects);
      }
    });
};

watch(selectedProject, (newProject) => {
  chosenProject = newProject;
  console.log('IN WATCH' + allProjects.length);
  console.log(allProjects);
  if (allProjects.length > 0) {
    for (let i = 0; i < allProjects.length; i++) {
      if (chosenProject == allProjects[i].name) {
        chosenProjectId = allProjects[i].id;
        getDataFromBackend(chosenProjectId);
        console.log(chosenProjectId);
      }
    }
  }
});

const generateTableDataForSelectedMonth = () => {
  tableData.value = generatedDate.value.map((dateItem, index) => ({
    id: index + 1, // Assign a unique id for each entry
    date: dateItem.date,
    hours_all_project: '',
    hours_this_project: '',
    pos: '',
  }));
};

const onRowEditSave = (event) => {
    let { newData, index } = event;

    tableData.value[index] = newData;
};
const getStatusLabel = (status) => {
    switch (status) {
        case 'INSTOCK':
            return 'success';

        case 'LOWSTOCK':
            return 'warning';

        case 'OUTOFSTOCK':
            return 'danger';

        default:
            return null;
    }
};

//Calculate number of days in a month
const daysInMonth = (month, year) => {
    return new Date(year, month, 0).getDate();
};
  
  //Generate dates for a selected month
const generateDatesForSelectedMonthTEST = () => {
    const selectedYear = dateMonthPicker.value.getFullYear();
    const selectedMonth = dateMonthPicker.value.getMonth() + 1;
    const days = daysInMonth(selectedMonth, selectedYear);
    //console.log(selectedMonth + ', ' + selectedYear);
  
    generatedDate.value = [];
  
    for (let day = 1; day <= days; day++) {
      //console.log(daysInMonth);
      //console.log(selectedMonth);
      const currentDate = new Date(selectedYear, selectedMonth - 1, day);
      if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
        generatedDate.value.push({
          date: currentDate,
        });
      }
    }
    generateTableDataForSelectedMonth();
};
  
  //Format the date
const formatDateTime = (date) => {
    const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
    return new Intl.DateTimeFormat('en-US', options).format(date);
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

.dropdownProject {
  position: relative;
  right: 17em;
  margin-bottom: 2em;
  top: 2em;
  text-align: center;
}

.dataTable {
    width: 50em;
    left: 10em;
}
</style>
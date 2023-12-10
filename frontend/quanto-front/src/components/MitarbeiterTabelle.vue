<template>
    <div class="container">
        <div>
        <div class="dropDown">
            <!-- Dropdown-Komponente mit v-model, options und optionLabel -->
            <Dropdown v-model="selectedProject" :options="projects" placeholder="Select a Project"
                 class="w-full md:w-14rem" @update:modelValue="test"/>
        </div>
    </div>
      <div class="monthPicker flex justify-content-center">
        <Calendar v-model="dateC" view="month" dateFormat="mm/yy" placeholder="Select a Date" @update:model-value="generateDatesForSelectedMonthTEST"></Calendar>
      </div>
      <div class="card p-fluid">
        <div style="max-height: 700px; overflow-y: auto; overflow-x: ;">
          <DataTable :value="generatedDate" editMode="cell" @cell-edit-complete="onCellEditComplete">
            <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" style="width: 25%">
              <template #body="{ data, field }">
                <span v-if="editingRow !== data">
                  {{ field === 'date' ? formatDateTime(data[field]) : field === 'pos' ? getStatusLabel(data[field]) : data[field] }}
                </span>
              </template>
              <template v-if="col.field !== 'date' && col.field !== 'pos'" #editor="{ data, field }">
                <InputText v-model="data[field]" ref="inputField" @input="onInput" />
              </template>
              <template v-if="col.field === 'pos'" #body="{ data, field }">
                <Dropdown class="position" v-model="data[field]" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Pos">
                  <template #option="slotProps">
                    <Tag :value="slotProps.option.value" :severity="getStatusLabel(slotProps.option.value)" />
                  </template>
                </Dropdown>
              </template>
            </Column>
          </DataTable>
        </div>
      </div>
    </div>
  </template>
  
  
  <script setup>
import { ref, onMounted, onUpdated } from 'vue';
import Calendar from 'primevue/calendar';
import axios from 'axios';
import InputText from 'primevue/inputtext';
import Dropdown from 'primevue/dropdown';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Tag from 'primevue/tag';

const selectedProject = ref();
const projects = [];
let chosenProject = "";

const dateC = ref(new Date());
const generatedDate = ref([]);
const editingRow = ref(null);

const columns = ref([
  { field: 'date', header: 'Date' },
  { field: 'hours_in_projects', header: 'Hours in Projects' },
  { field: 'hours_this_project', header: 'Hours this Project' },
  { field: 'pos', header: 'Pos' },
]);

const statuses = ref([
  { label: 'Status 1', value: 'status1' },
  { label: 'Status 2', value: 'status2' },
]);

const selectedYear = ref(null);
const selectedMonth = ref('December');
const years = ref([2022, 2023, 2024]);
const months = ref([
  { label: 'January', value: 1 },
  { label: 'February', value: 2 },
  { label: 'March', value: 3 },
  { label: 'April', value: 4 },
  { label: 'May', value: 5 },
  { label: 'June', value: 6 },
  { label: 'July', value: 7 },
  { label: 'August', value: 8 },
  { label: 'September', value: 9 },
  { label: 'Oktober', value: 10 },
  { label: 'November', value: 11 },
  { label: 'December', value: 12 },
]);


const onCellEditComplete = (event) => {
  let { data, newValue, field } = event;

  if (data[field] !== newValue) {
    switch (field) {
      case 'hours_in_projects':
      case 'hours_this_project':
        if (typeof newValue === 'string' && isPositiveInteger(newValue.trim())) {
          data[field] = newValue.trim();
        } else {
          event.preventDefault();
        }
        break;

      default:
        if (typeof newValue === 'string' && newValue.trim().length > 0) {
          data[field] = newValue.trim();
        } else {
          event.preventDefault();
        }
        break;
    }

    editingRow.value = null; // assuming editingRow is a ref
  }
};

const isPositiveInteger = (val) => {
  let str = String(val);
  str = str.trim();
  if (!str) {
    return false;
  }
  str = str.replace(/^0+/, '') || '0';
  const n = Math.floor(Number(str));
  return n !== Infinity && String(n) === str && n >= 0;
};

const onInput = () => {
  const inputFieldValue = this.$refs.inputField?.$props?.value;
  editingRow.value = inputFieldValue;
};

const getStatusLabel = (test) => {
  console.log(test);
};

const monthChanged = () => {
  const selectedMonth = dateC.value.getMonth() + 1;
  const selectedYear = dateC.value.getFullYear();
  console.log(dateC);
};

onUpdated(() => {
    chosenProject = selectedProject.value;
    console.log(chosenProject);
});

onMounted(() => {
  selectedYear.value = new Date().getFullYear();
  selectedMonth.value = new Date().getMonth() + 1;
  generateDatesForSelectedMonthTEST();
  getDataFromBackend();
  getProjectsFromBackend();
});

const getProjectsFromBackend = () => {
    const url = 'http://localhost:8000/getAllProjects/'
    axios.get(url)
    .then(response => {
      //console.log(response.data.data[0]);
      for(let i = 0; i < response.data.data.length; i++) {
        projects.push(response.data.data[i].name);
      }
    });
}

function test() {
    console.log("test");
}

const daysInMonth = (month, year) => {
  return new Date(year, month, 0).getDate();
};

const generateDatesForSelectedMonthTEST = () => {
  const selectedYear = dateC.value.getFullYear();
  const selectedMonth = dateC.value.getMonth() + 1;
  //const daysInMonth = new Date(selectedYear, selectedMonth + 1, 0).getDate();
  const daysInMonthTEST = daysInMonth(selectedMonth, selectedYear);
  console.log(selectedMonth + ', ' + selectedYear);

  generatedDate.value = [];

  for (let day = 1; day <= daysInMonthTEST; day++) {
    console.log(daysInMonthTEST);
    console.log(selectedMonth);
    const currentDate = new Date(selectedYear, selectedMonth - 1, day);
    if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
      generatedDate.value.push({
        date: currentDate,
      });
    }
  }

  getDataFromBackend();
};

const formatDateTime = (date) => {
  const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
  return new Intl.DateTimeFormat('en-US', options).format(date);
};

const getDataFromBackend = () => {
  const url = 'http://localhost:8000/getTableData/2';
  axios.get(url)
    .then(response => {
      console.log(response.data.data[0].employee);
      const startDate = response.data.data.start;
      const endDate = response.data.data.end;
      calculateHours(startDate, endDate);
    });
};

const calculateHours = (startDate, endDate) => {
  const startDateTime = new Date(startDate);
  const endDateTime = new Date(endDate);

  if (endDateTime <= startDateTime) {
    console.error('Enddatum sollte nach dem Startdatum liegen.');
    return;
  }

  const totalHours = (endDateTime - startDateTime) / (1000 * 60 * 60);
  const workdays = getWorkdays(startDateTime, endDateTime);
  const hoursPerDay = totalHours / workdays;

  generatedDate.value.forEach((day) => {
    day.hours = hoursPerDay;
    console.log(day.hours + ' StUNDEN');
  });
};

const getWorkdays = (startDate, endDate) => {
  let count = 0;
  let current = new Date(startDate);

  while (current <= endDate) {
    const dayOfWeek = current.getDay();

    if (dayOfWeek >= 1 && dayOfWeek <= 5) {
      count++;
    }

    current.setDate(current.getDate() + 1);
  }

  return count;
};

const handleYearChange = () => {
  getDataFromBackend();
};

const handleMonthChange = () => {
  getDataFromBackend();
};

</script>
  
  <style scoped>
  .container {
    position: relative;
  }
  
  .card {
    position: absolute;
    bottom: -45em;
    left: 6em;
    width: 50em;
  }
  
  .dropdowns {
    margin-bottom: 2em;
    left: -10em;
  }
  
  .position {
    z-index: 1000 !important;
    top: 0em;
    width: 7em;
    left: -15%;
  }
  
  .monthPicker {
    position: relative;
    border: 1px solid black;
    width: 10em;
    left: 10em;
    top: 4em;
  }

  .dropDown {
    position: relative;
    right: 17em;
    top: 2em;
    text-align: center;
}
  </style>
  
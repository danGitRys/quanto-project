<template>
    <div class="containerProjectMonth">
      <div class="dropdowns">
        <!-- Dropdown-Komponente mit v-model, options und optionLabel -->
        <div class="dropDown">
          <Dropdown
            v-model="selectedProject"
            :options="projects"
            placeholder="Select a Project"
            class="w-full md:w-14rem"
            style="width: 20em;"
          />
        </div>
      </div>
  
      <div class="monthPicker">
        <Calendar
          v-model="dateC"
          view="month"
          dateFormat="mm/yy"
          placeholder="Select a Date"
          @update:model-value="generateDatesForSelectedMonthTEST"
        ></Calendar>
      </div>
    </div>
    <div class="container">
      <div class="cards-container">
        <div v-for="(name, index) in names" :key="index" class="card-container">
          <div class="card p-fluid">
            <h1 class="names">{{ name }}</h1>
            <div class="scrollable-table">
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
                    <Dropdown
                      class="position"
                      v-model="data[field]"
                      :options="statuses"
                      optionLabel="label"
                      optionValue="value"
                      placeholder="Select a Pos"
                    >
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
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUpdated, watch } from 'vue';
  import Calendar from 'primevue/calendar';
  import axios, { formToJSON } from 'axios';
  import InputText from 'primevue/inputtext';
  import Dropdown from 'primevue/dropdown';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Tag from 'primevue/tag';
import { reactive } from 'vue';
  
  const selectedProject = ref();
  const projects = [];
  const allProjects = [];
  let chosenProject = '';
  let chosenProjectId = '';

//   const data = reactive([
//     {
//         date: [],
//         hours_in_projects: [],
//         hours_this_project: [],
//         pos: []
//     }
//   ])

  
  const names = ref([]);
  
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
    // { label: 'Status 2', value: 'status2' },
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
  
      editingRow.value = null;
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
    //console.log(dateC);
  };
  
  onUpdated(() => {

  });

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

  
  onMounted(() => {
    selectedYear.value = new Date().getFullYear();
    selectedMonth.value = new Date().getMonth() + 1;
    getProjectsFromBackend();
    console.log('HIER');
    generateDatesForSelectedMonthTEST();
  });
  
  const getProjectsFromBackend = () => {
    console.log('AUCH HIER');
    
    const url = 'http://localhost:8000/getAllProjects/';
    axios.get(url).then((response) => {
      for (let i = 0; i < response.data.data.length; i++) {
        projects.push(response.data.data[i].name);
        allProjects.push(response.data.data[i]);
        console.log('allProjects');
        console.log(allProjects);
      }
    });
  };

  const daysInMonth = (month, year) => {
    return new Date(year, month, 0).getDate();
  };
  
  const generateDatesForSelectedMonthTEST = () => {
    const selectedYear = dateC.value.getFullYear();
    const selectedMonth = dateC.value.getMonth() + 1;
    const daysInMonthTEST = daysInMonth(selectedMonth, selectedYear);
    //console.log(selectedMonth + ', ' + selectedYear);
  
    generatedDate.value = [];
  
    for (let day = 1; day <= daysInMonthTEST; day++) {
      //console.log(daysInMonthTEST);
      //console.log(selectedMonth);
      const currentDate = new Date(selectedYear, selectedMonth - 1, day);
      if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
        generatedDate.value.push({
          date: currentDate,
        });
      }
    }
  };
  
  const formatDateTime = (date) => {
    const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
    return new Intl.DateTimeFormat('en-US', options).format(date);
  };
  
  const getDataFromBackend = (id) => {
  // Empty the names List
  names.value = [];

  const url = `http://localhost:8000/getTableData/${id}`;
  axios.get(url).then((response) => {
    const dataLength = response.data.data.length
    const allForecasts = [];
    console.log('TESTOTOTOTOT');
    console.log(response.data);

    if (response.data && response.data.data) {
    for (let i = 0; i < response.data.data.length; i++) {
        if (response.data.data[i].projects) {
            for (let k = 0; k < response.data.data[i].projects.length; k++) {
                if (response.data.data[i].projects[k].positions) {
                    for (let z = 0; z < response.data.data[i].projects[k].positions.length; z++) {
                        console.log(response.data.data[i].projects[k].positions[z].forecast);
                        allForecasts.push(response.data.data[i].projects[k].positions[z].position)
                    }
                }
            }
        }
    }
}


allForecasts.forEach((elem) => {})



















    for (let i = 0; i < response.data.data.length; i++) {
      // Check whether the employee is in the project
      const projects = response.data.data[i].projects;
      const isInSelectedProject = projects.some(
        (project) => project.project.fk_project === id
      );

      if (isInSelectedProject) {
        names.value.push(response.data.data[i].employee.forename);

        for(let k = 0; k < response.data.data[i].projects.length; k++) {
            if(response.data.data[i].projects[k].project.fk_project == id) {
                // for(let z = 0; z < response.data.data[i].projects[k].position)
                // console.log('STATUS ' + id);
                // console.log(response.data.data[i]);
            }
        }
        // statuses.value.push(response.data.data[i].)

        console.log(names[i]);
        console.log("WIR SIND DRINNEN");
      }
    }
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
  </script>
  
  <style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-x: auto; /* Füge diese Eigenschaft hinzu */
  white-space: nowrap; /* Verschiebe white-space hierhin */
}

.containerProjectMonth {
    display: flex;
    flex-direction: column;
    align-items:center;;

}

.cards-container {
  display: inline-block;
  margin-left: 50em;
}

.card-container {
  display: inline-block;
  margin: 1em;
  width: 50em;
  overflow-x: auto;
}

.scrollable-table {
  max-height: 700px;
  overflow-y: auto;
  overflow-x: hidden;
}

.dropdowns {
  margin-bottom: 2em;
  left: -10em;
}

.position {
  top: 0em;
  width: 7em;
  left: -15%;
}

.monthPicker {
  position: relative;
  border: 1px solid black;
  right: 17em;
  text-align: center;
  top: 1em;
}

.dropDown {
  position: relative;
  right: 17em;
  top: 2em;
  text-align: center;
}

/* Add your other styles here */

</style>

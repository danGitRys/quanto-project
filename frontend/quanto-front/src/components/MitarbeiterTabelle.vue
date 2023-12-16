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
      <!-- Display employee names and editable data -->
      <div class="container">
        <div class="cards-container">
          <div v-for="(name, index) in names" :key="index" class="card-container">
            <div class="card p-fluid">
              <!-- Display employee name -->
              <h1 class="names">{{ name }}</h1>
  
              <!-- Display editable data in DataTable -->
              <div class="scrollable-table">
                <DataTable :value="generatedDate" editMode="cell" @cell-edit-complete="onCellEditComplete">
                  <!-- Loop through columns and display data -->
                  <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" style="width: 25%">
                    <template #body="{ data, field }">
                      <!-- Display data based on the field -->
                      <span v-if="editingRow !== data">
                        {{ field === 'date' ? formatDateTime(data[field]) : field === 'pos' ? getStatusLabel(data[field]) : data[field] }}
                      </span>
                    </template>
                    <!-- Provide editor for certain fields -->
                    <template v-if="col.field !== 'date' && col.field !== 'pos'" #editor="{ data, field }">
                      <InputText v-model="data[field]" ref="inputField" @input="onInput" />
                    </template>
                    <!-- Display dropdown for 'pos' field -->
                    <template v-if="col.field === 'pos'" #body="{ data, field }">
                      <Dropdown
                        class="position"
                        v-model="data[field]"
                        :options="statuses"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select a Pos"
                      >
                        <!-- <template #option="slotProps">
                          <Tag :value="slotProps.option.value" :severity="getStatusLabel(slotProps.option.value)" />
                        </template> -->
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
  // Import necessary modules
  import { ref, onMounted, onUpdated, watch } from 'vue';
  import Calendar from 'primevue/calendar';
  import axios from 'axios';
  import InputText from 'primevue/inputtext';
  import Dropdown from 'primevue/dropdown';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  
  const selectedProject = ref();
  const projects = [];
  const allProjects = [];
  let chosenProject = '';
  let chosenProjectId = '';
  
  const names = ref([]);
  
  const dateMonthPicker = ref(new Date());
  const generatedDate = ref([]);
  const editingRow = ref(null);
  
  //Define columns for datatable
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
  
  //Handle cell edit completion
  const onCellEditComplete = (event) => {
    
  };
  
  //Handle cell input
  const onInput = () => {
    
  };
  
  const getStatusLabel = (test) => {
    console.log(test);
  };
  
  //Component update
  onUpdated(() => {

  });

  //Watch for changes in selectedProject
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
    getProjectsFromBackend();
    console.log('HIER');
    generateDatesForSelectedMonthTEST();
  });
  
  //Fetch projects from backend
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
  };
  
  //Format the date
  const formatDateTime = (date) => {
    const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
    return new Intl.DateTimeFormat('en-US', options).format(date);
  };
  
  //Fetch data from backend with the projectid
  const getDataFromBackend = (id) => {
  // Empty the names List
  names.value = [];

  const url = `http://localhost:8000/getTableData/${id}`;
  axios.get(url).then((response) => {
    const allForecasts = []; //Test
    console.log('TEST');
    console.log(response.data);

    if (response.data && response.data.data) {
    for (let i = 0; i < response.data.data.length; i++) {
        // if (response.data.data[i].projects) {
        //     for (let k = 0; k < response.data.data[i].projects.length; k++) {
        //         if (response.data.data[i].projects[k].positions) {
        //             for (let z = 0; z < response.data.data[i].projects[k].positions.length; z++) {
        //                 console.log(response.data.data[i].projects[k].positions[z].forecast);
        //                 allForecasts.push(response.data.data[i].projects[k].positions[z].position)
        //             }
        //         }
        //     }
        // }
    }
}


//allForecasts.forEach((elem) => {})

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
  </script>
  
  <style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-x: auto;
  white-space: nowrap;
}

.containerProjectMonth {
    display: flex;
    flex-direction: column;
    align-items:center;

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

.dropdownProject {
  position: relative;
  right: 17em;
  margin-bottom: 2em;
  top: 2em;
  text-align: center;
}
</style>

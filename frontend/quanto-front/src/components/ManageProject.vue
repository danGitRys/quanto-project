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
      <div class="dates">
        <ul>
          <li v-for="(dateItem, index) in generatedDate" :key="index">
            {{ formatDateTime(dateItem.date) }}
          </li>
        </ul>
      </div>
    <div class="card">
      <div v-for="employee in employeesData" :key="employee.id">
        <h2>{{ employee.name }}</h2>
        <MitarbeiterTabelle
          :name="employee.name"
          :tableData="employee.times"
          :generatedDate="generatedDate"
          :selectedProject="selectedProject"
          :allProjects="allProjects"
        ></MitarbeiterTabelle>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue';
  import { startOfMonth, endOfMonth } from 'date-fns';
  import Calendar from 'primevue/calendar';
  import axios, { CancelToken} from 'axios';
  import Dropdown from 'primevue/dropdown';
  import MitarbeiterTabelle from './MitarbeiterTabelle.vue';
  
  const generatedDate = ref([]);
  const dateMonthPicker = ref(new Date());
  const selectedProject = ref();
  const projects = [];
  const allProjects = [];
  let chosenProject = '';
  let chosenProjectId = '';
  let cancelTokenSource = null;


  
  const empId = ref([]);
  const employeesData = ref([]);
  
  onMounted(() => {
    getProjectsFromBackend();
    generateDatesForSelectedMonthTEST();
  });
  
  const getProjectsFromBackend = async () => {
    const url = 'http://localhost:8000/getAllProjects/';
    await axios.get(url).then((response) => {
      const project = response.data.data;
      project.forEach(element => {
        projects.push(element.name);
        allProjects.push(element);
      });
    });
  };
  
  const getDataFromBackend = async () => {
  if (!chosenProjectId) {
    // No project selected, do nothing
    return;
  }

  // Cancel the previous request if it exists
  if (cancelTokenSource) {
    cancelTokenSource.cancel('New request initiated');
  }

  // Create a new cancel token source
  cancelTokenSource = axios.CancelToken.source();

  const url = 'http://localhost:8000/timeTableForecast';
  const url2 = `http://localhost:8000/getEmployeesToProjectId/${chosenProjectId}`;
  const url3Base = 'http://localhost:8000/getPositionsOfProjectOfEmployee';

  empId.value = [];
  employeesData.value = [];

  try {
    await axios.get(url2, { cancelToken: cancelTokenSource.token }).then(async (response) => {
      const empArray = response.data.data;

      empArray.forEach(async (element) => {
        empId.value.push(element.id);
        let positions = [];

        const url3 = `${url3Base}/${chosenProjectId}/${element.id}`;

        await axios.get(url3, { cancelToken: cancelTokenSource.token }).then(async (response) => {
          response.data.positions.forEach(pos => {
            positions.push({ name: `${pos.position_name}`, label: `${pos.position_id}`, value: `${pos.id}` });
          });
        });

        const employeeData = {
          id: element.id,
          name: element.forename,
          times: [],
        };

        const startOfMonthDate = startOfMonth(dateMonthPicker.value);
        const endOfMonthDate = endOfMonth(dateMonthPicker.value);
        const formattedStartDate = startOfMonthDate.toISOString().split('T')[0];
        const formattedEndDate = endOfMonthDate.toISOString().split('T')[0];

        const requestData = {
          start_date: formattedStartDate,
          end_date: formattedEndDate,
          project_id: chosenProjectId,
          employee_id: element.id,
        };

        await axios.post(url, requestData, { cancelToken: cancelTokenSource.token }).then((response) => {
          const bookings = response.data.data;

          generatedDate.value.forEach((dateItem, index) => {
            const tableEntry = bookings.find((element) => {
              const entryDate = new Date(element.date).toISOString().split('T')[0];
              return entryDate === dateItem.date.toISOString().split('T')[0];
            });

            const id = index + 1;
            const hours_this_project = tableEntry ? tableEntry.inProject : '';
            const hours_all_project = tableEntry ? tableEntry.outsideProject : '';
            const inProjectDetail = tableEntry ? tableEntry.inProjectDetail : '';

            employeeData.times[index] = {
              id: id,
              date: dateItem.date,
              hours_this_project: hours_this_project,
              hours_all_project: hours_all_project,
              inProjectDetail: inProjectDetail,
              pos: positions
            };
          });
        });

        employeesData.value.push(employeeData);
      });
    });
  } catch (error) {
    // Handle cancellation or other errors
    if (axios.isCancel(error)) {
      console.log('Request canceled:', error.message);
    } else {
      console.error('Error:', error.message);
    }
  }
};



  
  watch(selectedProject, (newProject) => {
    chosenProject = newProject;
  
    if (allProjects.length > 0) {
      for (let i = 0; i < allProjects.length; i++) {
        if (chosenProject == allProjects[i].name) {
          chosenProjectId = allProjects[i].id;
          getDataFromBackend();
        }
      }
    }
  });
  
  const generateTableDataForSelectedMonth = () => {
    employeesData.value.forEach(employee => {
      const employeeTableData = generatedDate.value.map((dateItem, index) => ({
        id: index + 1,
        date: dateItem.date,
        hours_all_project: '',
        hours_this_project: '',
        pos: '',
      }));
  
      employee.times = employeeTableData;
    });
  };
  
  const daysInMonth = (month, year) => {
    return new Date(year, month, 0).getDate();
  };
  
  const generateDatesForSelectedMonthTEST = () => {
    const selectedYear = dateMonthPicker.value.getFullYear();
    const selectedMonth = dateMonthPicker.value.getMonth() + 1;
    const days = daysInMonth(selectedMonth, selectedYear);
  
    generatedDate.value = [];
  
    for (let day = 1; day <= days; day++) {
      const currentDate = new Date(selectedYear, selectedMonth - 1, day);
      if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
        generatedDate.value.push({
          date: currentDate,
        });
      }
    }
    getDataFromBackend();
    generateTableDataForSelectedMonth();
  };
  
  const formatDateTime = (date) => {
    const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
    return new Intl.DateTimeFormat('en-US', options).format(date);
  };
  </script>
  
  <style scoped>

  /* .card {
  left: 10em;
  top: 15em;
  display: inline-flex;
  flex-direction: row;
  overflow-x: scroll;
} */

.dropdownProject {
right: 17em;
margin-bottom: 2em;
top: 2em;
text-align: center;
}

.dates {
    display: flex;
    margin-left: 100px;
    margin-top: 275px;
    z-index: 100;
    background-color: white;
}

ul{
    list-style: none;
    position:sticky;
}

:v-deep .v-application--wrap {
  min-height: fit-content;
}
  </style>
  
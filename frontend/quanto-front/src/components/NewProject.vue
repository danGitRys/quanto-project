<template>
  <div id="app">
    <div class="limiter">
      <ScrollPanel style="width: 100%; height:800px">
        <div class="container">
          <div class="input-container">
            <h3 class="input-label">Project Name:</h3>
            <InputText v-model="customerName" class="input-field small-input" type="text" />
          </div>
          <div class="input-container">
            <h3 class="input-label">Customer Name:</h3>
            <InputText v-model="customerName" class="input-field small-input" type="text" />
            
          </div>
          <div class="input-container">
            <h3 class="input-label">Project Start Date:</h3>
            <input v-model="projectStartDate" class="input-field small-input" type="date">
          </div>
          <div class="input-container-last">
            <h3 class="input-label">Project End Date:</h3>
            <input v-model="projectEndDate" class="input-field small-input" type="date">
          </div>
          
        </div>
        
        <div id="AddPM" class="container">
          <div class="input-container">
            
            <h3 class="input-label">Add Project Manager:</h3>
            <div class="employeeSelectionContainer">
              <div id="autocomplete">

                <v-autocomplete @click:append="addEmployee" v-model="projectManager" id="dropdownAddEmployee"
                label="Select Project Manager" :items="employeeList.name"
                variant="solo-filled">
                <option disabled value="">Select a Project Manager</option>
                <!-- Dynamische Werte kommen aus dem Store projectPosition.js -->
                <option v-for="(option, index) in employeeList.names" :value="index" :key="index">{{ option }}</option>
              </v-autocomplete>
              </div>
            </div>
          </div>
          <div  id="empButton">
            <v-btn @click="addEmployee" class="submitBtn" variant="outlined">
              Add Project Manager
            </v-btn>
          </div>            
        </div>

        <div id="AddEmployee" class="container">
          <div class="input-container">
            
            <h3 class="input-label">Add Employee:</h3>
            <div class="employeeSelectionContainer">
              <div id="autocomplete">

                <v-autocomplete @click:append="addEmployee" v-model="selectedEmployee" id="dropdownAddEmployee"
                label="Select Employee" :items="employeeList.name"
                variant="solo-filled">
                <option disabled value="">Select an Employee</option>
                <!-- Dynamische Werte kommen aus dem Store projectPosition.js -->
                <option v-for="(option, index) in employeeList.names" :value="index" :key="index">{{ option }}</option>
              </v-autocomplete>
              </div>
            </div>
          </div>
          <div  id="empButton">
            <v-btn @click="addEmployee" class="submitBtn" variant="outlined">
              Add Employee
            </v-btn>
          </div>            
        </div>
        <div id="Positions" class="container">
          <div class="input-container">
            
            <h3 class="input-label">Add Positions:</h3>
            <label for="pos">Position</label>
            <InputText id="pos" type="text" v-model="position" />
            <label for="posSwitch">Add Local/Remote</label>
            <InputSwitch id="posSwitch" v-model="checked" />
          </div>
        </div>
      </ScrollPanel>
    </div>

    <div id="table" class="container">
      <DataTable ref="selectedEmployees" :value="selectedEmployees" dataKey="empID" 
          :paginator="true" :rows="10"
          paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[5,10,25]"
          currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products">
          <template #header>
              <div class="flex flex-wrap gap-2 align-items-center justify-content-between">
                  <h4 class="m-0">Selected Employees</h4>
                  <span class="p-input-icon-left">
                      <i class="pi pi-search" />
                      <InputText placeholder="Search..." />
                  </span>
              </div>
          </template>
          <Column selectionMode="multiple" style="width: 3rem" :exportable="false"></Column>
          <Column field="empID" header="EmployeeID" sortable style="min-width:12rem"></Column>
          <Column field="name" header="Name" sortable style="min-width:12rem"></Column>
          <Column field="role" header="Role" sortable style="min-width:10rem"></Column>
          <Column :exportable="false" style="min-width:8rem">
              <template #body="slotProps">
                  <Button icon="pi pi-trash" outlined rounded severity="danger" @click="confirmDeleteEmployee(slotProps.data)" />
              </template>
          </Column>
      </DataTable>
    </div>

  </div>
  
</template>



<script>
import { employeeList } from '@/store/employeeList';
import InputText from 'primevue/inputtext';

export default {
    name: "newProject",
    components: {
        InputText,
    },
    data() {
        return {
          employeeList: [],
          selectedEmployee: '',
          selectedEmployees: [],
          checked: false,
        }
    },
    methods: {
      init() {
        this.employeeList = employeeList()
      },
    },
    created() {
        this.init()
    }
};
// 
// Add Employee Variables / Refs
// 

// class Employee {

// }

// const selectedEmployee = ref('');
// const selectedEmployees = ref([
//   {
//     empID: '123',
//     name: 'Peter',
//     role: 'PM',
//   },
// ]);

// var checked = ref(0);


// // 
// // Add Employee Functions
// // 
// function addEmployee() {
//     // Check if already in Array
//     if (selectedEmployees.value.indexOf(selectedEmployee.value) == -1) { // indexOf returns -1 if it is not in the Array
//         selectedEmployees.value.push(selectedEmployee.value);
//         return 0;
//     }
//     alert(selectedEmployee.value + " is already in List!")
// }

// function deleteEmployee(employee) {
//     console.log(employee)
//     var index = selectedEmployeesList.value.indexOf(employee)
//     selectedEmployeesList.value.splice(index, 1); // Remove the position at the specified index
// }

// function submitEmployees() {
//     // if an Employee is already working on the Project, give feedback
// }

// function confirmDeleteEmployee(emp) {

// }





// var customerName = ref("")
// var projectManager = ref("")
// var projectStartDate = ref("")
// var projectEndDate = ref("")

// function createProject() {
//   console.log(customerName.value)
//   console.log(projectManager.value)
//   console.log(projectStartDate.value)
//   console.log(projectEndDate.value)
// }


</script>


<style scoped>
/* Stil für kleinere Input-Felder */
.app {
  justify-content: center;
  display: flex;
  margin-left: 55px;
  height: 100%;
}
.small-input {
  width: 10px;
  /* Ändern Sie die Breite nach Bedarf */
  padding: 5px;
  /* Ändern Sie das Padding nach Bedarf */
}

#empButton {
  margin: 10px;
  align-items: right;
}
.limiter {
  width:100%;
  margin: 15px;
  height: 100%;
}

.container {
  background-color: lightgray;
  border-radius: 10px;
  padding: 20px;
  margin: 30px;
}

#table {
  min-width: 800px;
  margin: 45px;
}

.input-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid black;
  padding: 10px 0;
}
.input-container-last {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
}

.input-label {
  width: 200px;
  text-align: left;
  margin-right: 20px;
}

.input-field {
  background-color: ghostwhite;
  outline: 1px solid black;
  border-radius: 5px;
  flex: 1;
  max-width: 300px;
}

.employee-dropdown {
  background-color: ghostwhite;
  outline: 1px solid black;
  border-radius: 5px;
  flex: 1;
  max-width: 300px;
}

.plus-button {
  background-color: lightgray;
  border: 1px solid black;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.create-button {
  background-color: orange;
  /* Blaue Hintergrundfarbe */
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  margin-top: 10px;
  font-size: 18px;
  transition: background-color 0.3s;
  display: block;
  /* Ändern Sie die Anzeige auf "block" */
  margin: 10px auto;
  /* Auto-Margin horizontal zentriert den Button */
}

.create-button:hover {
  background-color: #0056b3;
  /* Farbänderung bei Hover */
}

.employeeSelectionContainer {
  width:100%;
}
#autocomplete {
  margin-top: 22px;
}
</style>
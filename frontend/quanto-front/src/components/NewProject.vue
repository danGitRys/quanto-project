<template>
  <div id="app">
    <div class="limiter">

      <div class="container">
        <div class="input-container">
          <h3 class="input-label">Customer Name:</h3>
          <input v-model="customerName" class="input-field small-input" type="text">
        </div>
        <div class="input-container">
          <h3 class="input-label">Project Manager:</h3>
          <input v-model="projectManager" class="input-field small-input" type="text">
          
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
      
      <div id="AddEmployee" class="container">
        <div class="input-container">
          
          <h3 class="input-label">Add Employee:</h3>
          <div class="employeeSelectionContainer">
            <div id="autocomplete">

              <v-autocomplete @click:append="addEmployee" v-model="selectedEmployee" id="dropdownAddEmployee"
              label="Select Employee" :items="employeeList().name"
              variant="solo-filled">
              <option disabled value="">Select an Employee</option>
              <!-- Dynamische Werte kommen aus dem Store projectPosition.js -->
              <option v-for="(option, index) in employeeList().names" :value="index" :key="index">{{ option }}</option>
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
    </div>
    <div id="table" class="container">
      <v-table fixed-header="true" data:positions>
        <thead>
          <tr>
            <th class="text-left">
              Employee
            </th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="emp in selectedEmployeesList" :key="emp">
            <td>{{ emp }}</td>
            
            <td>
              <v-dialog v-model="dialogVisible" ref="deleteDialog">
                      <template v-slot:activator="{ props }">
                          <div class="buttonContainer">
                              <v-btn v-bind="props" class="deleteBtn" variant="outlined">
                                  Delete
                              </v-btn>
                          </div>
                      </template>

                      <template v-slot:default="{ isActive }">
                          <v-card title="Are you sure?">
                              <v-card-text>
                                  Are you sure you want to delete {{ emp }} from the selected Employees?
                              </v-card-text>

                              <v-card-actions>
                                  <v-spacer></v-spacer>

                                  <v-btn text="Cancel" @click="isActive.value = false"></v-btn>
                                  <v-btn text="Confirm" @click="deleteEmployee(emp)">
                                  </v-btn>
                              </v-card-actions>
                          </v-card>
                      </template>
                  </v-dialog>
              </td>
          </tr>
        </tbody>
      </v-table>
    </div>

  </div>
  
</template>

<style scoped>
/* Stil für kleinere Input-Felder */
#app {
  justify-content: center;
  display: flex;
  margin-left: 55px;
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
}

.container {
  background-color: lightgray;
  border-radius: 10px;
  padding: 20px;
  margin: 30px;
}

#table {
  min-width: 500px;
  margin: 45px;
}
.v-table {
  height:100%
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

<script setup>
import { employeeList } from '@/store/employeeList'


// 
// Add Employee Variables / Refs
// 
const selectedEmployee = ref('');
const selectedEmployeesList = ref([]);

// 
// Add Employee Functions
// 
function addEmployee() {
    // Check if already in Array
    if (selectedEmployeesList.value.indexOf(selectedEmployee.value) == -1) { // indexOf returns -1 if it is not in the Array
        selectedEmployeesList.value.push(selectedEmployee.value);
        return 0;
    }
    alert(selectedEmployee.value + " is already in List!")
}

function deleteEmployee(employee) {
    console.log(employee)
    var index = selectedEmployeesList.value.indexOf(employee)
    selectedEmployeesList.value.splice(index, 1); // Remove the position at the specified index
}

function submitEmployees() {
    // if an Employee is already working on the Project, give feedback
}



import { ref } from 'vue';

const customerName = ref("")
const projectManager = ref("")
const projectStartDate = ref("")
const projectEndDate = ref("")

function createProject() {
  console.log(customerName.value)
  console.log(projectManager.value)
  console.log(projectStartDate.value)
  console.log(projectEndDate.value)
}


</script>

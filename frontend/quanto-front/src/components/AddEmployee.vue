<template>
<div class="mainContainer">
    <div class="container">
        <label>Add Employee</label>
        <div class="employeeSelectionContainer">

            <!-- Maybe Searchable?-->
            <v-autocomplete @click:append="addEmployee" v-model="selectedEmployee" id="dropdownAddEmployee" label="Select Employee" :items="employeeList().name">
                <option disabled value="">Select an Employee</option>
                <!-- Dynamische Werte kommen aus dem Store projectPosition.js -->
                <option v-for="(option,index) in employeeList().names" :value="index" :key="index">{{ option }}</option>
            </v-autocomplete>
            <v-btn @click="addEmployee" class="submitBtn" variant="outlined">
            Add Employee
        </v-btn>
        </div>
        <div class="buttonContainer">
        <v-btn @click="submitEmployees" class="submitBtn" variant="outlined">
            Submit
        </v-btn>
        </div>
        <v-table fixed-header="true" height="600px" data:positions>
            <thead>
                <tr>
                    <th class="text-left">
                    Employee
                    </th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="emp in selectedEmployeesList"
                    :key="emp"
                >
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

                                    <v-btn
                                    text="Cancel"
                                    @click="isActive.value = false"
                                    ></v-btn>
                                    <v-btn
                                        text="Confirm"
                                        @click="deleteEmployee(emp)"
                                    >
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

    
    <div class="container">
        <label>Add Position</label>
        <div id="positionsContainer">
            <label>Enter Position: </label>
            <select v-model="selectedPosition" id="dropdownProjectPosition">
                <option disabled value="">Select a Project Positon</option>
                <!-- Dynamische Werte kommen aus dem Store projectPosition.js -->
                <option v-for="(option,index) in optionsDataPositions" :value="index" :key="index">{{ option }}</option>
            </select>
        </div>
        
        <div id="dailyRatesContainer">
            <label>Enter Daily Rate: </label>
            <input type="number" name="dailyRateInput" placeholder="Daily Rate for the Position" v-model="rate">
        </div>
        <div id="numberOfPosContainer">
            <label>Enter Number of Positions </label>
            <input type="number" name="numberOfPos" placeholder="1" v-model="numberOfPositions">
        </div> 

        <div class="buttonContainer">
            <v-btn @click="addPosition" class="submitBtn" variant="outlined">
            Add Position
            </v-btn>
        </div>
        <div id="budgetContainer">
            <label>Budget: {{ budget }} €</label>
        </div>
        <div class="buttonContainer">
        <v-btn @click="submitPositions" class="submitBtn" variant="outlined">
            Submit
        </v-btn>
        </div>
        <v-table data:positions>
            <thead>
                <tr>
                    <th class="text-left">
                    Position
                    </th>
                    <th class="text-left">
                    Daily Rate
                    </th>
                    <th class="text-left">
                    Amount
                    </th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="pos in positions"
                    :key="pos.name"
                >
                    <td>{{ pos.name }}</td>
                    <td>{{ pos.rate }}</td>
                    <td>{{ pos.amount }}</td>
                    <td>
                        <v-dialog>
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
                                    Are you sure you want to delete {{ pos.amount }} of {{ pos.name }} with a Daily Rate of {{ pos.rate }}?
                                    Deleted Positions are lost forever.
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>

                                    <v-btn
                                    text="Cancel"
                                    @click="isActive.value = false"
                                    ></v-btn>
                                    <v-btn
                                        text="Confirm"
                                        @click="deletePosition(pos)"
                                    >
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

<script setup>
import { ref} from 'vue';
import { projectPosition } from '@/store/projectPostion'
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

// 
// Add Position Variables / Refs
// 
class Position {
    name = "";
    rate = 0;
    amount = 0;
    constructor(name, rate, amount) {
        this.name = name;
        this.rate = rate;
        this.amount = amount;
    }
}
const projectPos = projectPosition();
const optionsDataPositions = projectPos.names;
const selectedPosition = ref('');

const rate = ref('');
let numberOfPositions = ref('');

const dialogVisible = ref(false);
const positions = ref([]);
let budget = ref(0);

// 
// Add Position Functions
// 
function calcBudget() {
    budget.value = 0;
    for (let i = 0; i < positions.value.length;i++) {
        budget.value += positions.value[i].rate * positions.value[i].amount;
    }
    return budget.value;
}
function addPosition() {
    // Index in Position Name Array
    let amount = 1;
    if (numberOfPositions.value != '') {
        amount = numberOfPositions.value;
    }
    let posIndex = selectedPosition.value;
    if (optionsDataPositions[posIndex]== undefined || rate.value == "") {
        alert("Please enter Position AND Daily Rate");
        return 1;
    }
    const newPos = new Position(optionsDataPositions[posIndex],rate.value, amount);
    positions.value.push(newPos);
    calcBudget(); // Update the budget
    rate.value = '';
    numberOfPositions.value = '';
    console.log(positions.value)
}

function deletePosition(pos) {
    console.log(positions.value)
    console.log(pos)
    var index = positions.value.indexOf(pos)
    positions.value.splice(index, 1); // Remove the position at the specified index
    calcBudget();  // Update the budget
    
    // Close the dialog
    const deleteDialog = this.$refs.deleteDialog; // Assuming this is inside a component
    if (deleteDialog) {
        deleteDialog.isActive = false;
    }
}


function submitPositions() {

}


</script>

<style scoped>
.submitBtn{
    border: 2px solid #304C5D;
    background-color: #EF7C00;
    color: white;
    font-size: 22px;
    padding: 20px;
    display: flex;
    margin: 10px;
}
.mainContainer{
    display: flex;
    justify-content: center;
}
.buttonContainer{
    margin: 10px;
    width: 100%;
    display: flex;
    justify-content:flex-end;
}

.container{
    padding: 40px;
    background: white;
    border: 3px solid black;
    border-radius: 5%;
    margin: 20px;
    display: inline-block;
    flex-direction: column;
    justify-content: left;
    min-width: 20%;
    max-width: 50%;
}

label{
     font-size: 32px;
}
input, select{
  
    float: right;
    outline: 2px solid #EF7C00;
    font-size:32px ;
}

div{
    margin-top:50px ;
}

</style>
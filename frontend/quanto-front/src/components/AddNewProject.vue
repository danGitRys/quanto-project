<template>
  <div id="app" class="d-flex justify-center">
    <div class="container">
      <div class="input-container">
        <h3 class="input-label">Customer Name:</h3>
        <input v-model = "customerName" class="input-field small-input" type="text">
      </div>
      <div class="input-container">
        <h3 class="input-label">Project Manager:</h3>
        <input v-model="projectManager" class="input-field small-input" type="text">

      </div>
      <div class="input-container">
        <h3 class="input-label">Project Start Date:</h3>
        <input v-model="projectStartDate" class="input-field small-input" type="date">
      </div>
      <div class="input-container">
        <h3 class="input-label">Project End Date:</h3>
        <input v-model="projectEndDate" class="input-field small-input" type="date">
      </div>

      <div class="input-container">
        <h3 class="input-label">Add Employee:</h3>
        <button class="plus-button" @click="addEmployee">+</button>
      </div>

      <div class="input-container">
        <h3 class="input-label">Selected Employees:</h3>
        <select v-model="selectedEmployees" class="employee-dropdown" multiple>
          <option value="employee2">Employee 1</option>
          <option value="employee2">Employee 2</option>
          <option value="employee1">Employee 3</option>
          <option value="employee2">Employee 4</option>
          <option value="employee1">Employee 5</option>
          <option value="employee2">Employee 6</option>
          <option value="employee1">Employee 7</option>
          <option value="employee2">Employee 8</option>
          <option value="employee1">Employee 9</option>
          <option value="employee2">Employee 10</option>
          <option value="employee1">Employee 11</option>
          <option value="employee2">Employee 12</option>
          <option value="employee1">Employee 13</option>
          <option value="employee2">Employee 14</option>
          <option value="employee1">Employee 15</option>
          <option value="employee2">Employee 16</option>
          <!-- Weitere Optionen hier -->
        </select>
      </div>

      <button class="create-button" @click="createProject">Create</button>
    </div>
  </div>
</template>

<style scoped>
/* Stil für kleinere Input-Felder */
.small-input {
  width: 10px; /* Ändern Sie die Breite nach Bedarf */
  padding: 5px; /* Ändern Sie das Padding nach Bedarf */
}
.container {
  width: 90vw;
  background-color: lightgray;
  border-radius: 10px;
  padding: 20px;
  margin-top: 100px;
  margin-bottom: 100px;
  margin-left: 100px;
  margin-right: 100px;
}

.input-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid black;
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
  background-color:orange; /* Blaue Hintergrundfarbe */
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  margin-top: 10px;
  font-size: 18px;
  transition: background-color 0.3s;
  display: block; /* Ändern Sie die Anzeige auf "block" */
  margin: 10px auto; /* Auto-Margin horizontal zentriert den Button */
}

.create-button:hover {
  background-color: #0056b3; /* Farbänderung bei Hover */
}
</style>

<script setup>

import { ref } from 'vue';

const customerName = ref ("")
const projectManager = ref("")
const projectStartDate = ref("")
const projectEndDate = ref("")

function createProject (){
  console.log (customerName.value)
  console.log (projectManager.value)
  console.log (projectStartDate.value)
  console.log (projectEndDate.value)
}


</script>

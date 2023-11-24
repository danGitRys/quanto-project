// fetch oder axios anfrage
// füllen von ProjectName and Position mit dynamisch Daten vom Backend

<template>
  <div class="allContainer">
    <div class="mainContainer">
      <div class="container">
        <div class="pickDateContainer">
          <label for="datePicker"> Pick Date: </label>
          <input v-model="date" id="datePicker" type="date">
        </div>

        <div class="startTimeContainer">
          <label for="startTimePicker"> Start Time: </label>
          <input v-model="startTime" id="startTimePicker" type="time">
        </div>

        <div class="breakTimeContainer">
          <label for="breakTimePicker"> Break Time: </label>
          <input v-model="breakTime" id="breakTimePicker" type="time">
        </div>

        <div class="endTimeContainer">
          <label for="endTimePicker"> End Time: </label>
          <input v-model="endTime" id="endTimePicker" type="time">
        </div>

        <div class="projectNameContainer">
          <label for="dropdownProjectName">Project Name:</label>
          <select v-model="selectedProjectName" name="test" id="dropdownProjectName">
            <option disabled value="">Select a Project Name</option>
            <!-- Dynamische Werte kommen aus dem Store app.js -->
            <option v-for="(option, index) in optionsData" :value="index" :key="index">{{ option }}</option>
          </select>

        </div>

        <div class="projectPositionContainer">
          <label for="dropdownProjectPosition">Project Position:</label>
          <select v-model="selectedProjectPosition" id="dropdownProjectPosition">
            <option disabled value="">Select a Project Positon</option>
            <!-- Dynamische Werte kommen aus dem Store projectPosition.js -->
            <option v-for="(option, index) in optionsData2" :value="index" :key="index">{{ option }}</option>
          </select>
        </div>
        <div class="buttonContainer">
          <v-btn @click="sendDatatoBackend" id="submitBtn" variant="outlined">
            Submit
          </v-btn>
        </div>
      </div>

    </div>





  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAppStore } from '@/store/app';
import { projectPosition } from '@/store/projectPostion';
import axios from "axios"

const selectedProjectName = ref('');
const selectedProjectPosition = ref('');

const date = ref('');
const startTime = ref('');
const breakTime = ref('');
const endTime = ref('');
const appStore = useAppStore();
const projectPos = projectPosition();
// Daten aus dem Store zum Dynamischen hinzufügen der Dropdowns
const optionsData = appStore.names;
const optionsData2 = projectPos.names;

function sendDatatoBackend() {
  // Abrufen des Inhaltes des DropDown Menüs da V-Model nicht auf Option Tags möglich ist  

  const indexValueProjectName = selectedProjectName.value;
  const selectedProjectNameValue = optionsData[indexValueProjectName];
  console.log(selectedProjectNameValue);

  const indexValueProjectPosition = selectedProjectPosition.value;
  const selectedProjectPositionValue = optionsData2[indexValueProjectPosition];
  console.log(selectedProjectPositionValue);
  // Testen ob alle Daten in Variablen gespeichert wurden
  console.log(date.value);
  console.log(startTime.value);
  console.log(breakTime.value);
  console.log(endTime.value);

// const endT = endTime.value
// console.log(endT)


const data = {
 date: date.value,
 startTime: startTime.value,
 breakTime: breakTime.value,
 endTime: endTime.value,
}
console.log(data)


  // if (date.value == '' || startTime.value == '' || breakTime.value == '' || endTime.value == '' || selectedProjectNameValue == undefined || selectedProjectPositionValue == undefined) {
  //   alert("Please fill out all fields");
  // }
  // else {
    const url = "http://localhost:8000/timeRegistration"
    axios.post(url, data)
      .then(response => {
        // Erfolgreiche Antwort vom Server
        console.log(response.data);
      })
      .catch(error => {
        // Fehler bei der Anfrage
        console.error(error);
      });
    // Daten an Backend senden
  
    

  //   alert("Data has been submitted");
  // }


}
</script>

<style scoped>
#datePicker,
#startTimePicker,
#breakTimePicker,
#endTimePicker,
#dropdownProjectName,
#dropdownProjectPosition {
  font-size: 32px;

}

#submitBtn {
  border: 2px solid #304C5D;
  background-color: #EF7C00;
  color: white;
  font-size: 32px;
  padding: 22px;
  display: flex;
}

.mainContainer {

  display: flex;
  justify-content: center;
}

.buttonContainer {
  margin-top: 40px;
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.container {
  padding: 40px;
  background: white;
  border: 3px solid black;
  border-radius: 5%;
  margin-top: -15px;
  display: inline-block;
  flex-direction: column;
  justify-content: left;
  width: 45%;
}

label {
  font-size: 32px;
}

input,
select {

  float: right;
  outline: 2px solid #EF7C00;
}

div {
  margin-top: 50px;
}</style>
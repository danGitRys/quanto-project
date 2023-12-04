// füllen von ProjectName and Position mit dynamisch Daten vom Backend
<template>
  <div class="allContainer">
    <div class="mainContainer">
      <div class="container">

  <div class="projectNameContainer">
      
            <label for="dropdownProjectName">Project Name:</label>
            <select v-model="selectedProjectName" @change="loadPositions" id="dropdownProjectName">
              <option disabled value="">Select a Project</option>
              <option v-for="(project, index) in projectArray" :value="project" :key="index">{{ project }}</option>
            </select>
           
          </div>

          <div class="projectPositionContainer">
            <label for="dropdownProjectPosition">Project Position:</label>
            <select v-model="selectedProjectPosition" @change="selectedPostion" id="dropdownProjectPosition">
              <option disabled value="">Select a Project Positon</option>
              <!-- Dynamische Werte kommen aus dem Store projectPosition.js -->
              //<option v-for="(position, index) in positionArray" :value="position" :key="index">{{ position }}</option>
            </select>
          </div>


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
          <input v-model="breakTime" id="breakTimePicker" placeholder="Minutes">
        </div>

        <div class="endTimeContainer">
          <label for="endTimePicker"> End Time: </label>
          <input v-model="endTime" id="endTimePicker" type="time">
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
import { onBeforeMount, reactive, ref} from 'vue';
//import { useAppStore } from '@/store/app';
//import { projectPosition } from '@/store/projectPostion';
import axios from "axios"

let projectArray = ref([]);
let positionArray = ref([]);

//const appStore = useAppStore();
const startTime = ref('');
const breakTime = ref('');
const endTime = ref('');

const selectedProjectName = ref('')
const selectedProjectPosition = ref('');

// Initialisierung mit dem aktuellen Datum im gewünschten Format
const date = ref(getFormattedDate());

let project = {
  name: [],
  id: [],
}

let position = {
  name:[],
  id:[],
}

let posID = "";
function selectedPostion(){
  console.log("AUFRUGF")
  console.log(selectedProjectPosition.value)
  position.name.forEach((element, index) => {
    if(element === selectedProjectPosition.value){
    posID = position.id[index];
    
    }

  })

}

async function loadPositions() {
  positionArray.value = [];
  project.name.forEach((element, index) => {
    if (element === selectedProjectName.value){
      console.log("Gefunden", project.id[index])
      const fk_project = project.id[index]
      getPositionsFromBackend(fk_project)

    }
    // Hier sollten Sie Ihren Code platzieren, der für jedes Element in project.name ausgeführt werden soll.
  });
}




onBeforeMount(() => {
getProjectsFromBackend();

})

// EMPLPOYEE AKTUELL NOCH HARDGECODET 

let employee_id = 8;

async function getProjectsFromBackend() {
  const url = `http://localhost:8000/testInnerJoin/${employee_id}`;
 
  const response = await axios.get(url);
  let respArray = response.data.projects;
  console.log(respArray);
  respArray.forEach((element,index) => {
    projectArray.value[index] = element.name;
  });

  for (let i = 0; i < respArray.length; i++){
    project.name[i] = respArray[i].name;
    project.id[i] = respArray[i].id;
    console.log("Springst du hier rein")
    console.log("HEY " + project.name)
  }
  
  console.log(response.data.projects.name)
  console.log(response.data.projects)
  

  // .project ergänzen wenn mehrere Projekte 

 // projectArray.value = response.data.projects;

  console.log("wirst du aufgerufen");
}

// HIER MUSS NOCH DIE EMPPYEE ID MIT ÜBERGEBEN WERDEN IN DER URL 

async function getPositionsFromBackend(fk_project){
  
  const url = `http://localhost:8000/getPositionsOfProjectOfEmployee/${fk_project}`
  console.log(url)
  const response = await axios.get(url)
  console.log(response);

  console.log(response.data.positions[0].position_id)

  let resPositionArray = response.data.positions;
  resPositionArray.forEach((element,index) =>{
    positionArray.value[index] = element.position_id;

    position.name[index] = element.position_id;
    position.id[index] = element.id;
  })




  console.log(response.data.data)
  console.log("Postion Backend Aufrug");

}





function getFormattedDate() {
  const today = new Date();
  const day = today.getDate();
  // +1 da Monate nullbasiert sind
  const month = today.getMonth() + 1; 
  const year = today.getFullYear();

  // Führende Nullen hinzufügen, wenn nötig
  const formattedDay = day < 10 ? `0${day}` : day;
  const formattedMonth = month < 10 ? `0${month}` : month;

  return `${year}-${formattedMonth}-${formattedDay}`;
}







function sendDatatoBackend() {
   //const selectedProjectIndex = selectedProjectName.value;
  // const selectedProject = projectArray.value[selectedProjectIndex]
   //console.log(selectedProjectIndex)
   //console.log(selectedProject)
   console.log("Hello World")


   // Datum werden in richtiges Format umgewandelt für die Datenbank
   const startDate = `${date.value}` + " " + `${startTime.value+":00"}`
   const endDate = `${date.value}` + " " + `${endTime.value + ":00"}`

const data = {
  "fk_employee": 2,
  "fk_position": posID,
  "start": startDate,
  "end": endDate,
  "pause": breakTime.value
  //"time": "15"
}
console.log(data)


   if (date.value == '' || startTime.value == '' || breakTime.value == '' || endTime.value == '' || selectedProjectName.value == undefined || selectedProjectPosition.value == undefined) {
     alert("Please fill out all fields");
   }
   else {
    const url = "http://localhost:8000/createBooking"
    axios.post(url, data)
      .then(response => {
        // Erfolgreiche Antwort vom Server
        console.log(response.data);
        // true
        if (response.data['success']) {
        alert("Booking sucessfull")
      }

      })
      .catch(error => {
        // Fehler bei der Anfrage
        console.error(error);
      });
   }

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
#breakTimePicker{
  width: 130px;
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
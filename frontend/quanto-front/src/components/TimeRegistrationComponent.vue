<template>
  <div class="allContainer">
    <div class="mainContainer">
      <div class="container">

<!--Project DropDown Menu-->
  <div class="projectNameContainer">
            <label for="dropdownProjectName">Project Name:</label>
            <!--loadPosition get called every Time a entry of the DropDown get picked-->
            <select v-model="selectedProjectName" @change="loadPositions" id="dropdownProjectName">
              <option disabled value="">Select a Project</option>
              <!--Project DropDown Array get Filled Dynamically with Data from the Backend-->
              <option v-for="(project, index) in projectArray" :value="project" :key="index">{{ project }}</option>
            </select>
          </div>


          <!--Position DropDown Menu-->
          <div class="projectPositionContainer">
            <label for="dropdownProjectPosition">Project Position:</label>
            <select v-model="selectedProjectPosition" @change="selectedPostion" id="dropdownProjectPosition">
              <option disabled value="">Select a Project Positon</option>
               <!--Postion DropDown Array get Filled Dynamically with Data from the Backend-->
             <option v-for="(position, index) in positionArray" :value="position" :key="index">{{ position }}</option>
            </select>
          </div>

          <!--DatePicker-->
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
      <!--If the Button get clicked the data will get sended to the backend-->
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
import { onBeforeMount, ref} from 'vue';
import axios from "axios"

// 2 arrays that receive values from the backend and are dynamically filled
let projectArray = ref([]);
let positionArray = ref([]);

const startTime = ref('');
const breakTime = ref('');
const endTime = ref('');
const selectedProjectName = ref('')
const selectedProjectPosition = ref('');
// calls function to get the current date
const date = ref(getFormattedDate());

let project = {
  name: [],
  id: [],
}

let position = {
  name:[],
  id:[],
}
// global variable used in the data object later
let posID = "";

// the function loops to my postion Object if it matched the selected Postion I get the posID of the selected Position
// which I will need for the Backend call
function selectedPostion(){
  position.name.forEach((element, index) => {
    if(element === selectedProjectPosition.value){
    posID = position.id[index];
    }
  })
}
// the function loops to my project Object if it matched the selected Project I get the fk (forgein key) of the Project 
// which I need for the backend call to get all Positions for the selected Project

async function loadPositions() {
  positionArray.value = [];
  project.name.forEach((element, index) => {
    if (element === selectedProjectName.value){
      const fk_project = project.id[index]
      getPositionsFromBackend(fk_project)
    }
  });
}
// get called before the Page is loaded I get all projects the employee is involved
onBeforeMount(() => {
getProjectsFromBackend();
})

// EMPLPOYEE AKTUELL NOCH HARDGECODET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

let employee_id = 8;
//function that get all Projects from the Backend from a specific employee
async function getProjectsFromBackend() {
  // employee_id give back all employees for this employee
  const url = `http://localhost:8000/testInnerJoin/${employee_id}`;
  // request send to backend
  const response = await axios.get(url);
  // save the response in the Array
  let respArray = response.data.projects;
  // fill the projectArray with the data of the backend
  respArray.forEach((element,index) => {
    projectArray.value[index] = element.name;
  });
  // fill the data of the backend into the project object 
  for (let i = 0; i < respArray.length; i++){
    project.name[i] = respArray[i].name;
    project.id[i] = respArray[i].id;
  }
}

// HIER MUSS NOCH DIE EMPPYEE ID MIT ÜBERGEBEN WERDEN IN DER URL 

async function getPositionsFromBackend(fk_project){
  const url = `http://localhost:8000/getPositionsOfProjectOfEmployee/${fk_project}`
  const response = await axios.get(url)
  let resPositionArray = response.data.positions;
  resPositionArray.forEach((element,index) =>{
    positionArray.value[index] = element.position_id;
    position.name[index] = element.position_id;
    position.id[index] = element.id;
  })
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
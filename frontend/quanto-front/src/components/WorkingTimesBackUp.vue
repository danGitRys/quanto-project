<template>
    <div>
        <div class="card flex justify-content-center">
            <Dropdown v-model="selectedProject" :options="projectNames" @change="fetchEmployeesOfProject" optionLabel="name"
                placeholder="Project Name" class="w-full md:w-14rem" />
        </div>

        <div class="card flex justify-content-center">
            <Dropdown v-model="selectedName" :options="employeeNames" @change="fetchDataOfEmployee" optionLabel="name"
                placeholder="Employees" class="w-full md:w-14rem" />
        </div>

        <div class="card">
            <DataTable :value="products" tableStyle="min-width: 50rem">
                <Column field="code" header="Projekt"></Column>
                <Column field="id" header="ID"></Column>
                <Column field="monday" :header="dateHeader.monday">
                    <template #body="{ row }">
                        <DataTable :value="innerTable">
                            <Column v-for="col in columns" :key="col.field" :field="col.field" :header="col.header"
                                :style="{ width: col.width }">
                                <template #body="{ data, field }">



                                    <div v-if="field === 'plannedTime'">
                                        <InputText v-model="data[field]" />
                                    </div>
                                    <div v-else-if="field === 'workingTimes'">
                                        <InputText v-model="data[field]" />
                                    </div>
                                    <div v-else-if="field === 'breakTime'">
                                        <InputText v-model="data[field]" />
                                    </div>
                                    <div v-else-if="field === 'sumTime'">
                                        <InputText v-model="data[field]" />
                                    </div>



                                </template>
                            </Column>
                        </DataTable>
                    </template>
                </Column>

                <!-- Continue with the rest of your columns -->
                <Column field="tuesday" :header="dateHeader.tuesday">
                    <template #body="{ row }">
                        <DataTable :value="innerTable">
                            <Column v-for="col in columns" :key="col.field" :field="col.field" :header="col.header"
                                :style="{ width: col.width }">
                                <template #body="{ data, field }">


                                    <div v-if="field === 'plannedTime'">
                                        <InputText v-model="data[field]" />
                                    </div>
                                    <div v-else-if="field === 'workingTimes'">
                                        <InputText v-model="data[field]" />
                                    </div>
                                    <div v-else-if="field === 'breakTime'">
                                        <InputText v-model="data[field]" />
                                    </div>
                                    <div v-else-if="field === 'sumTime'">
                                        <InputText v-model="data[field]" />
                                    </div>



                                </template>
                            </Column>
                        </DataTable>
                    </template>
                </Column>




                <Column field="wensday" :header="dateHeader.wednesday"></Column>
                <Column field="thursday" :header="dateHeader.thursday"></Column>
                <Column field="friday" :header="dateHeader.friday"></Column>
                <Column field="changeWeek" header="">
                    <template #header="slotProps">
                        <div class="buttonContainer">
                            <button @click="previousWeek">&#9665;</button>
                            <button @click="nextWeek">&#9655;</button>
                        </div>
                    </template>
                </Column>
            </DataTable>
        </div>
    </div>
</template>



<script setup>
import { ref, onMounted, reactive } from 'vue';
import axios from 'axios';
import Dropdown from 'primevue/dropdown';


const innerTable = reactive([
    { plannedTime: '', workingTimes: '', breakTime: '', sumTime: '' }
])



const columns = ref([
    { field: 'plannedTime', header: 'Plan', width: '25%' },
    { field: 'workingTimes', header: 'Work', width: '25%' },
    { field: 'breakTime', header: 'Break', width: '25%' },
    { field: 'sumTime', header: 'Summe', width: '25%' },
    // Add more columns as needed
]);





let employeeId;

const selectedProject = ref();
const selectedName = ref();


function fetchDataOfEmployee() {
    employeeId = selectedName.value.employeeId
    console.log(employeeId)
    getDataFromBackend(employeeId)
}

let projectForeignKey;

async function fetchEmployeesOfProject() {
    projectForeignKey = selectedProject.value.code;
    employeeNames.value = [];
    selectedName.value = null;

    const url = `http://localhost:8000/getEmployeesToProjectId/${projectForeignKey}`
    const response = await axios.get(url)

    const employeeResponse = response.data.data;

    employeeResponse.forEach((element, index) => {
        const foreName = element.forename;
        const sureName = element.surname;
        const fullName = `${foreName} ${sureName}`;
        const employeeId = element.id;
        employeeNames.value.push({ name: fullName, employeeId: employeeId })
    })
}

async function fetchProjectsOfEmployee() {
    const url = "http://localhost:8000/getProjectsWhereProjectLeader/3007"
    const response = await axios.get(url)
    const projects = response.data.projects;
    projects.forEach((element) => {
        projectNames.value.push({ name: element.projectNames, code: element.foreignKeysForProject })
    })
}

const employeeNames = ref([
    { name: '', employeeId: '' }
]);

const projectNames = ref([
    { name: '', code: '' }
]);

const products = ref([]);

let currentDate = new Date();


const dateHeader = ref({
    monday: "",
    tuesday: "",
    wednesday: "",
    thursday: "",
    friday: "",
})

onMounted(() => {
    getWeekDate();
    // Kann bei WorkingTimes direkt hier aufgerufen werden da wir ID aus dem
    // SESSion Managment bekommen 
    //getDataFromBackend(2);
    fetchProjectsOfEmployee();
});



function fillmonthArray() {
    const monthArray = [];
    monthArray.push(dateHeader.value.monday, dateHeader.value.tuesday,
        dateHeader.value.wednesday, dateHeader.value.thursday, dateHeader.value.friday)
    monthArray.forEach((element, index, array) => {
        array[index] = element.slice(5);
    });

    return monthArray

}




async function getDataFromBackend(employeeId) {
    try {
        console.log(employeeId)
        const startDate = dateHeader.value.monday
        const startDateRightFormat = startDate.slice(5)
        const endDate = dateHeader.value.friday
        const endDateRightFormat = endDate.slice(5)

        //const url = `http://localhost:8000/getTest/2/${startDateRightFormat}/${endDateRightFormat}`
        const url = `http://localhost:8000/getTest/${employeeId}/${projectForeignKey}`
        const response = await axios.get(url);
        processData(response.data.positions);

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


function processData(backendData) {
    backendData.forEach((element) => {
        products.value.push({ code: element.projectName + " " + element.id, id: element.id })


    })

    fillInnerTable()




}


const positionArray = [];


async function fillInnerTable() {
    try {
        const monthArray = fillmonthArray();


        products.value.forEach((element) => {
            positionArray.push(element.id)
        })
        console.log(console.log(monthArray))
        console.log(console.log(positionArray))


        const url = `http://localhost:8000/getBookingTimes/3013/${monthArray[0]}`
        const response = await axios.get(url)
        const bookingTimes = (response.data.bookingTimes)
        console.log(bookingTimes)


        bookingTimes.forEach((element, index) => {
            const planStart = element.forecast_start.slice(0, 2)
            const planEnd = element.forecast_end.slice(0, 2)
            const planed = planEnd - planStart;
            const workingTimes = element.start_time + "-" + element.end_time;
            const breakTime = element.pause;
            const sumTime = element.end_time.slice(0, 2) - element.start_time.slice(0, 2)
            const x = { plannedTime: planed, workingTimes: workingTimes, breakTime: breakTime, sumTime: sumTime }
            const y = { plannedTime: planed, workingTimes: workingTimes, breakTime: breakTime, sumTime: sumTime }


            innerTable[0] = x





            // innerTable[index].plannedTime = planed;
            // innerTable[index].workingTimes = workingTimes;
            // innerTable[index].breakTime = breakTime;
            // innerTable[index].sumTime = sumTime;

        })

    }
    catch (error) {
        console.log(error)
    }
}

// Funktion, um die Datumswerte auf die nächste Woche zu ändern
function nextWeek() {
    currentDate.setDate(currentDate.getDate() + 7);
    updateDateHeader();
}

function previousWeek() {
    currentDate.setDate(currentDate.getDate() - 7);
    updateDateHeader();
}


function updateDateHeader() {
    const targetDate = new Date(currentDate);
    let day = targetDate.getDay();
    targetDate.setDate(currentDate.getDate() - day + (day === 0 ? -6 : 1));
    const weekDates = [];

    for (let i = 0; i < 5; i++) {
        const formattedDate = formatDate(targetDate);
        weekDates.push(formattedDate);
        targetDate.setDate(targetDate.getDate() + 1);
    }

    dateHeader.value.monday = weekDates[0];
    dateHeader.value.tuesday = weekDates[1];
    dateHeader.value.wednesday = weekDates[2];
    dateHeader.value.thursday = weekDates[3];
    dateHeader.value.friday = weekDates[4];
}


function getWeekDate() {
    const today = new Date();
    const targetDate = new Date(today);

    let day = targetDate.getDay();
    targetDate.setDate(today.getDate() - day + (day === 0 ? -6 : 1));

    const weekDates = [];

    // Iteriere über die Wochentage und füge die Werte zum Array hinzu
    for (let i = 0; i < 5; i++) {
        const formattedDate = formatDate(targetDate);
        weekDates.push(formattedDate);
        targetDate.setDate(targetDate.getDate() + 1);

    }
    dateHeader.value.monday = weekDates[0]
    dateHeader.value.tuesday = weekDates[1]
    dateHeader.value.wednesday = weekDates[2]
    dateHeader.value.thursday = weekDates[3]
    dateHeader.value.friday = weekDates[4]
}

function formatDate(date) {
    const options = { weekday: 'short', day: '2-digit', month: '2-digit', year: 'numeric' };
    return date.toLocaleDateString('de-DE', options);
}






</script>

<style scoped>
.buttonContainer {
    width: 70px;
}

.buttonContainer>button {
    color: aqua;

    font-size: 32px;
    padding: 5%;
}
</style>
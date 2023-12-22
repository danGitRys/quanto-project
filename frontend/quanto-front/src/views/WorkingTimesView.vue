<template>
    <div class="card">
        
        <DataTable :value="products" tableStyle="min-width: 50rem">
            <Column field="code" header="Code"></Column>
            <Column field="monday" :header=dateHeader.monday>
                
                <template #body="{ row }">
                    <DataTable :value="innerTable">
                        <Column field="innerCode" header="Plan"></Column>
                        <Column field="secondCode" header="Work"></Column>
                        <Column field="drei" header="Break"></Column>
                        <Column field="four" header="Summe"></Column>
                    </DataTable>
                </template>
                
            </Column>
            <Column field="tuesday" :header=dateHeader.tuesday></Column>
            <Column field="wensday" :header=dateHeader.wensday></Column>
            <Column field="thursday" :header=dateHeader.thursday></Column>
            <Column field="friday" :header=dateHeader.friday></Column>
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
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import axios from 'axios';

const products = ref([]);
const innerTable = ref([]);

const dateHeader = ref({
    monday: "",
    tuesday:"",
    wensday: "",
    thursday: "",
    friday: "",
})

onMounted(() => {
    getWeekDate();
    getDataFromBackend();
    
});

let projectObject = [];

function nextWeek() {
    console.log(projectObject)
}



function getWeekDate(){
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
    dateHeader.value.wensday = weekDates[2]
    dateHeader.value.thursday = weekDates[3]
    dateHeader.value.friday = weekDates[4]
}

function formatDate(date) {
    const options = { weekday:'short', day: '2-digit', month: '2-digit', year: 'numeric' };
    return date.toLocaleDateString('de-DE', options);
}

async function getDataFromBackend() {
    try {
        const startDate = dateHeader.value.monday
        const startDateRightFormat = startDate.slice(5)
        const endDate =  dateHeader.value.friday
        const endDateRightFormat = endDate.slice(5)

        console.log(startDate)
        console.log(startDateRightFormat)
        console.log(endDateRightFormat)

        //const url = `http://localhost:8000/getTest/2/${startDateRightFormat}/${endDateRightFormat}`
        const url = "http://localhost:8000/getTest/2/25.11.2023/12.12.2023"
        const response = await axios.get(url);
        console.log(response.data)
        processData(response.data.positions);

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function processData(backendData) {

    products.value = backendData.map(item => ({
        code: item.projectName + "\r" + item.id,

     
    }));
    backendData.forEach((element, index) =>{
        projectObject.push({projectName: element.projectName, positionId: element.id})
        console.log(element)
    })

    
    fillInnerTable()

}

async function fillInnerTable(){
    try{
        const url = "http://localhost:8000/getBookingTimes/2/01.01.2023"
        const response = await axios.get(url)
        const bookingTimes = (response.data.bookingTimes)
         
        

        console.log(bookingTimes)
        bookingTimes.forEach((element) => {

             const planStart = element.forecast_start.slice(0,2)
             const planEnd = element.forecast_end.slice(0,2)
             const planed =  planEnd - planStart;

             innerTable.value.push({ innerCode: planed, secondCode: element.start_time + "-" + element.end_time , drei: element.pause })
        })

    }
    catch(error) {
        console.log(error)
    }
   

   

}




</script>

<style scoped>
.buttonContainer{
    width: 70px;
}
.buttonContainer > button {
    color: aqua;
    
    font-size: 32px;
    padding: 5%;
}

</style>
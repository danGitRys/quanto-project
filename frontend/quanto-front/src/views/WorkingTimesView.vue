<template>
    <div class="card">
        
        <DataTable :value="products" tableStyle="min-width: 50rem">
            <Column field="code" header="Code"></Column>
            <Column field="monday" :header=dateHeader.monday>
                <template #body="{ row }">
                    <DataTable :value="innerTable">
                        <Column field="innerCode" header="Inner Code"></Column>
                        <!-- Weitere Spalten für die innere Tabelle -->
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
    tuesday:" ",
    wensday: " ",
    thursday: " ",
    friday: " ",
})

onMounted(() => {
    getWeekDate();
    getDataFromBackend();
    
});

function nextWeek(){
    const x = dateHeader.value.monday;
    const y = x.slice(5)
    
    

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
        const endDate =  dateHeader.value.friday

        console.log(startDate)


        console.log("HEy")
        const url = "http://localhost:8000/getTest/2008"
        const response = await axios.get(url);
        processData(response.data.positions);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


const data = ref({innerCode: "XXXX"}) 
    


function processData(backendData) {
    console.log(backendData);
    products.value = backendData.map(item => ({
        
        code: item.projectName + 
        "\r" + item.id
        //name: innerTable.value.push(data.value)
        
        
    }));

    


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
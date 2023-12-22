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
    getDataFromBackend();
    getWeekDate();
});

function nextWeek() {
    const daysInWeek = 7;
    const millisecondsInDay = 86400000; // Anzahl der Millisekunden pro Tag
    // Für jeden Tag von Montag bis Freitag
    for (let i = 0; i < 5; i++) {
        const currentDay = Object.keys(dateHeader.value)[i];
        // Erstelle ein neues Date-Objekt mit dem aktuellen Tag
        const nextWeekDate = new Date(dateHeader.value[currentDay]);
        // Füge sieben Tage zur aktuellen Datum-Zeit hinzu, um eine Woche vorzuspringen
        nextWeekDate.setTime(nextWeekDate.getTime() + daysInWeek * millisecondsInDay);
        // Aktualisiere den Wert im dateHeader-Objekt
        dateHeader.value[currentDay] = nextWeekDate.toDateString();
    }   
}

function previousWeek() {
    const daysInWeek = 7;
    const millisecondsInDay = 86400000; // Anzahl der Millisekunden pro Tag

    // Für jeden Tag von Montag bis Freitag
    for (let i = 0; i < 5; i++) {
        const currentDay = Object.keys(dateHeader.value)[i];

        // Erstelle ein neues Date-Objekt mit dem aktuellen Tag
        const previousWeekDate = new Date(dateHeader.value[currentDay]);

        // Subtrahiere sieben Tage von der aktuellen Datum-Zeit, um eine Woche zurückzugehen
        previousWeekDate.setTime(previousWeekDate.getTime() - daysInWeek * millisecondsInDay);

        // Aktualisiere den Wert im dateHeader-Objekt
        dateHeader.value[currentDay] = previousWeekDate.toDateString();
    }

}




function getWeekDate(){
    const today = new Date();
    const targetDate = new Date(today);
 
    let day = targetDate.getDay();
     targetDate.setDate(today.getDate() - day + (day === 0 ? -6 : 1));

    const weekDates = [];

    // Iteriere über die Wochentage und füge die Werte zum Array hinzu
    for (let i = 0; i < 5; i++) {
        weekDates.push(targetDate.toDateString());
        targetDate.setDate(targetDate.getDate() + 1);
        
    }
    dateHeader.value.monday = weekDates[0]
    dateHeader.value.tuesday = weekDates[1]
    dateHeader.value.wensday = weekDates[2]
    dateHeader.value.thursday = weekDates[3]
    dateHeader.value.friday = weekDates[4]
}



async function getDataFromBackend() {
    try {
        const url = "http://localhost:8000/getPositionsOfProjectOfEmployee/2008"
        const response = await axios.get(url);
        processData(response.data.positions);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}



const data = ref({innerCode: "XXXX"}) 
    


function processData(backendData) {
    products.value = backendData.map(item => ({
        code: item.id,
        name: innerTable.value.push(data.value)
        
        
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
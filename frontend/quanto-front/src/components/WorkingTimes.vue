<template>
        <div class="card">
            <DataTable :value="products" tableStyle="min-width: 50rem">
                <Column field="code" header="Projekt"></Column>
                <Column field="id" header="ID"></Column>
                <Column field="monday" :header="dateHeader.monday">
                    <template #body="slotProps">
                        <template v-if="slotProps.index < monday.length">
                            <InnerTable2 :people="monday[slotProps.index]" />
                        </template>
                    </template>
                </Column>


                <Column field="tuesday" :header="dateHeader.tuesday">
                    <template #body="slotProps">
                        <template v-if="slotProps.index < tuesday.length">
                            <InnerTable2 :people="tuesday[slotProps.index]" />
                        </template>
                    </template>
                </Column>




                <Column field="wensday" :header="dateHeader.wednesday">
                    <template #body="slotProps">
                        <template v-if="slotProps.index < wednesday.length">
                            <InnerTable2 :people="wednesday[slotProps.index]" />
                        </template>
                    </template>
                </Column>

                <Column field="thursday" :header="dateHeader.thursday">
                    <template #body="slotProps">
                        <template v-if="slotProps.index < thursday.length">
                            <InnerTable2 :people="thursday[slotProps.index]" />
                        </template>
                    </template>
                </Column>

                <Column field="friday" :header="dateHeader.friday">
                    <template #body="slotProps">
                        <template v-if="slotProps.index < friday.length">
                            <InnerTable2 :people="friday[slotProps.index]" />
                        </template>
                    </template>
                </Column>

                <Column field="timeCorrection" header="TimeCorrection">
                    <template #body="slotProps">
                        <button class="confirmButton" :id="'confirmButton' + slotProps.index"
                            @click="confirmTimeCorrection(slotProps.index)">Confirm</button>
                    </template>

                </Column>


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
import Dropdown from 'primevue/dropdown';
import InnerTable2 from './InnerTable2.vue';
import { parse } from 'vue/compiler-sfc';



// monday Array
const monday = [];
const tuesday = [];
const wednesday = [];
const thursday = [];
const friday = [];




let employeeId;

const selectedProject = ref();
const selectedName = ref();


function confirmTimeCorrection(index) {
    const confirmButton = document.getElementById('confirmButton' + index);

    // Zugriff auf die Tabelle (parentNode der Tabellenzeile)
    const table = confirmButton.closest('table');

    // Ändern der Hintergrundfarbe der gesamten Tabelle
    table.classList.add('tableConfirmed');

    // Ändern der Stile des Buttons
    confirmButton.style.backgroundColor = 'green';
    confirmButton.style.color = 'white';
    confirmButton.innerHTML = 'Confirmed';
    confirmButton.disabled = true;
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
    getDataFromBackend(2005);
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
        const url = `http://localhost:8000/getAllPositionsFromAllProjects/${employeeId}`
        const response = await axios.get(url);
        console.log(response.data.positions);
        processData(response.data.positions);

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}





let bookingTimesArray = [];
async function processData(backendData) {


    const monthArray = fillmonthArray();
    console.log(monthArray);

    const positionArray = [];
    backendData.forEach((element) => {
        positionArray.push(element.id);
    });

    for (const date of monthArray) {
        console.log(date);

        for (const [index, position] of positionArray.entries()) {
            
            // HARDGECODET -> WARTEN AUF SESSIONMANGMENT
            employeeId = 2005;

            const urlBookingTimes = `http://localhost:8000/getBookingTimesForDay/${position}/${date}/${employeeId}`;
            const urlForecastTimes = `http://localhost:8000/getForecastForDay/${position}/${date}/${employeeId}`;
            const responseBookingTimes = await axios.get(urlBookingTimes);
            const responseForecastTimes = await axios.get(urlForecastTimes);
            let bookingArray = responseBookingTimes.data.bookingTimes[0];
            let forecastArray = responseForecastTimes.data.forecastTimes[0];

            if (bookingArray == undefined) {
                bookingArray = { start_time_booking: '00:00:00', end_time_booking: '00:00:00', pause_booking: '0' };
            }

            if (forecastArray == undefined) {
                forecastArray = { forecast_start: '00:00:00', forecast_end: '00:00:00', position_id: position };
            }


            console.log(bookingArray);
            console.log(forecastArray);




            bookingTimesArray = [{ ...bookingArray, ...forecastArray }]
            console.log(bookingTimesArray);

            for (const element of bookingTimesArray) {
                if (Object.keys(element).length === 0) {
                    console.log('Das Objekt ist leer.');
                } else {
                    console.log('Das Objekt ist nicht leer.');
                    console.log(element);

                    const planStart = element.forecast_start.slice(0, 2);
                    const planEnd = element.forecast_end.slice(0, 2);
                    const planned = planEnd - planStart;
                    const workingTimes = element.start_time_booking.slice(0, 5) + '-' + element.end_time_booking.slice(0, 5);
                    const breakTime = element.pause_booking;
                    
                    const sumTime = element.end_time_booking.slice(0, 2) - element.start_time_booking.slice(0, 2) - breakTime;
                    const positionId = element.position_id;
                    const bookingId = element.booking_id;

                    const x = { planned: planned, working: workingTimes, break: breakTime, sum: sumTime }
                    console.log(x)



                    if (date == dateHeader.value.monday.slice(5) && positionId == position)
                        monday[index] = { planned, working: workingTimes, break: breakTime, sum: sumTime, positionId: position, selectedDate: date, bookingId: bookingId };
                    if (date == dateHeader.value.tuesday.slice(5) && positionId == position)
                        tuesday[index] = { planned, working: workingTimes, break: breakTime, sum: sumTime, positionId: position, selectedDate: date, bookingId: bookingId };
                    if (date == dateHeader.value.wednesday.slice(5) && positionId == position)
                        wednesday[index] = { planned, working: workingTimes, break: breakTime, sum: sumTime, positionId: position, selectedDate: date,bookingId: bookingId };
                    if (date == dateHeader.value.thursday.slice(5) && positionId == position)
                        thursday[index] = { planned, working: workingTimes, break: breakTime, sum: sumTime, positionId: position, selectedDate: date, bookingId: bookingId };
                    if (date == dateHeader.value.friday.slice(5) && positionId == position)
                        friday[index] = { planned, working: workingTimes, break: breakTime, sum: sumTime, positionId: position, selectedDate: date, bookingId: bookingId };

                    // Hier kannst du weiteren Code für nicht leere Objekte hinzufügen
                    console.log(monday);
                }
            }






        }
    }
    //// Position Name hinzufügen????
    backendData.forEach((element) => {
        products.value.push({ code: element.projectName, id: element.id })
    });

    addSumTable();

}

function addSumTable() {
 
    products.value.push({ code: 'Summe' });
    
    let mondaySum = 0;
    let mondayBreakSum = 0;
    let mondayPlannedSum = 0;
    let tuesdaySum = 0;
    let tuesdayBreakSum = 0;
    let tuesdayPlannedSum = 0;
    let wednesdaySum = 0;
    let wednesdayBreakSum = 0;
    let wednesdayPlannedSum = 0;
    let thursdaySum = 0;
    let thursdayBreakSum = 0;
    let thursdayPlannedSum = 0;
    let fridaydaySum = 0;
    let fridayBreakSum = 0;
    let fridayPlannedSum = 0;
    
    for (let i = 0; i < monday.length; i++) {
        mondaySum += monday[i].sum; 
        mondayBreakSum += parseInt(monday[i].break, 10); 
        mondayPlannedSum += monday[i].planned;
    }
    
    for (let i = 0; i < tuesday.length; i++) {
        tuesdaySum += tuesday[i].sum;
        tuesdayBreakSum += parseInt(tuesday[i].break, 10);
        tuesdayPlannedSum += tuesday[i].planned; 
    }

    for (let i = 0; i < wednesday.length; i++) {
        wednesdaySum += wednesday[i].sum;
        wednesdayBreakSum += parseInt(wednesday[i].break, 10); 
        wednesdayPlannedSum += wednesday[i].planned;
    }

     for (let i = 0; i < thursday.length; i++) {
        thursdaySum += thursday[i].sum;
        thursdayBreakSum += parseInt(thursday[i].break, 10);
        thursdayPlannedSum += thursday[i].planned;
    }
    
    for (let i = 0; i < friday.length; i++) {
        fridaydaySum += friday[i].sum;  
        fridayBreakSum += parseInt(friday[i].break, 10);
        fridayPlannedSum += friday[i].planned;
    }


    monday[monday.length] = { sum: mondaySum, break: mondayBreakSum, planned: mondayPlannedSum };
    tuesday[tuesday.length] = { sum: tuesdaySum, break: tuesdayBreakSum, planned: tuesdayPlannedSum };
    wednesday[wednesday.length] = { sum: wednesdaySum, break: wednesdayBreakSum, planned: wednesdayPlannedSum };
    thursday[thursday.length] = { sum: thursdaySum, break: thursdayBreakSum, planned: thursdayPlannedSum };
    friday[friday.length] = { sum: fridaydaySum,    break: fridayBreakSum, planned: fridayPlannedSum};
   
}



// Funktion, um die Datumswerte auf die nächste Woche zu ändern
function nextWeek() {
    currentDate.setDate(currentDate.getDate() + 7);
    updateDateHeader();
    clearTable();
    // HARDGECODET EMP IDD -> WARTEN AUF SESSIONMANGMENT
    getDataFromBackend(2005);

}

function clearTable() {
    monday.length = 0;
    tuesday.length = 0;
    wednesday.length = 0;
    thursday.length = 0;
    friday.length = 0;
    products.value.length = 0;

}

function previousWeek() {
    currentDate.setDate(currentDate.getDate() - 7);
    updateDateHeader();
    clearTable();
    // HARDGECODET EMP IDD -> WARTEN AUF SESSIONMANGMENT
    getDataFromBackend(2005);
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
#projectNameDropDown {
    margin-top: 10px;
    margin-bottom: 10px;
    font-weight: 900;

}

#employeeDropDown {

    margin-bottom: 10px;
    font-weight: 900;
}

.tableConfirmed {
    background-color: lightgreen;
    /* Add other styles as needed */
}


.buttonContainer {
    width: 70px;
}

.buttonContainer>button {
    color: #304C5D;
    font-size: 32px;
    padding: 5%;
}

.confirmButton {

    border: 1px solid black;
    border-radius: 5px;
    padding: 5px;
    background-color: rgb(9, 255, 17);
    margin-left: 25px;
}

.dropDownButton {
    height: 500px;
    width: 500px;
    font-size: 500px;
    font-weight: bold;
    color: #304C5D;
}

.p-dropdown-label p-inputtext p-placeholder {
    font-size: 500px;
    font-weight: bold;
    color: #304C5D;
}
</style>
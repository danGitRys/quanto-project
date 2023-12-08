<template>
    <div class="container">
      <div class="card p-fluid">
        <div style="max-height: 700px; overflow-y: auto;">
          <DataTable
            :value="displayedData"
            editMode="cell"
            @cell-edit-complete="onCellEditComplete"
            :pt="{
              table: { style: 'min-width: 50rem' },
              column: {
                bodycell: ({ state }) => ({
                  class: [{ 'pt-0 pb-0': state['d_editing'] }],
                }),
              },
            }"
          >
            <Column
              v-for="col of columns"
              :key="col.field"
              :field="col.field"
              :header="col.header"
              style="width: 25%"
            >
              <template #body="{ data, field }">
                <span v-if="editingRow !== data">
                  {{ field === 'date' ? formatDateTime(data[field]) : data[field] }}
                </span>
              </template>
  
              <template v-if="col.field !== 'date'" #editor="{ data, field }">
                <InputText v-model="data[field]" ref="inputField" @input="onInput" />
              </template>
            </Column>
          </DataTable>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import InputText from 'primevue/inputtext';
  import { ref } from 'vue';
  import axios from 'axios';
  
  export default {
    components: {
      InputText,
    },
    data() {
      return {
        generatedDate: [],
        columns: [
          { field: 'date', header: 'Date' },
          { field: 'hours_in_projects', header: 'Hours in Projects' },
          { field: 'hours_this_project', header: 'Hours this Project' },
          { field: 'pos', header: 'Pos' },
        ],
        editingRow: null,
      };
    },
    mounted() {
      this.generateDatesForCurrentMonth();
      this.getDataFromBackend();
    },
    computed: {
      displayedData() {
        return [...this.generatedDate];
      },
    },
    methods: {
      onCellEditComplete: function (event) {
        let { data, newValue, field } = event;
  
        if (data[field] !== newValue) {
          switch (field) {
            case 'hours_in_projects':
            case 'hours_this_project':
              if (typeof newValue === 'string' && this.isPositiveInteger(newValue.trim())) {
                data[field] = newValue.trim();
              } else {
                event.preventDefault();
              }
              break;
  
            default:
              if (typeof newValue === 'string' && newValue.trim().length > 0) {
                data[field] = newValue.trim();
              } else {
                event.preventDefault();
              }
              break;
          }
  
          this.editingRow = null;
        }
      },
  
      isPositiveInteger(val) {
        let str = String(val);
        str = str.trim();
        if (!str) {
          return false;
        }
        str = str.replace(/^0+/, '') || '0';
        var n = Math.floor(Number(str));
        return n !== Infinity && String(n) === str && n >= 0;
      },
  
      onInput() {
        const inputFieldValue = this.$refs.inputField?.$props?.value;
        this.editingRow = inputFieldValue;
      },
  
      daysInMonth(month, year) {
        return new Date(year, month, 0).getDate();
      },
  
      generateDatesForCurrentMonth() {
        let date = new Date();
        let month = date.getMonth() + 1;
        let year = date.getFullYear();
        let daysInMonth = this.daysInMonth(month, year);
  
        for (let day = 1; day <= daysInMonth; day++) {
          const currentDate = new Date(year, month - 1, day);
          // Filtering out the weekend
          if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
            this.generatedDate.push({
              date: currentDate,
            });
          }
        }
      },
  
      formatDateTime(date) {
        const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
        return new Intl.DateTimeFormat('en-US', options).format(date);
      },
  
      getDataFromBackend() {
        const url = "http://localhost:8000/getForecast/5";
        axios.get(url)
          .then(response => {
            console.log(response.data.data);
            const startDate = response.data.data.start;
            const endDate = response.data.data.end;
            this.calculateHours(startDate, endDate);
          })
      },
  
      calculateHours(startDate, endDate) {
    const startDateTime = new Date(startDate);
    const endDateTime = new Date(endDate);

    // Whether endDate is after startDate
    if (endDateTime <= startDateTime) {
      console.error("Enddatum sollte nach dem Startdatum liegen.");
      return;
    }

    // calculate the total difference in hours
    const totalHours = (endDateTime - startDateTime) / (1000 * 60 * 60);

    // Split the hours in workdays form mon-fri
    const workdays = this.getWorkdays(startDateTime, endDateTime);
    const hoursPerDay = totalHours / workdays;

    this.generatedDate.forEach((day) => {
      day.hours = hoursPerDay;
      console.log(day.hours + " StUNDEN");
    });
  },

  getWorkdays(startDate, endDate) {
    // calculate the workdays between start- and endDate
    let count = 0;
    let current = new Date(startDate);

    while (current <= endDate) {
      const dayOfWeek = current.getDay();

      if (dayOfWeek >= 1 && dayOfWeek <= 5) {
        count++;
      }

      // go to next day
      current.setDate(current.getDate() + 1);
    }

    return count;
  },
    },
  };
  </script>
  
  <style scoped>
  .container {
    position: relative;
  }
  
  .card {
    position: absolute;
    bottom: -37em;
    left: 6em;
  }
  </style>
  
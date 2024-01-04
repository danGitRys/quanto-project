<template>
    <div class="container">
      <Bar v-if="loaded" :data="chartData" />
    </div>
    <div>
      <apexchart width="500" type="line" :options="apexOptions" :series="apexSeries"></apexchart>
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs'
  import VueApexCharts from 'vue3-apexcharts'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  import axios from "axios"
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'BarChart',
    components: { Bar },
    data() {
      return {
        loaded: false,
        chartData: null,
        apexOptions: {
          chart: {
            id: 'vuechart-example'
          },
          xaxis: {
            categories: []
          }
        },
        apexSeries: [{
          name: 'series-1',
          data: []
        }]
      }
    },
  
    async mounted() {
      this.loaded = false
  
      try {
        const response = await axios.get("http://localhost:8000/positionLinearGraph/" + this.$route.params.id)
        const responseData = response.data
        const valid = responseData.success
  
        if (valid) {
          const tempData = responseData.data
          const xData = tempData.x
          const yData = tempData.y
  
          // Update chartData with xData and yData
          this.chartData = {
            labels: xData,
            datasets: [{ data: yData }]
          }
  
          // Update ApexChart options and series
          this.apexOptions = {
        ...this.apexOptions,
        xaxis: {
          ...this.apexOptions.xaxis,
          categories: xData
        }
      };
      this.apexSeries = [{ name: 'series-1', data: yData }];
        } else {
          alert("This Team doesn't exist")
        }
      } catch (error) {
        console.error(error)
      }
  
      this.loaded = true
    }
  }
  </script>
  
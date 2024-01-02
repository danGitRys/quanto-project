

<template>
    <div class="container">
      <Bar v-if="loaded" :data="chartData" />
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  import axios from "axios"
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'BarChart',
    components: { Bar },
    data: () => ({
      loaded: false,
      chartData: null
    }),
    async mounted() {
      this.loaded = false
  
      try {
        const response = await axios.get("http://localhost:8000/positionGraph/" + this.$route.params.id)
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
  
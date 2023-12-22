<template>
    <div>
      <apexchart width="500" type="line" :options="apexOptions" :series="apexSeries"></apexchart>
    </div>
  </template>
  
  <script>
  import VueApexCharts from 'vue3-apexcharts';
  import axios from 'axios';
  
  export default {
    name: 'BarChart',
    components: { VueApexCharts },
    data() {
      return {
        loaded: false,
        apexOptions: {
          chart: {
            id: 'vuechart-example'
          },
          xaxis: {
            categories: []
          }
        },
        apexSeries: [],
      };
    },
  
    async mounted() {
      this.loaded = false;
  
      try {
        const response = await axios.get("http://localhost:8000/projectPositionsLinearGraph/" + this.$route.params.id);
        const responseData = response.data;
        const valid = responseData.success;
  
        if (valid) {
          const data = responseData.data;
          const xData = data.xData;
          const yData = data.yData;
  
          // Update ApexChart options and series
          this.apexOptions = {
            ...this.apexOptions,
            xaxis: {
              ...this.apexOptions.xaxis,
              categories: xData
            }
          };
  
          this.apexSeries = yData.map(item => ({
            name: item.positionName,
            data: item.yValues
          }));
        } else {
          alert("This Team doesn't exist");
        }
      } catch (error) {
        console.error(error);
      }
  
      this.loaded = true;
    }
  };
  </script>
  
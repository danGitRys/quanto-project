<template>
    <div>
      <apexchart width="500" type="line" :options="apexOptions" :series="apexSeries"></apexchart>
    </div>
  </template>
  
  <script>
  import VueApexCharts from 'vue3-apexcharts';
  import axios from 'axios';
//import { transformWithEsbuild } from 'vite';
import { projectIdStore } from "@/store/projectIdStore";
import {projectionStore} from "@/store/projectionStore";
  
  export default {
    name: 'BarChart',
    components: { VueApexCharts },
    data() {
      return {
        props:{
          id: String,
        },
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
        const projectId = projectIdStore().sharedData;
        const projection = projectionStore().sharedData;

        var days = 0;


        switch(projection){

          case '4 Weeks':
            days=28;
            break;
          
          case '8 Weeks':
            days = 56;
            break;
          
          default:
            days= 1000;
            break;


        }

        const response = await axios.get("http://localhost:8000/projectProjectionGraph/"+projectId+"/"+days,
        {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`,
                },
            });
        const responseData = response.data;
        console.log(responseData)
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
            data: item.yValues.map(value => parseFloat(value).toFixed(2))
          }));
        } else {
          alert("Error Plotting Projection Graph");
        }
      } catch (error) {
        console.error(error);
      }
  
      this.loaded = true;
    }
  };
  </script>
  
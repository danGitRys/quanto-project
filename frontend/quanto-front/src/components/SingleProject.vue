<template>
<div id="info">
    <v-card>
        <v-title>{{ project_name }}</v-title>
        <p>Company: {{ company }}</p>
        <p>Project ID: {{ project_id }}</p>
        <p>Project Start Date: {{ project_start }}</p>
        <p>Project End Date: {{ project_end }}</p>
        <p>Project Creator: {{ project_creator }}</p>
        <p>Project Creation Date: {{ proejct_creationDate }}</p>
    </v-card>
</div>
<dif id="Positions">
  
  

      <DataTable :value="positonList" stripedRows tableStyle="min-width: 50rem">
    <Column field="id" header="Code"></Column>
    <Column field="position_id" header="Name"></Column>
    <Column field="position_name" header="Position-Name"></Column>
    <Column field="start_date" header="Start Date"></Column>
    <Column field="end_date" header="End Date"></Column>
    <Column field="rate" header="Hourly Rate"></Column>
    <Column field="volume_remaining" header="Volume Remaining"></Column>
    <Column field="volume_total" header="Volume Total"></Column>
    <Column field="wd" header="Working Days"></Column>
</DataTable>
   
</dif>
<div id="Assigned Employees">

</div>

<div id="Booking history">

</div>

<div id="Forecast">

</div>
</template>

<script>
import axios from "axios"
import { getBaseTransformPreset } from '@vue/compiler-core';
import 'primevue/resources/themes/lara-light-green/theme.css'


export default {
    
    data() {
        return {
            company:'',
            project_id:'',
            project_pid:'',
            project_name:'',
            project_start:'',
            project_end:'',
            project_creator:'',
            proejct_creationDate:'',
            positonList:[],

        }
    },

    methods:{
        getProject(){
            console.log("test")
            axios.get("http://localhost:8000/getProject/"+this.$route.params.id,{
           
        }).then(response => {
            console.log(response)
            
            var responseData = response.data
            var valid = responseData.success
            if(valid==true){
                var tempData = responseData.data
                console.log(tempData)
                this.company = tempData["company"],
                this.project_id = tempData["id"],
                this.project_pid = tempData["p_id"],
                this.project_name = tempData["name"],
                this.project_start = tempData["start_date"],
                this.project_end = tempData["end_date"],
                this.project_creator = tempData["fk_creator"]
                this.proejct_creationDate = tempData["creation_date"]
           
            }
            else{
                alert("This Team doesnt exist")
            }
           
            
        })
        .catch(error=> {
            console.log(error)
            
        })
        },

        getPositonsToProject(){
            console.log("test")
            axios.get("http://localhost:8000/getPositionsToProjectId/"+this.$route.params.id,{
           
        }).then(response => {
            console.log(response)
            
            var responseData = response.data
            var valid = responseData.success
            if(valid==true){
                var tempData = responseData.data
                console.log(tempData)
                for(var i=0;i<tempData.length;i++){
                    var tempPosition = tempData[i]
                    console.log(tempPosition)
                    var tempEntry = {
                        "end_date":tempPosition["end_date"],
                        "fk_project":tempPosition["fk_project"],
                        "id":tempPosition["id"],
                        "position_id":tempPosition["position_id"],
                        "position_name":tempPosition["position_name"],
                        "rate": tempPosition["rate"],
                        "start_date":tempPosition["start_date"],
                        "volume_remaining":tempPosition["volume_remaining"],
                        "volume_total":tempPosition["volume_total"],
                        "wd":tempPosition["wd"]

                    }
                    this.positonList.push(tempEntry)
                }
                
           
            }
            else{
                alert("This Team doesnt exist")
            }
           
            
        })
        .catch(error=> {
            console.log(error)
            
        })
        },

        getEmployeesToProject(){
            console.log("test")
            axios.get("http://localhost:8000/getEmployeesToProjectId/"+this.$route.params.id,{
           
        }).then(response => {
            console.log(response)
            
            var responseData = response.data
            var valid = responseData.success
            if(valid==true){
                var tempData = responseData.data
                console.log(tempData)
                for(var i=0;i<tempData.length;i++){
                    var tempPosition = tempData[i]
                    console.log(tempPosition)
                    var tempEntry = {
                        "end_date":tempPosition["end_date"],
                        "fk_project":tempPosition["fk_project"],
                        "id":tempPosition["id"],
                        "position_id":tempPosition["position_id"],
                        "rate": tempPosition["rate"],
                        "start_date":tempPosition["start_date"],
                        "volume_remaining":tempPosition["volume_remaining"],
                        "volume_total":tempPosition["volume_total"],
                        "wd":tempPosition["wd"]

                    }
                    this.positonList.push(tempEntry)
                }
                
           
            }
            else{
                alert("This Team doesnt exist")
            }
           
            
        })
        .catch(error=> {
            console.log(error)
            
        })
        },

        getTeam15(){
            window.location.href = '/getTeam/15';
        }
    },

    beforeMount(){
        this.getProject()
        this.getPositonsToProject()
        this.getEmployeesToProject
    }


};

</script>

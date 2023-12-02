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
    <v-card>
    <v-title> Positions of project: {{ project_name }}</v-title>
    <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Position ID</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Rate</th>
            <th>Volume Remaining</th>
            <th>Volume Total</th>
            <th>Working Days (wd)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="position in positonList" :key="position.id">
            <td>{{ position.id }}</td>
            <td>{{ position.position_id }}</td>
            <td>{{ position.start_date }}</td>
            <td>{{ position.end_date }}</td>
            <td>{{ position.rate }}</td>
            <td>{{ position.volume_remaining }}</td>
            <td>{{ position.volume_total }}</td>
            <td>{{ position.wd }}</td>
          </tr>
        </tbody>
      </table>
    </v-card>
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

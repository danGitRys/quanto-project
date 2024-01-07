<template>



    <div id="info">
    
    
    <Fieldset legend="Project: {{ project_name }}">
        <p>Company: {{ company }}</p>
            <p>Project ID: {{ project_id }}</p>
            <p>Project Start Date: {{ project_start }}</p>
            <p>Project End Date: {{ project_end }}</p>
            <p>Project Creator: {{ project_creator }}</p>
            <p>Project Creation Date: {{ proejct_creationDate }}</p>
    </Fieldset>
    
    
    </div>
    
    
    
      
       
    
    
    
    <div id="Assigned Employees">
    
    </div>
    
    <div id="Booking history">
    
    </div>
    
    <div id="Forecast">
    
    </div>
    
    
    <Accordion :multiple="true" :activeIndex="[0]">
        <AccordionTab header="Positions in Project">
            <Card>
        <template #title> </template>
        <template #content>
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
        </template>
    </Card>
        </AccordionTab>
        <AccordionTab header="Employees in Project">
            <Card>
        <template #title> </template>
        <template #content>
            <DataTable :value="employeeList" stripedRows tableStyle="min-width: 50rem">
        <Column field="id" header="Id"></Column>
        <Column field="emp_id" header="Employee-Id"></Column>
        <Column field="forename" header="Forename"></Column>
        <Column field="surname" header="Surname"></Column>
        <Column field="mail" header="mail"></Column>
        <Column field="phone" header="Phone"></Column>
       
    </DataTable>
        </template>
    </Card>
        </AccordionTab>
        <AccordionTab header="Graphs and Analytics">
        <MultiLineGraph/>
            <Accordion :multiple="true" :activeIndex="[0]">
        <AccordionTab class="graphClass" header="Header I">
            <p class="m-0">
                <v-select
    v-model="selectedDuration"
    label="Select"
    :items="['4 Weeks','8 Weeks','Alltime']"
    variant="solo-filled"
    
  ></v-select>
  <ProjectionGraph :key="graphKey"/>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
                laborum.
            </p>
        </AccordionTab>
        <AccordionTab header="Header II">
            <p class="m-0">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo
                enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.
            </p>
        </AccordionTab>
        <AccordionTab header="Header III">
            <p class="m-0">
                At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in
                culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.
            </p>
        </AccordionTab>
    </Accordion>
        </AccordionTab>
    </Accordion>
    
    </template>
    
    
    <style>
    
    .graphClass{
        margin-left: 40px;
    }
    
    
    </style>
    
    <script>
    import axios from "axios"
    import { getBaseTransformPreset } from '@vue/compiler-core';
    import 'primevue/resources/themes/lara-light-green/theme.css'
    import MultiLineGraph from "@/components/graphs/ProjectPositionLinearGraph.vue"; // Corrected import
    import ProjectionGraph from "@/components/graphs/PositionProjectionGraph.vue"
    import { projectIdStore } from "@/store/projectIdStore";
    import {projectionStore} from "@/store/projectionStore";
    
    
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
                employeeList:[],
                projectId: this.$route.params.id,
                selectedDuration:'4 Weeks',
                graphKey: 0,
    
            }
        },
    
        components:{
             MultiLineGraph,
             ProjectionGraph
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

                    axios.get("http://localhost:8000/employee/"+this.project_creator,{
               
            }).then(response => {
                console.log(response)
                var creatorData = response.data.data 
                this.project_creator = creatorData["forename"] + " " + creatorData["surname"]
                
            
                
            })
            .catch(error=> {
                console.log(error)
                
            })
               
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
                            "id":tempPosition["id"],
                            "emp_id":tempPosition["emp_id"],
                            "fk_team_id":tempPosition["fk_team_id"],
                            "forename":tempPosition["forename"],
                            "surname":tempPosition["surname"],
                            "mail": tempPosition["mail"],
                            "phone":tempPosition["phone"],
                            "company_role":tempPosition["company_role"],
                            "team_role":tempPosition["team_roll"]
                        
    
                        }
                        this.employeeList.push(tempEntry)
                       
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
            },
            updateProjectId(){
                projectIdStore().setSharedData(this.$route.params.id);
            },
            setProjectionDuration(){
                projectionStore().setSharedData(this.selectedDuration)
            }
        },
    
        beforeMount(){
            this.getProject()
            this.getPositonsToProject()
            this.getEmployeesToProject()
            this.updateProjectId()
            this.setProjectionDuration()
        },
        watch: {
    selectedDuration(newValue) {
      console.log('Watch - Selected Duration Changed:', newValue);
      this.graphKey++;
                projectionStore().setSharedData(newValue)
            
    },
  },
};
    
    
    
    
    </script>
    
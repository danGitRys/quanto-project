<template>
    <div id="addEmployee">
        <Toast />
        <Card style="width: 60%">
            <template #title>New Employee</template>
            <template #content>
                <div class="container">
                    <h2 class="input-label"></h2>
                    <p class="input-container">
                        <label for="empId">Employee ID:</label>
                        <InputText id="empId" type="text" v-model="empid" placeholder="ID"/>
                    </p>
                    <Divider />
                    <p class="input-container">
                    <label for="firstname">First Name:</label>
                    <InputText
                        id="firstname"
                        type="text"
                        v-model="firstname"
                        placeholder="First Name"
                        describedby="firstnamedescription"
                    />
                    <label for="lastname">Last Name:</label>
                    <InputText
                        id="lastname"
                        type="text"
                        v-model="lastname"
                        placeholder="Last Name"
                        describedby="lastnamedescription"
                    />
                    </p>
                    <Divider />
                    <div class="input-container">
                        <label for="email">E-Mail:</label>
                        <InputText
                            id="email"
                            type="e-mail"
                            v-model="email"
                            placeholder="E-Mail"
                        />
                    </div>
                    <Divider />
                    <div class="input-container">
                        <label for="phone">Telephone-Number:</label>
                        <InputText
                            id="phone"
                            type="phone"
                            v-model="phone"
                            placeholder="Telephone-Number"
                        />
                    </div>
                    <Divider />
                    <div class="input-container">
                        <label for="ACTeam">Team:</label>
                        <AutoComplete
                            id="ACTeam" 
                            v-model="team" 
                            dropdown option-label="name" 
                            update:modelValue 
                            :suggestions="teams" 
                            placeholder="Teamname" 
                            @complete="getTeams" 
                        />
                    </div>
                    <Divider />
                    <div class="input-container">
                        <label for="ACTeamrole">Teamrole:</label>
                        <AutoComplete
                            id="ACTeamrole"
                            v-model="teamrole"
                            dropdown
                            :suggestions="teamroles"
                            update:modelValue 
                            placeholder="Teamrole"   
                            @complete="getTeamRoles" 
                        />
                    </div>         
                </div>
            </template>
        </Card>
    </div> 
    <footer>
        <Button label="Submit" icon="pi pi-check" @click="submitEmployee"/>
    </footer>
</template>

<script>
import { teamroles } from '@/store/teamroles';
import axios from 'axios';
import AutoComplete from 'primevue/autocomplete';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";

export default {
    name: "addEmployee",
    components: {
        AutoComplete,
        InputText,
        Button,
        Toast,
    },
    data() {
        return {
            empid: '',
            firstname: '',
            lastname: '',
            email: '',
            phone: '',
            team: '',
            teamid: 0,
            teamrole: '',
            teams: [],
            teamroles: [],
            filteredItems: [],
            toast: useToast(),
        }
    },
    methods: {
        init() {
            this.getTeams()
            this.getTeamRoles()
        },
        async getTeams() {
            try {
                const response = await axios.get("http://localhost:8000/getTeams", {})
                this.teams = response.data.teams
            } catch (error) {
                console.log(error);
            }
        },
        async getTeamRoles() {
            try {
                const response = await axios.get("http://localhost:8000/getTeamRoles", {})
                this.teamroles = response.data.roles
            } catch (error){
                console.log("An error occured while fetching Teamroles!")
            }
        },
        getTeamID() {
            for (let i = 0; i < this.teams.length; i++) {
                if (this.team.name == this.teams[i].name) {
                    this.teamid = this.teams[i].id
                }
            }
            console.log(this.teamid)
        },
        formIsValid() {
            if (this.empid == '') return false
            if (this.firstname == '') return false
            if (this.lastname == '') return false
            if (this.email == '') return false
            if (this.phone == '') return false
            if (this.team == '') return false
            if (this.teamrole == '') return false
            return true
        },
        submitEmployee() {
            if (this.formIsValid()) {
                this.getTeamID()
                console.log(this.teamid)
                const request = axios.post("http://localhost:8000/createEmployee", {
                    emp_id: this.empid,
                    forename: this.firstname,
                    surname: this.lastname,
                    email: this.email,
                    phone: this.phone,
                    fk_team_id: this.teamid,
                    team_role: this.teamrole,
                }).then(response => {
                    console.log(response)
                    if(response.data['success']==true){
                        this.toast.add({severity: 'success', summary: 'Success', detail: response.data.message, life: 3000})
                    }
                    else{
                        this.toast.add({severity: 'error', summary: 'Error', detail: response.data.error, life: 3000})
                    }
                }).catch(error=> {
                    this.toast.add({severity: 'error', summary: 'Error', detail: 'Error connecting to the Server.', life: 3000})
                })
            }
            else {
                this.toast.add({severity: 'error', summary: 'Error', detail: 'Please fill in all Fields.', life: 3000})
            }
        },
    },
    created() {
        this.init()
    }
};
</script>

<style scoped>

#addEmployee {
  justify-content: center;
  display: flex;
  margin-left: 55px;
  height: calc(100% - 185px);
}
footer {
    position: sticky;
    bottom: 0px;
    width: 100%;
    height: 75px;
    background-color: #94B8C7;
    display: flex;
    justify-content: center;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.input-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  padding: 10px 0;
}

.submitBtn {
    border: 2px solid #304C5D;
    background-color: #EF7C00;
    color: white;
    font-size: 22px;
    padding: 20px;
    display: flex;
    margin: 10px;
}


.container {

  border-radius: 10px;
  padding: 20px;
  margin: 30px;
}

label {
    font-size: 16px;
}

.p-inputtext{
  background-color: white;
}

.p-autocomplete{
  background-color: white;
}

.p-card {
    margin: 30px;
}


.p-divider {
    color:#EF7C00;
    background-color: black;
}
.p-card {
    padding: 30px;
    background-color: aliceblue;
}

</style>
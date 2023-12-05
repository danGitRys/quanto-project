<template>
    <div class="app">
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
                <small id="firstnamedescription">Enter First Name</small>
                <label for="lastname">Last Name:</label>
                <InputText
                    id="lastname"
                    type="text"
                    v-model="lastname"
                    placeholder="Last Name"
                    describedby="lastnamedescription"
                />
                <small id="lastnamedescription">Enter Last Name</small>
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
                    v-model="team" 
                    dropdown option-label="name" 
                    update:modelValue 
                    :suggestions="teams" 
                    placeholder="Teamname" 
                    @complete="getTeams" />
                <!-- <v-autocomplete v-model="team" id="ACTeam"
                    label="Select Team" :items="this.getTeams().name"
                    variant="solo-filled">
                </v-autocomplete> -->
            </div>
            <Divider />
            <div class="input-container-last">
                <label for="ACTeamrole">Teamrole:</label>
                <AutoComplete
                    v-model="teamrole"
                    :suggestions="teamroles"
                    placeholder="Teamrole"   
                    dropdown
                    update:modelValue 
                    @complete="getTeamRoles" />
                <v-autocomplete v-model="teamrole" id="ACTeamrole"
                    label="Select Role" :items="this.teamroles"
                    variant="solo-filled">
                </v-autocomplete>
            </div>         
        </div>
    </template>
    </Card>
    </div> 
    <footer>
        <div class="buttonContainer">
            <Button label="Submit" icon="pi pi-check" @click="submitEmployee"/>
            <!-- <v-btn @click="submitEmployee" class="submitBtn" variant="outlined">
                Submit
            </v-btn> -->
        </div>
    </footer>
</template>

<script>
import { teamroles } from '@/store/teamroles';
import { ref } from "vue";
import axios from 'axios';
import AutoComplete from 'primevue/autocomplete';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

export default {
    name: "addEmployee",
    components: {
        AutoComplete,
        InputText,
        Button,
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
            items: ['Apple', 'Banana', 'Orange', 'Mango', 'Pineapple'],
            selectedItem: null,
            filteredItems: [],
        }
    },
    methods: {
        async init() {
            await this.getTeams()
            await this.getTeamRoles()
        },
        async getTeams() {
            try {
                const response = await axios.get("http://localhost:8000/getTeams", {});
                this.teams = response.data.teams;
            } catch (error) {
                console.log(error);
            }
        },
        getTeamRoles() {
            this.teamroles = teamroles().role
            console.log(this.teamroles)
        },
        getTeamID() {
            for (let i = 0; i < this.teams.length; i++)
            if (this.team.name == this.teams[i].name) {
                this.teamid = this.teams[i].id
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
                        console.log("Employee created successfully.")
                    }
                    else{
                        alert("Creating new employee failed.")
                    }
                }).catch(error=> {
                    console.log(request)
                    alert("An error has occured.")
                })
            }
            else {
                alert("All fields must be filled in!")
            }
        },
        searchItems(event) {
            const query = event.query.toLowerCase();
            this.filteredItems = this.items.filter(item =>
            item.toLowerCase().includes(query)
      );
        }
    },
    created() {
        this.init()
    }
};

// 
// Add Employee Variables / Refs
// 
// var empid = ref('')
// var firstname = ref('');
// var lastname = ref('');
// var email = ref('');
// var phone = ref('');
// var team = ref('');
// var teamid = 0;
// var teamrole = ref('');
// var teams = ref([]);

// 
// Add Employee Functions
// 
// function getTeams() {
//     axios.get("http://localhost:8000/getTeams", {}).then(response => {
//             console.log(response)
//             teams = response.dataTable
//             if (responseData.success) {

//             }
            
//         }           
//     )
//     var teamid = 0;
//     return teamid;
// }

// function submitEmployee() {
//     // if an Employee is already working on the Project, give feedback

// }

// beforeMount() {
//         this.getTeams()
// }

</script>

<style scoped>

.input-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  padding: 10px 0;
}
.input-container-last {
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

.app {
  justify-content: center;
  display: flex;
  margin-left: 55px;
  height: 100%;
}

.buttonContainer {
    margin: 10px;
    width: 100%;
    display: flex;
    justify-content: flex-end;
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


div {
    margin-top: 50px;
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
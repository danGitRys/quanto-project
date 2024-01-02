<template>
    <div id="newProject">
    <Splitter style="height: 100%; width: 90%">
    <SplitterPanel class="flex align-items-center justify-content-center" style="min-width: 500px;">
        <ScrollPanel style="width: 100%; height: 100%">
            <Card>
                <template #title>Create Project</template>
                <template #content>

                    <h3 class="input-label">Project ID:</h3>
                    <InputGroup>
                        <InputGroupAddon>
                            <i class="pi pi-tag"></i>
                        </InputGroupAddon>
                        <InputText v-model="projectid" class="input-field small-input" type="text" placeholder="Enter Project ID"/>
                    </InputGroup>

                    <Divider />

                    <h3 class="input-label">Project Name:</h3>
                    <InputGroup>
                        <InputGroupAddon>
                            <i class="pi pi-book"></i>
                        </InputGroupAddon>
                        <InputText v-model="projectname" class="input-field small-input" type="text" placeholder="Enter Project Name"/>
                    </InputGroup>
                        
                    <Divider />

                    <h3 class="input-label">Customer Name:</h3>
                    <InputGroup>
                        <InputGroupAddon>
                            <i class="pi pi-building"></i>
                        </InputGroupAddon>
                        <InputText v-model="customername" class="input-field small-input" type="text"  placeholder="Enter Customer Name"/>
                    </InputGroup>

                    <Divider />

                    <h3 class="input-label">Project Start Date:</h3>
                    <InputGroup>
                        <InputGroupAddon>
                            <i class="pi pi-calendar-plus"></i>
                        </InputGroupAddon>
                            <InputText v-model="projectstart" class="input-field small-input" type="date"/>
                    </InputGroup>
                        
                    <Divider />

                    <h3 class="input-label">Project End Date:</h3>
                    <InputGroup>
                        <InputGroupAddon>
                            <i class="pi pi-calendar-times"></i>
                        </InputGroupAddon>
                        <InputText v-model="projectend" class="input-field small-input" type="date" />
                    </InputGroup>

                    <h3 class="input-label">Project Manager:</h3>
                    <InputGroup>
                        <InputGroupAddon>
                            <i class="pi pi-user"></i>
                        </InputGroupAddon>
                        <AutoComplete
                            id="ACProjectmanager"
                            v-model="projectmanager"
                            dropdown
                            :suggestions="employeeNames"
                            
                            update:modelValue 
                            placeholder="Select Projectmanager"   
                            @complete="getEmployeeNames" 
                        />
                    </InputGroup>
                        
                </template>
            </Card>
            <Card id="addEmployees">
                <template #title>Add Employees</template>
                <template #content>
                    <h3 class="input-label">Add Employee:</h3>
                    <InputGroup>
                        <InputGroupAddon>
                            <i class="pi pi-user"></i>
                        </InputGroupAddon>
                        <AutoComplete
                            id="ACEmployee"
                            v-model="selectedEmployee"
                            dropdown
                            :suggestions="employeeNames"
                            
                            update:modelValue 
                            placeholder="Select Employees"   
                            @complete="getEmployeeNames"
                            @item-select="appendEmployee" 
                        />
                    </InputGroup>

                    <Divider />

                </template>
            </Card>
            <Card id="Positions">
                <template #title> Add Positions</template>
                <template #content>

                    <h3 class="input-label">PositionID</h3>
                    <InputGroup>
                        <InputText id="pos" type="text" v-model="positionid" placeholder="Enter PositionID"/><br>
                    </InputGroup>
                    <h3 class="input-label">Positionname</h3>
                    <InputGroup>
                        <InputText id="pos" type="text" v-model="positionname" placeholder="Enter Positionname"/><br>
                    </InputGroup>
                    <h3 class="input-label">Positionrate</h3>
                    <InputGroup>
                        <InputText id="posrate" type="number" v-model="positionrate" placeholder="Enter Rate"/><br>
                    </InputGroup>
                    <h3 class="input-label">Number of Workdays</h3>
                    <InputGroup>
                        <InputText id="workdays" type="number" v-model="workdays" placeholder="Enter Workdays"/><br>
                    </InputGroup>
                    <h3 class="input-label">Automaticly create On-Site/Remote Position</h3>
                    <InputGroup>
                        <InputSwitch id="posSwitch" v-model="checked" />
                    </InputGroup>
                    <Button @click="createPosition" icon="pi pi-plus" label="Add Position" />
                </template>
          
            </Card>
        </ScrollPanel>
    </SplitterPanel>
    <SplitterPanel class="flex align-items-center justify-content-center" style="min-width: 900px;">
        <ScrollPanel style="width: 100%; height:100%">
            <div id="Employeetable" class="table-container">
                <DataTable ref="selectedEmployees" striped-rows removableSort
                    :value="selectedEmployees" :dataKey="selectedEmployees.id" 
                    :paginator="true" :rows="10"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[5,10,25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} selected Employes">
                    <template #header>
                        <div class="flex flex-wrap gap-2 align-items-center justify-content-between">
                            <h4 class="m-0">Selected Employees</h4>
                            <span class="p-input-icon-left">
                                <i class="pi pi-search" />
                                <InputText placeholder="Search..." />
                            </span>
                        </div>
                    </template>
                    <Column selectionMode="multiple" style="width: 3rem" :exportable="false"></Column>
                    <Column field="emp_id" header="EmployeeID" sortable style="min-width:12rem"></Column>
                    <Column field="forename" header="First Name" sortable style="min-width:12rem"></Column>
                    <Column field="surname" header="Last Name" sortable style="min-width:12rem"></Column>
                    <Column field="team" header="Team" sortable style="min-width:10rem"></Column>
                    <Column :exportable="false" style="min-width:8rem">
                        <template #body="slotProps">
                            <Button icon="pi pi-trash" outlined rounded severity="danger" @click="confirmDeleteEmployee(slotProps.data)" />
                        </template>
                    </Column>
                </DataTable>
            </div>

            <Dialog v-model:visible="deleteEmployeeDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
                    <div class="confirmation-content">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span v-if="employee">Are you sure you want to delete Mr./Mrs. <b>{{ employee.surname }}</b> from the selected Employees?</span>
                    </div>
                    <template #footer>
                        <Button label="No" icon="pi pi-times" text @click="closeDialog"/>
                        <Button label="Yes" icon="pi pi-check" text @click="deleteEmployee" />
                    </template>
            </Dialog>

            <div id="Positiontable" class="table-container">
                <DataTable ref="positions" striped-rows removableSort
                    :value="positions" dataKey="positonid" 
                    :paginator="true" :rows="10"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[5,10,25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} Project Positions">
                    <template #header>
                        <div class="flex flex-wrap gap-2 align-items-center justify-content-between">
                            <h4 class="m-0">Project Positions</h4>
                            <span class="p-input-icon-left">
                                <i class="pi pi-search" />
                                <InputText placeholder="Search..." />
                            </span>
                        </div>
                    </template>
                    <Column selectionMode="multiple" style="width: 3rem; min-height: 500px" :exportable="false"></Column>
                    <Column field="id" header="PositionID" sortable style="min-width:12rem; min-height: 500px;"></Column>
                    <Column field="name" header="Name" sortable style="min-width:12rem; min-height: 500px;"></Column>
                    <Column field="rate" header="Role" sortable style="min-width:10rem; min-height: 500px;"></Column>
                    <Column field="workdays" header="Workdays" sortable style="min-width:10rem; min-height: 500px;"></Column>
                    <Column :exportable="false" style="min-width:8rem">
                        <template #body="slotProps">
                            
                            <Button icon="pi pi-trash" outlined rounded severity="danger" @click="confirmDeletePosition(slotProps.data)" />
                        </template>
                    </Column>
                </DataTable>

                <Dialog v-model:visible="deletePositionDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
                    <div class="confirmation-content">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span v-if="position">Are you sure you want to delete Position \"<b>{{ position.name }}</b>\" from the Projects Positions?</span>
                    </div>
                    <template #footer>
                        <Button label="No" icon="pi pi-times" text @click="closeDialog"/>
                        <Button label="Yes" icon="pi pi-check" text @click="deletePosition" />
                    </template>
                </Dialog>
            </div>
        </ScrollPanel>
    </SplitterPanel>
    </Splitter>
    </div>
    <footer>
        <Button label="Submit" icon="pi pi-check" @click="createProject"/>
    </footer>
</template>



<script>
import InputText from 'primevue/inputtext';
import InputSwitch from 'primevue/inputswitch';
import ScrollPanel from 'primevue/scrollpanel';
import DataTable from 'primevue/datatable';
import Card from 'primevue/card';
import axios from 'axios'

class Position {
    id
    name
    rate
    workdays
    start_date
    end_date
    constructor(positionid, positionname, positionrate, workdays, start, end) {
        this.id = positionid
        this.name = positionname
        this.rate = positionrate
        this.workdays = workdays
        this.start_date = start
        this.end_date = end
    }
}

export default {
    name: "newProject",
    components: {
        InputText,
        InputSwitch,
        ScrollPanel,
        DataTable,
        Card,
    },
    data() {
        return {
            //General Information
            projectid: '',
            projectname: '',
            customername: '',
            projectstart: '',
            projectend: '',

            //Employees
            projectmanager: '',
            employees: [],
            employeeNames: [],
            selectedEmployee: '',
            selectedEmployees: [],

            //Positions
            positionid: '',
            positionname: '',
            positionrate: null,
            workdays: 1,
            checked: false, //true: add remote and on-site version automatically
            positions: [],

            // Event Handler / Dialog Variables
            employee: null,
            position: null,
            deleteEmployeeDialog: false,
            deletePositionDialog: false,

            // Event Handler
            confirmDeleteEmployee: (employee) => {
                this.employee = employee
                this.deleteEmployeeDialog = true
            },
            deleteEmployee: () => {
                var index = this.selectedEmployees.indexOf(this.employee)
                this.selectedEmployees.splice(index ,1)
                this.deleteEmployeeDialog = false
            },
            confirmDeletePosition: (position) => {
                this.position = position
                this.deletePositionDialog = true
            },
            deletePosition: () => {
                var index = this.positions.indexOf(this.position)
                this.positions.splice(index ,1)
                this.deletePositionDialog = false
            },
            closeDialog: () => {
                this.deleteEmployeeDialog = false
                this.deletePositionDialog = false
            },
        }
    },
    created() {
        this.init()
    },
    methods: {
        // Fetch data needed for the Form
        init() {
            this.getEmployees()
        },
        // Fetch list of all Employees from backend
        async getEmployees() {
            try {
                const response = await axios.get("http://localhost:8000/getAllEmployees", {})
                this.employees = response.data.employees
            } catch (error) {
                console.log(error)
            }
        },
        // Fetch list of all Full Names of employees from backend
        async getEmployeeNames() {
            try {
                const response = await axios.get("http://localhost:8000/getAllEmployeeNames", {})
                this.employeeNames = response.data.employeeNames
            } catch (error) {
                console.log(error)
            }
        },
        // Add selected Employee (Full Name) to array "selectedEmployees"
        appendEmployee() {
            // Append the Object of the Employee with the same Index as the selectedEmployee of the employeeNames Array
            // to the selectedEmployees Array if he/she is not in the Array already
            if (this.selectedEmployees.includes(this.employees[this.employeeNames.indexOf(this.selectedEmployee)])) {
                alert(this.selectedEmployee + " is already selected!")
            }
            else {
                this.selectedEmployees.push(this.employees[this.employeeNames.indexOf(this.selectedEmployee)])
            }
        },
        // Create new Object of Class Position with the values of the form and push to positions Array
        createPosition() {
            console.log("test")
            var pos = new Position(this.positionid, this.positionname, this.positionrate, this.workdays)
            console.log(pos)
            this.positions.push(pos)
        },
        async createProject() {
            // Create Timestamp for creation_date
            var today = new Date()
            var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate()
            const request = await axios.post("http://localhost:8000/createProject", {
                //General Information
                p_id: this.projectid,
                projectname: this.projectname,
                customername: this.customername,
                start_date: this.projectstart,
                end_date: this.projectend,
                creation_date: date.toString(),
                //Dummy data below
                fk_creator: 2,
                
            }).then(response => {
                console.log(response)
                if(response.data['success']==true){
                    console.log(response.data.message)
                    this.assignProjectManager(response.data.projectid)
                    this.assignEmployees(response.data.projectid)
                    this.assignPositions(response.data.projectid)
                }
                else {
                    console.log(response.data.error)
                }
            })
        },
        async assignProjectManager(projectid) {
            var assignProjectManager = await axios.post("http://localhost:8000/assignment", {
                "fk_project": projectid,
                "fk_employee": this.selectedEmployees[i].id,
                "role": "Member",
            }).then(response => {
                if(response.data['success']==true) {
                    console.log(response.data.message)
                }
                else {
                    console.log(response.data.error)
                }
            })
        },
        async assignEmployees(projectid) {
            var assignEmployee
            for (let i = 0; i < this.selectedEmployees.length; i++) {
                assignEmployee = await axios.post("http://localhost:8000/assignment", {
                    "fk_project": projectid,
                    "fk_employee": this.selectedEmployees[i].id,
                    "role": "Member",
                }).then(response => {
                    if(response.data['success']==true) {
                        console.log(response.data.message)
                    }
                    else {
                        console.log(response.data.error)
                    }
                })
            }
        },
        async assignPositions(projectid) {
            var assignPosition
            for (let i = 0; i < this.positions.length; i++) {
                assignPosition = await axios.post("http://localhost:8000/createPosition", {
                    "fk_project": projectid,
                    "position_id": this.positions[i].id + " " + this.positions[i].name,
                    "rate": this.positions[i].rate,
                    "wd": this.positions[i].workdays,
                    "start_date": this.projectstart,
                    "end_date": this.projectend,
                }).then(response => {
                    if(response.data['success']==true) {
                        console.log(response.data.message)
                    }
                    else {
                        console.log(response.data.error)
                    }
                })
            }
        },
    },
};
</script>


<style scoped>
/* Stil für kleinere Input-Felder */
#newProject {
  justify-content: center;
  display: flex;
  margin-left: 60px;
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
.table-container{
    margin: 15px;
    min-height: 500px;
}
.p-Splitter {
    width: 100%;
}

.input-label {
  text-align: left;
  margin-right: 20px;
}

.p-card {
    margin: 20px;
    padding: 30px;
    background-color: aliceblue;
}
.p-card-content {
    margin: 0px;
    padding: 0px;
}
.p-scrollpanel {
    padding: 20px;
}
</style>

<template>
  <div class="card">
    <DataTable :value="projects" paginator :rows="10" dataKey="id">
      <template #empty>No projects found.</template>

      <Column field="project_id" header="Project ID" sortable style="min-width: 10rem"></Column>
      <Column field="project_company" header="Company" sortable style="min-width: 14rem"></Column>
      <Column field="project_name" header="Project Name" sortable style="min-width: 14rem"></Column>
      <Column field="project_company" header="Company" sortable style="min-width: 14rem"></Column>
      <!-- Add more columns as needed -->
      <!-- For example, you can add columns for other project attributes -->
      <!-- <Column field="attributeName" header="Attribute Name" sortable style="min-width: 14rem"></Column> -->
    </DataTable>
  </div>
</template>

<style scoped>
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 50px 10%;
  padding: 30px;
}

.custom-search-input {
  position: relative;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
}

.custom-search-input input {
  box-sizing: border-box;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding-left: 30px;
}

.custom-search-input .pi-search {
  position: absolute;
  left: 50px;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
  font-size: 16px;
}

.custom-search-input .p-inputtext {
  padding-left: 25px;
  padding-right: 25px;
}
</style>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import Calendar from 'primevue/calendar';
import InputNumber from 'primevue/inputnumber';
import Dropdown from 'primevue/dropdown';
import Tag from 'primevue/tag';

export default {

  data() {
    return {
      projects: []
    }
  },
  methods: {

    getProjects() {
      console.log("test")
      axios.get("http://localhost:8000/getProjectsForEmployee/" + this.$route.params.id, {

      }).then(response => {
      
        var responseData = response.data
        var valid = responseData.success
        if (valid == true) {
          var tempData = responseData.data
          console.log(tempData)

          for(var i=0;i<tempData.length;i++){
                    var tempProject = tempData[i]
                    this.projects.push(tempProject)
                   

                    }
                    

        }
        else {
          alert("This Team doesnt exist")
        }


      })
        .catch(error => {
          console.log(error)

        })
    },
    



  },
  beforeMount() {
      this.getProjects()
      console.log("Called")

    }


}




</script>

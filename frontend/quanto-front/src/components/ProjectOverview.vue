<template>
  <div class="card">
    <div class="custom-search-input">
      <InputText v-model="globalFilter" placeholder="Search..." />
    </div>
      <!-- DataTable-Komponente mit verschiedenen Spalten -->
    <DataTable
      :value="projects"
      paginator
      :rows="10"
      dataKey="id"
      :globalFilter="globalFilter"
    >
     <!-- Benutzerdefinierte Anzeige, wenn keine Projekte gefunden werden -->
      <template #empty>No projects found.</template>

      <!-- Definition von Spalten mit verschiedenen Feldern und Überschriften -->
      <Column
        field="project_id"
        header="ID"
        sortable
        style="min-width: 10rem"
      ></Column>
      <Column
        field="project_pid"
        header="Project ID"
        sortable
        style="min-width: 14rem"
      ></Column>
      <Column
        field="project_name"
        header="Project Name"
        sortable
        style="min-width: 14rem"
      ></Column>
      <Column
        field="project_company"
        header="Company"
        sortable
        style="min-width: 14rem"
      ></Column>
      <Column
        field="assignment_role"
        header="Role"
        sortable
        style="min-width: 14rem"
      ></Column>
      <Column
        field="project_start_date"
        header="Start Date"
        sortable
        style="min-width: 14rem"
      ></Column>
      <Column
        field="project_end_date"
        header="End Date"
        sortable
        style="min-width: 14rem"
      ></Column>
    </DataTable>
  </div>
</template>

<style>
/* Stildefinitionen für die Komponente */
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 50px 10%;
  padding: 30px;
}

.custom-search-input {
  margin-bottom: 20px;
}

.custom-search-input input {
  box-sizing: border-box;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
}

/* Stildefinitionen für die DataTable-Elemente */
.p-datatable-thead th {
  background-color: #f2f2f2; /* Light gray background for headers */
  padding: 10px;
  text-align: left;
}

.p-datatable-tbody tr {
  font-family: "Arial", sans-serif; /* Change the font for entries */
  color: #333; /* Change the text color for entries */
}

.p-datatable-tbody td {
  padding: 10px;
}
</style>

<script>
// Importieren von benötigten Bibliotheken und Komponenten
import axios from "axios";
import { ref, onMounted } from "vue";
import { FilterMatchMode, FilterOperator } from "primevue/api";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import InputText from "primevue/inputtext";
import Calendar from "primevue/calendar";
import InputNumber from "primevue/inputnumber";
import Dropdown from "primevue/dropdown";
import Tag from "primevue/tag";

export default {
  data() {
    // Datenoption für die Projekte
    return {
      projects: [],
    };
  },
  methods: {
     // Methode zum Abrufen von Projektdaten über eine API-Anfrage
    getProjects() {
      console.log("test");
      axios
        .get(
          "http://localhost:8000/getProjectsForEmployee/" +
            this.$route.params.id,
          {}
        )
        .then((response) => {
          var responseData = response.data;
          var valid = responseData.success;
          if (valid == true) {
            var tempData = responseData.data;
            console.log(tempData);

            // Iteration durch die erhaltenen Projektdaten und Hinzufügen zu 'projects'
            for (var i = 0; i < tempData.length; i++) {
              var tempProject = tempData[i];
              this.projects.push(tempProject);
            }
          } else {
            alert("This Team doesnt exist");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  // Hook vor dem Mounten der Komponente, um Projektdaten zu laden
  beforeMount() {
    this.getProjects();
    console.log("Called");
  },
};
</script>

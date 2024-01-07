<template>
  <div class="card">
    <div class="search-input">
      <input v-model="globalFilter" placeholder="Search..." />
    </div>
    <table>
      <thead>
        <tr>
          <th @click="sortProjects('project_id')" class="fixed-width">ID {{ getSortIcon('project_id') }}</th>
          <th @click="sortProjects('project_pid')" class="fixed-width">Project ID {{ getSortIcon('project_pid') }}</th>
          <th @click="sortProjects('project_name')" class="fixed-width">Project Name {{ getSortIcon('project_name') }}</th>
          <th @click="sortProjects('project_company')" class="fixed-width">Company {{ getSortIcon('project_company') }}</th>
          <th @click="sortProjects('assignment_role')" class="fixed-width">Role {{ getSortIcon('assignment_role') }}</th>
          <th @click="sortProjects('project_start_date')" class="fixed-width">Start Date {{ getSortIcon('project_start_date') }}</th>
          <th @click="sortProjects('project_end_date')" class="fixed-width">End Date {{ getSortIcon('project_end_date') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="project in projects" :key="project.id">
          <td>{{ project.project_id }}</td>
          <td>{{ project.project_pid }}</td>
          <td @click="test(project)">{{ project.project_name }}</td>
          <td>{{ project.project_company }}</td>
          <td>{{ project.assignment_role }}</td>
          <td>{{ project.project_start_date }}</td>
          <td>{{ project.project_end_date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style>
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 50px auto;
  padding: 30px;
  width: 80%;
}

.search-input {
  margin-bottom: 20px;
  text-align: center;
}

.search-input input {
  box-sizing: border-box;
  width: 60%;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 8px;
  text-align: left;
  cursor: pointer;
  position: relative;
}

th.fixed-width {
  background-color: #f2f2f2;
  width: 150px; /* Feste Breite für die Spalten */
  transition: none; /* Übergang bei Hover entfernen */
}

th:hover {
  background-color: #f2f2f2; /* Farbe beim Hover beibehalten */
}

th:last-child, td:last-child {
  padding-right: 0;
}

.sort-icon {
  position: absolute;
  top: 8px;
  right: 8px;
  visibility: visible;
}
</style>

<script>
import axios from "axios";
import { useUser } from '@/store/user';
import {projectId} from '@/store/projectId';
export default {
  data() {
    return {
      projects: [],
      globalFilter: "",
      sortKey: "",
      sortOrder: 1,
    };
  },
  methods: {
    test(project) {
      projectId().setProjectId(project.project_id);
      console.log(projectId().getProjectId());
      window.location.href = '/timeRegistration';
      
    },
    getProjects() {
      var User = useUser()
      var userId = User.getUserData.id
      axios
        .get(
          "http://localhost:8000/getProjectsForEmployee/" + userId,
          {}
        )
        .then((response) => {
          console.log(response)
          var responseData = response.data;
          var valid = responseData.success;
          if (valid == true) {
            this.projects = responseData.data;
          } else {
            alert("This Team doesn't exist");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    sortProjects(key) {
      if (this.sortKey === key) {
        this.sortOrder *= -1;
      } else {
        this.sortKey = key;
        this.sortOrder = 1;
      }

      this.projects.sort((a, b) => {
        const modifier = this.sortOrder === 1 ? 1 : -1;
        if (a[key] < b[key]) return -1 * modifier;
        if (a[key] > b[key]) return 1 * modifier;
        return 0;
      });
    },
    getSortIcon(column) {
      if (this.sortKey === column) {
        return this.sortOrder === 1 ? '↓' : '↑';
      }
      return '';
    },
  },
  
  mounted() {
    this.getProjects();
  },
};
</script>

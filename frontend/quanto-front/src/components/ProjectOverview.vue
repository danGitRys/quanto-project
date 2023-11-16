<template>
  <div class="container">
    <div class="header">
      <h1 class="header-title">Projects</h1>
      <input v-model="searchQuery" class="search-input" placeholder="Search">

    </div>

    <v-date-table :items="projects"></v-date-table>


  <!--   <table class="project-table">
      <thead>
        <tr>
          <th>NAME</th>
          <th>LEADER Quanto </th>
          <th>PROJECT END</th>
          <th>ROLE</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="project of projects">
          <td>
            <span>{{ project.title }}</span>
          </td>
          <td>
            <span>{{ project.leader }}</span>
          </td>

          <td>
            <strong>{{ project.endDate }}</strong>
          </td>

          <td>
            <strong>{{ project.role }}</strong>
          </td>
        </tr>
        <tr>

          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>

         <tr>
          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>

        <tr>
          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>

        <tr>
          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>

        <tr>
          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>

        <tr>
          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>

        <tr>
          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>

        <tr>
          <td><span>Extra small</span></td>
          <td><strong>xs</strong></td>
          <td><strong>xs</strong></td>
          <td>600</td>
        </tr>
      </tbody>
    </table> -->




   <div class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">Previous</button>
      <span>{{ currentPage }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
      <span v-if="currentPage < totalPages" class="next-pages">
        ... {{ currentPage + 1 }} {{ currentPage + 2 }} {{ currentPage + 3 }} ...
      </span>

    </div>
 </div>
</template>





<style scoped>

.container {
  background-color: lightgray;
  border-radius: 10px;
  padding: 20px;
  margin-top: 100px;
  margin-bottom: 100px;
  margin-left: 100px;
  margin-right: 100px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 2px solid #ccc;
}

.header-title {
  font-size: 24px;
  color: #0056b3;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.project-table {
  width: 100%;
  border-collapse: collapse;
}

thead tr {
  background-color: #f0f0f0;
}

th {
  padding: 10px 20px;
  text-align: left;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

td {
  padding: 10px 20px;
}

span {
  font-size: 14px;
  color: #333;
}

strong {
  font-weight: bold;
  color: #0056b3;
}

.search-input {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  outline: none;
  font-size: 14px;
  width: 200px;
}

.pagination{
  display: flex;
  justify-content: center;

  margin-top: 10px;
  margin-right: 10px;
  text-align: center;
}

.pagination button {
  padding: 10px 20px;
  background-color: #0056b3;
  color: white;
  border: none;
  border-radius: 5px;
  margin: 0 10px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.pagination span {
  font-size: 16px;
  margin: 0 10px;
}

.next-pages {
  font-size: 16px;
  color: #0056b3;
}

</style>

<script setup>
  import { VDataTable } from 'vuetify/labs/VDataTable';
</script>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      currentPage: 1,
      totalPages: 3,
      projects:[
        {
          title: "Projekt A",
          leader: "Chris",
          endDate: "14.11.23",
          role:"SD"
        },
        {
          title: "Projekt B",
          leader: "Michele",
          endDate: "15.11.23"
        },
        {
          title: "Projekt c",
          endDate: "16.11.23"
        }

      ]
    };
  },

 methods: {
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
  },


};

</script>


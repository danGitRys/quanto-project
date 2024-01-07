<template>
    <div>
        <!-- Wähle den Index dynamisch aus (z.B. pep[1]) und übergebe ihn an InnerTable2 -->
        <InnerTable2 :people="pep" :selectedPersonIndex="0" />
    </div>
    <div>
            <InnerTable2 :people="pep" :selectedPersonIndex="1" />

        </div>

     <div v-for="(person, index) in pep" :key="index">
          <InnerTable2 :people="pep" :selectedPersonIndex="index" />
        </div>
      
</template>

<script setup>
import { ref } from 'vue';
import InnerTable2 from './InnerTable2.vue';
import axios from 'axios';
const pep = ref([
    { name: 'Chris', age: 13, city: 'Canstatt' },
    { name: 'Kai', age: 25, city: 'xxx' },
    {name: 'Felix', age: 54, city: 'xfafx'},
    {name: 'Basti', age: 15, city: 'xfafx'}
]);


getPeople();

async function getPeople() {
    const url = 'http://localhost:8000/getProjectsWhereProjectLeader/3007'
    const response = await axios.get(url);
    console.log(response.data.projects);
    const data = response.data.projects;
    console.log(data);
    data.forEach(element => {
        pep.value.push({name: element.projectNames, age:12,city:"hellp"})
    });
  
}


</script>

<template>
  <div>
    <DataTable :value="data" tableStyle="min-width: 10rem">
      <Column field="code" header="Montag">
        <template #body="slotProps">
          {{ console.log(slotProps) }}
          <template v-if="slotProps.index < monday.length">
            <InnerTable3 :people="monday[slotProps.index]" />
          </template>
        </template>
      </Column>
      </DataTable>
  </div>
</template>



<script setup>
import { ref } from 'vue';

import InnerTable3 from './InnerTable3.vue';


const monday = [
  { planned: '8', working: '8', break: '0', sum: '8', quantity: 1 },
  { planned: '2', working: '0', break: '1', sum: '7',  quantity: 15 },
  { planned: '1177', working: '28', break: '0', sum: '899' },
   { planned: '151', working: '15', break: '0', sum: '899' },
];

const tuesday = [
  { planned: '2444', working: '888', break: '111', sum: '22222' },
   { planned: '2444', working: '999', break: '111', sum: '22222' },
  // other Tuesday data...
];
const data = ref([...monday, ...tuesday]);


</script>

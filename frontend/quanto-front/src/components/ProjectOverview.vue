<template>
  <div class="card">
    <DataTable
      v-model:filters="filters"
      v-model:selection="selectedCustomers"
      :value="customers"
      paginator
      :rows="10"
      dataKey="id"
      filterDisplay="menu"
      :globalFilterFields="['projects']"
    >
      <template #header>
        <div class="flex justify-content-center mb-2">
          <span class="custom-search-input p-input-icon-left">
            <i class="pi pi-search" />
            <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
          </span>
        </div>
      </template>
      <template #empty>No customers found.</template>

      <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>

      <Column field="id" header="Project ID" sortable style="min-width: 10rem">
        <template #body="{ data }">{{ data.id }}</template>
      </Column>

      <Column field="projects" header="Project Name" sortable style="min-width: 14rem">
        <template #body="{ data }">{{ data.projects }}</template>
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by projects" />
        </template>
      </Column>

      <Column field="company" header="Company" sortable style="min-width: 14rem">
        <template #body="{ data }">{{ data.company }}</template>
      </Column>

      <Column field="start_date" header="Start Date" sortable style="min-width: 10rem">
        <template #body="{ data }">{{ formatDate(data.start_date) }}</template>
        <template #filter="{ filterModel }">
          <Calendar v-model="filterModel.value" dateFormat="mm/dd/yy" placeholder="mm/dd/yyyy" mask="99/99/9999" />
        </template>
      </Column>

      <Column field="end_date" header="End Date" sortable style="min-width: 10rem">
        <template #body="{ data }">{{ formatDate(data.end_date) }}</template>
        <template #filter="{ filterModel }">
          <Calendar v-model="filterModel.value" dateFormat="mm/dd/yy" placeholder="mm/dd/yyyy" mask="99/99/9999" />
        </template>
      </Column>

      <Column field="balance" header="Balance" sortable style="min-width: 10rem">
        <template #body="{ data }">{{ formatCurrency(data.balance) }}</template>
        <template #filter="{ filterModel }">
          <InputNumber v-model="filterModel.value" mode="currency" currency="USD" locale="en-US" />
        </template>
      </Column>

      <Column field="status" header="Status" sortable style="min-width: 12rem">
        <template #body="{ data }">
          <Tag :value="data.status" :severity="getSeverity(data.status)" />
        </template>
        <template #filter="{ filterModel }">
          <Dropdown v-model="filterModel.value" :options="statuses" placeholder="Select One" class="p-column-filter" showClear>
            <template #option="slotProps">
              <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
            </template>
          </Dropdown>
        </template>
      </Column>
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

<script setup>
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

const customers = ref();
const selectedCustomers = ref();
const filters = ref();
const statuses = ref(['unqualified', 'qualified', 'new', 'negotiation', 'renewal', 'proposal']);

onMounted(() => {
  loadProjects();
});

const initFilters = () => {
  filters.value = {
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    projects: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
  };
};

initFilters();

const formatDate = (value) => {
  return value.toLocaleDateString('en-US', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  });
};

const formatCurrency = (value) => {
  return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};

const getSeverity = (status) => {
  switch (status) {
    case 'unqualified':
      return 'danger';

    case 'qualified':
      return 'success';

    case 'new':
      return 'info';

    case 'negotiation':
      return 'warning';

    case 'renewal':
      return null;
  }
};

const loadProjects = async () => {
  await loadProjectsForEmployee(1);
};

const loadProjectsForEmployee = async (employeeId) => {
  try {
    const response = await axios.get(`http://localhost:8000/getProjectsForEmployee/${employeeId}`);
    console.log('Projekte für Mitarbeiter geladen:', response.data);
  } catch (error) {
    console.error('Fehler beim Laden der Projekte für Mitarbeiter', error);
  }
};
</script>

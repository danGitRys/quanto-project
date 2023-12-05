
<template>
  <div class="card">
      <DataTable v-model:filters="filters" v-model:selection="selectedCustomer" :value="customers"
              stateStorage="session" stateKey="dt-state-demo-session" paginator :rows="5" filterDisplay="menu"
              selectionMode="single" dataKey="id" :globalFilterFields="['name', 'country.name', 'representative.name', 'status']" tableStyle="min-width: 50rem">
          <template #header>
              <span class="p-input-icon-left">
                  <i class="pi pi-search" />
                  <InputText v-model="filters['global'].value" placeholder="Global Search" />
              </span>
          </template>
          <Column field="name" header="Name" sortable style="width: 25%">
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by name" />
              </template>
          </Column>
          <Column header="Country" sortable sortField="country.name" filterField="country.name" filterMatchMode="contains" style="width: 25%">
              <template #body="{ data }">
                  <div class="flex align-items-center gap-2">
                      <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${data.country.code}`" style="width: 24px" />
                      <span>{{ data.country.name }}</span>
                  </div>
              </template>
              <template #filter="{ filterModel }">
                  <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by country" />
              </template>
          </Column>
          <Column header="Representative" sortable sortField="representative.name" filterField="representative" :showFilterMatchModes="false" :filterMenuStyle="{ width: '14rem' }" style="width: 25%">
              <template #body="{ data }">
                  <div class="flex align-items-center gap-2">
                      <img :alt="data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${data.representative.image}`" style="width: 32px" />
                      <span>{{ data.representative.name }}</span>
                  </div>
              </template>
              <template #filter="{ filterModel }">
                  <MultiSelect v-model="filterModel.value" :options="representatives" optionLabel="name" placeholder="Any" class="p-column-filter">
                      <template #option="slotProps">
                          <div class="flex align-items-center gap-2">
                              <img :alt="slotProps.option.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.option.image}`" style="width: 32px" />
                              <span>{{ slotProps.option.name }}</span>
                          </div>
                      </template>
                  </MultiSelect>
              </template>
          </Column>
          <Column field="status" header="Status" sortable filterMatchMode="equals" style="width: 25%">
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
          <template #empty> No customers found. </template>
      </DataTable>
  </div>
</template>

<script>
//import { CustomerService } from '@/service/CustomerService';
import { FilterMatchMode, FilterOperator } from 'primevue/api';

export default {
  data() {
      return {
          customers: null,
          selectedCustomer: null,
          filters: null,
          representatives: [
              { name: 'Amy Elsner', image: 'amyelsner.png' },
              { name: 'Anna Fali', image: 'annafali.png' },
              { name: 'Asiya Javayant', image: 'asiyajavayant.png' },
              { name: 'Bernardo Dominic', image: 'bernardodominic.png' },
              { name: 'Elwin Sharvill', image: 'elwinsharvill.png' },
              { name: 'Ioni Bowcher', image: 'ionibowcher.png' },
              { name: 'Ivan Magalhaes', image: 'ivanmagalhaes.png' },
              { name: 'Onyama Limba', image: 'onyamalimba.png' },
              { name: 'Stephen Shaw', image: 'stephenshaw.png' },
              { name: 'XuXue Feng', image: 'xuxuefeng.png' }
          ],
          statuses: ['unqualified', 'qualified', 'new', 'negotiation', 'renewal', 'proposal']
      };
  },
  created() {
      this.initFilters();
  },
  mounted() {
      CustomerService.getCustomersSmall().then((data) => (this.customers = data));
  },
  methods: {
      initFilters() {
          this.filters = {
              global: { value: null, matchMode: FilterMatchMode.CONTAINS },
              name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
              'country.name': { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
              representative: { value: null, matchMode: FilterMatchMode.IN },
              status: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] }
          };
      },
      getSeverity(status) {
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
      }
  }
};
</script>

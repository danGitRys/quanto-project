/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";
import router from "@/router";
import PrimeVue from 'primevue/config'
// Plugins
import { registerPlugins } from "@/plugins";

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import MultiSelect from 'primevue/multiselect';
import Dropdown from 'primevue/dropdown';
import Tag from 'primevue/tag';

const app = createApp(App);

registerPlugins(app);
app.use(PrimeVue);
app.component('DataTable',DataTable)
app.component('Column',Column)
app.component('InputText', InputText);
app.component('MultiSelect', MultiSelect);
app.component('Dropdown', Dropdown);
app.component('Tag', Tag);

app.use(router).mount("#app");

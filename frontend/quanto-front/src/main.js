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

const app = createApp(App);

registerPlugins(app);
app.use(PrimeVue);
app.component('DataTable', DataTable)
app.component('Column', Column)
app.use(router).mount("#app");

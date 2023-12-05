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
import 'primeicons/primeicons.css'
import './assets/app.css'

// Plugins
import { registerPlugins } from "@/plugins";

// Primevue Components
import InputText from 'primevue/inputtext';
import AutoComplete from 'primevue/autocomplete';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Divider from 'primevue/divider';
import Card from 'primevue/card';

const app = createApp(App);

app.use(PrimeVue);
app.use(router).mount("#app");
registerPlugins(app);
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('InputText', InputText)
app.component('AutoComplete', AutoComplete)
app.component('Button', Button)
app.component('Divider', Divider)
app.component('Card', Card)


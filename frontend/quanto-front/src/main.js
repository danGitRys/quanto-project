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
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import AutoComplete from 'primevue/autocomplete';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Divider from 'primevue/divider';
import Card from 'primevue/card';
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';
import Dialog from 'primevue/dialog';

const app = createApp(App);

app.use(PrimeVue);
app.use(router)
registerPlugins(app);
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('InputText', InputText)
app.component('AutoComplete', AutoComplete)
app.component('Button', Button)
app.component('Divider', Divider)
app.component('Card', Card)
app.component('Splitter', Splitter)
app.component('SplitterPanel', SplitterPanel)
app.component('InputGroup', InputGroup)
app.component('InputGroupAddon', InputGroupAddon)
app.component('Dialog', Dialog)
app.mount("#app");


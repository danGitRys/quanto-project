<template>
    <div class="container">
    <div class="card flex justify-content-flex-start">
        <Sidebar v-model:visible="visible">
            <template #container="{ closeCallback }">
                <div class="flex flex-column h-full">
                    <div class="flex align-items-baseline justify-content-between px-4 pt-3 flex-shrink-0">
                        <span class="inline-flex align-items-center gap-2">
                            <svg width="200" height="46" viewBox="0 0 200 46" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                            <rect width="200" height="45.6284" fill="url(#pattern0)"/>
                            <defs>
                            <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
                            <use xlink:href="#image0_2418_1582" transform="scale(0.000455373 0.00199601)"/>
                            </pattern>
                            <image id="image0_2418_1582" width="2196" height="501" xlink:href="..\icons\QuantoLogo.svg"/>
                            </defs>
                            </svg>
                        </span>
                        <span>
                            <Button type="button" @click="closeCallback" icon="pi pi-times" rounded outlined class="h-2rem w-2rem"></Button>
                        </span>
                    </div>
                    <div class="overflow-y-auto">
                        <ul class="list-none p-3 m-0">
                            <li>
                                <ul class="list-none p-0 m-0 overflow-hidden">
                                    <router-link to="/" v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                                    <i class="pi pi-home mr-2"></i>
                                    <span class="font-medium">Dashboard</span>
                                    </router-link>
                                    <li v-if="isAdmin || isProjectManager">
                                        <router-link to="/workingTimes+" v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                                            <i class="pi pi-calendar mr-2"></i>
                                            <span class="font-medium">Working Times +</span>
                                        </router-link>
                                    </li>
                                    <li v-else>
                                        <router-link to="/workingTimes" v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                                            <i class="pi pi-calendar mr-2"></i>
                                            <span class="font-medium">Working Times</span>
                                        </router-link>
                                    </li>
                                    <li v-if="isAdmin">
                                        <router-link to="/newproject" v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                                            <i class="pi pi-plus-circle mr-2"></i>
                                            <span class="font-medium">New Project</span>
                                        </router-link>
                                    </li>
                                    <li v-if="isAdmin || isProjectManager">
                                        <router-link to="/ManageProject" v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                                            <i class="pi pi-book mr-2"></i>
                                            <span class="font-medium">Manage Project</span>
                                        </router-link>
                                    </li>
                                    <li>
                                        <router-link to="/timeRegistration" v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                                            <i class="pi pi-clock mr-2"></i>
                                            <span class="font-medium">Time Registration</span>
                                        </router-link>
                                    </li>
                                    <li>
                                        <router-link to="/settings" v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                                            <i class="pi pi-cog mr-2"></i>
                                            <span class="font-medium">Settings</span>
                                        </router-link>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                    <div class="mt-auto">
                        <hr class="mb-3 mx-3 border-top-1 border-none surface-border" />
                        <a v-ripple class="m-3 flex align-items-center cursor-pointer p-3 gap-2 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                            <!-- <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" /> -->
                            <span class="font-bold">{{ forename }} {{ surname }}</span>
                        </a>
                    </div>
                    <div v-ripple class="logoutStyle m-3 flex align-items-center cursor-pointer gap-2 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                        <button @click="logout" class="logoutBtn pi pi-sign-out">  Logout</button>
                    </div>
                </div>
            </template>
        </Sidebar>
        <Button icon="pi pi-bars" @click="visible = true" />
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {AuthService} from '@/service/login.js'
import axios from "axios";
import Sidebar from 'primevue/sidebar';
import Avatar from "primevue/avatar";
import Button from 'primevue/button';
import "primeflex/primeflex.css";
import "primevue/resources/themes/lara-light-green/theme.css";
import "primeicons/primeicons.css";

const visible = ref(false);

let forename = '';
let surname = '';

let isAdmin = false;
let isProjectManager = false;

let token = localStorage.getItem('token');


// Überprüfen, ob der Local Storage-Wert vorhanden ist
if (token) {
    console.log('Daten aus dem Local Storage:', token);
} else {
    console.log('Keine Daten im Local Storage gefunden.');
}

onMounted(() => {
    getRole();
  });

  const getRole = async () => {
    try {
        axios.post("http://localhost:8000/getRole",{
            token:token
        }).then(response => {
            console.log(response)
            const role = response.data.employee.company_role;
            isAdmin = role === "Admin";
            isProjectManager = role === "Project_Manager";

            forename = response.data.employee.forename;
            surname = response.data.employee.surname;
        })
        .catch(error=> {
            console.log(error)
        })
    } catch (error) {
        console.error(error);
    }
  };

  const logout = () => {
    console.log("Logout");
    localStorage.clear();
    window.location.href = '/login';
  }
</script>

<style scoped>
/* * {
    box-sizing: border-box;
} */

.logoutStyle {
    background-color: #94B8C7;
    border-radius: 8px;
    border: none;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;

}

.logoutBtn {
    width: 100%;
    height: 100%;
}
</style>
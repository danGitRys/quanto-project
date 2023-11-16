// Composables
import { createRouter, createWebHistory } from "vue-router";
import LoginScreen from "@/views/LoginScreen.vue";

import NewProject from "@/views/NewProject.vue";

import TimeRegistration from "@/views/TimeRegistration.vue";
import LandingPage from "@/views/LandingPage.vue";
import AddEmployee from "@/views/AddEmployee.vue";
import dataTable from "@/components/DataTable.vue"

const routes = [
  {
    path: "/ff",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Home",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Home.vue"),
      },
    ],
  },

  {
    path: "/",
    name: "Login",
    component: LoginScreen,
  },

  {


  

    path: "/projectOverview",

    name: "ProjectOverview",
    component: LandingPage,
  },

  {
    path: "/newproject",
    name: "NewProject",
    component: NewProject,




  },
  {

    path: "/timeRegistration",
    name: "TimeRegistration",
    component: TimeRegistration,
  },

  {
    path: "/addEmployee",
    name: "AddEmployee",
    component: AddEmployee,
  },

  {
    path: "/dataTable",
    name: "dataTable",
    component: dataTable,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

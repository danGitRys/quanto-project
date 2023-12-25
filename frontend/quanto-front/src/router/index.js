// Composables
import { createRouter, createWebHistory } from "vue-router";
import LoginScreen from "@/views/LoginScreen.vue";

import NewProject from "@/views/NewProject.vue";
import Home from "@/views/Home.vue";
import TimeRegistration from "@/views/TimeRegistration.vue";
import LandingPage from "@/views/LandingPage.vue";
import AddEmployee from "@/views/AddEmployee.vue";



import getTeam from "@/components/demo/getTeamComponent.vue"
import ManageProject from "@/views/ManageProject.vue";

import singleProject from "@/components/SingleProject.vue";

import dataTable from "@/components/DataTable.vue";



import TimeCorrection from "@/views/TimeCorrection.vue";
import positionDemoGraph from "@/components/graphs/PositionDemoGraph.vue";
//import positionLinearDemoGraph from "@/components/graphs/positionLinearDemoGraph.vue";
import positionLinearGraph from "@/components/graphs/PositionLinearGraph";
import projectPositonsLinearGraph from "@/components/graphs/ProjectPositionLinearGraph.vue"
import projectionGraph from "@/components/graphs/PositionProjectionGraph.vue"



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

    path: "/Home",
    name: "Home",
    component: Home,
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
    name: "Time Registration",
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

  {
    path: "/ManageProject",
    name: "ManageProject",
    component: ManageProject,
  },

  {
    path: "/getTeam/:id",
    name: "getTeam",
    component: getTeam,
  },
  {
    path: "/project/:id",
    name: "project",
    component: singleProject,
  },


  {
    path: "/TimeCorrection",
    name: "TimeCorrection",
    component: TimeCorrection,
  },

  {
    path: "/positionDemoGraph/:id",
    name: "positionDemoGraph",
    component: positionDemoGraph,
  },

  {
    path: "/positionLinearDemoGraph/:id",
    name: "positionLinearDemoGraph",
    component: positionLinearGraph,
  },
  {
    path: "/projectPositionsLinearGraph/:id",
    name: "projectPositionLinearDemoGraph",
    component: projectPositonsLinearGraph,
  },
  {
    path: "/projectionGraph/:id",
    name: "projectionGraph",
    component:projectionGraph,
  },


];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

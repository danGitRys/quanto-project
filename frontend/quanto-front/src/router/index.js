// Composables
import { createRouter, createWebHistory } from "vue-router";
// import pinia from "@/store";


import LoginScreen from "@/views/LoginScreen.vue";
import NewProject from "@/views/NewProject.vue";
import Home from "@/views/Home.vue";
import TimeRegistration from "@/views/TimeRegistration.vue";
import LandingPage from "@/views/LandingPage.vue";
import AddEmployee from "@/views/AddEmployee.vue";
import getTeam from "@/components/demo/getTeamComponent.vue"
import ManageProject from "@/views/ManageProject.vue";
import singleProject from "@/components/SingleProject.vue"
import dataTable from "@/components/DataTable.vue";
import TimeCorrection from "@/views/TimeCorrection.vue";
import { useUser } from "@/store/user";


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
    path: "/login",
    name: "Login",
    component: LoginScreen,
  },
  {

    path: "/Home",
    name: "Home",
    component: Home,
  },

  {

    path: "/",
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
    meta: { requiresAuth: true }
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


];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});



router.beforeEach((to, from, next) => {
  
  const User = useUser()
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!User.isLoggedIn) {
      next('/login') // Redirect to login if not authenticated
      // next()
    } else {
      next()
    }
  } else {
    if (User.userData){
      
    }
    next();
  }
});

export default router;

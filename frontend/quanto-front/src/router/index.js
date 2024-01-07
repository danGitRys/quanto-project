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

import singleProject from "@/views/SingleProject.vue";

import dataTable from "@/components/DataTable.vue";
import TimeCorrection from "@/views/TimeCorrection.vue";

import WorkingTimesView from "@/views/WorkingTimesView.vue"
import InnerTables from "@/components/InnerTables.vue"

import positionDemoGraph from "@/components/graphs/PositionDemoGraph.vue";
//import positionLinearDemoGraph from "@/components/graphs/positionLinearDemoGraph.vue";
import positionLinearGraph from "@/components/graphs/PositionLinearGraph";
import projectPositonsLinearGraph from "@/components/graphs/ProjectPositionLinearGraph.vue"
import projectionGraph from "@/components/graphs/PositionProjectionGraph.vue"
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
    meta: { requiresAuth: true },
  },

  {

    path: "/",
    name: "ProjectOverview",
    component: LandingPage,
    meta: { requiresAuth: true },
  },

  {
    path: "/newproject",
    name: "Create New Project",
    component: NewProject,
    meta: { requiresAuth: true, roles: ['Admin']},
  },
  {
    path: "/timeRegistration",
    name: "Time Registration",
    component: TimeRegistration,
    meta: { requiresAuth: true },
  },
  {
    path: "/addEmployee",
    name: "Add Employee",
    component: AddEmployee,
    meta: { requiresAuth: true, roles: ['Admin']},
  },

  {
    path: "/dataTable",
    name: "dataTable",
    component: dataTable,
    meta: { requiresAuth: true },
  },

  {
    path: "/ManageProject",
    name: "ManageProject",
    component: ManageProject,
    meta: { requiresAuth: true },
  },

  {
    path: "/getTeam/:id",
    name: "getTeam",
    component: getTeam,
    meta: { requiresAuth: true },
  },
  {
    path: "/project/:id",
    name: "Single Project",
    component: singleProject,
    meta: { requiresAuth: true },
  },


  {
    path: "/TimeCorrection",
    name: "TimeCorrection",
    component: TimeCorrection,
  },

  {

    path: "/WorkingTimesPlus",
    name: "Working Times+",
    component: WorkingTimesView,
  },
  {
    path: "/WorkingTimes",
    name: "Working Times",
    component: WorkingTimesView,
  },
  {
    path: "/test",
    name: "test",
    component: InnerTables,
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



router.beforeEach(async (to, from, next) => {
  
  const User = useUser()

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!User.isLoggedIn) {
      next('/login') // Redirect to login if not authenticated
      // next()
    }
    else {
      const storedToken = localStorage.getItem('token') 
      await User.fetchUserData(storedToken)
      try {
        const userRole = User.getUserData.company_role
      }
      catch (error) {
        console.log(error)
      }
      if (User.getUserData.company_role) {
        if (to.meta.roles) {
          if (!to.meta.roles.includes(User.getUserData.company_role)) {
            alert("Not Authorized.")
            next('/timeRegistration')
          }
          else {
            next()
          }
        }
        else {
          next()
        }
      }
      else {
        alert('Error reading Role')
        next('/login')
      }        
    }
  } 
  else {
    next();
  }
});

export default router;
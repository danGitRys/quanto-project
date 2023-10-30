// Composables
import { createRouter, createWebHistory } from "vue-router";
import LoginScreen from "@/views/LoginScreen.vue";
import ManageProject from "@/views/ManageProject.vue";
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
    path: "/ManageProject",
    name: "ManageProject",
    component: ManageProject,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

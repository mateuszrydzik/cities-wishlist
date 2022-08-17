import { createWebHistory, createRouter } from "vue-router";

import MapContainer from "@/components/MapContainer.vue";
import Login from "@/components/Login.vue";
import Welcome from "@/components/Welcome.vue";
import store from "../store";

const routes = [
  { path: "/", name: "Welcome", component: Welcome },
  {
    path: "/app",
    name: "MapContainer",
    component: MapContainer,
    // meta: {
    //   requiresAuth: true,
    // },
  },
  { path: "/login", name: "Login", component: Login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// router.beforeEach((to, from, next) => {
//   if (to.matched.some((record) => record.meta.requiresAuth)) {
//     if (!store.getters.isAuthenticated) {
//       next({ name: "Login" });
//     } else {
//       next({ name: "MapContainer" });
//     }
//   } else {
//     next();
//   }
// });

export default router;

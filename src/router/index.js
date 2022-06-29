import { createWebHistory, createRouter } from "vue-router";

import MapContainer from "@/components/MapContainer.vue";
import Login from "@/components/Login.vue";

const routes = [
  { path: "/", name: "MapContainer", component: MapContainer },
  { path: "/login", name: "Login", component: Login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

<template>
  <v-app>
    <div id="app">
      <Toolbar :title="title" />
      <router-view :key="$route.path" />
    </div>
  </v-app>
</template>

<script>
import Toolbar from "./components/Toolbar.vue";

export default {
  name: "App",
  components: {
    Toolbar,
  },
  data: () => ({
    title: "Cities Wishlist",
  }),
};
</script>

<style>
html,
body {
  height: 100%;
  margin: 0;
}
#app {
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  overflow: auto;
}
</style>

<template>
  <v-app>
    <div id="app">
      <Toolbar :title="title" />
      <MapContainer />
      <ButtonAddCity />
    </div>
  </v-app>
</template>

<script>
import Toolbar from "./components/Toolbar.vue";
import ButtonAddCity from "./components/ButtonAddCity.vue";
import MapContainer from "./components/MapContainer.vue";

export default {
  name: "App",
  components: {
    Toolbar,
    ButtonAddCity,
    MapContainer,
  },
  data() {
    return {
      title: "Cities Wishlist",
    };
  },
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
}
</style>

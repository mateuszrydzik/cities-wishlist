<template>
  <v-app-bar app light color="green" height="60px">
    <v-toolbar-title>Cities Wishlist</v-toolbar-title>
    <v-btn @click="emitApp()">Launch map</v-btn>
    <v-btn href="#mainFeatures"> Features </v-btn>
    <v-btn href="#contact"> Contact </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: "Appbar",
  methods: {
    emitApp() {
      this.$parent.App();
    },
  },
};
</script>

<style scoped>
.v-toolbar-title {
  color: white;
}
</style>

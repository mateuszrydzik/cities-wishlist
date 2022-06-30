<template>
  <v-toolbar app light color="green" height="60px">
    <v-toolbar-title>{{ title }}</v-toolbar-title>
  </v-toolbar>
</template>

<script>
export default {
  name: "Toolbar",
  props: {
    title: String,
  },
};
</script>

<style scoped>
.v-toolbar-title {
  color: white;
}
</style>

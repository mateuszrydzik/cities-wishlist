<template>
  <div id="button">
    <v-container>
      <v-btn icon elevation="10" color="green" @click="emitImportPlace">
        {{ icon }}
      </v-btn>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "ButtonImportCity",
  data: () => ({
    icon: "pull",
  }),
  methods: {
    emitImportPlace() {
      this.$parent.importPlace();
    },
  },
};
</script>

<style scoped>
#button {
  position: fixed;
  right: 5%;
  bottom: 15%;
  z-index: 1;
}
</style>

<template>
  <div id="button">
    <v-container>
      <v-btn icon elevation="10" color="green" @click="emitGetAllFeatures">
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
    emitGetAllFeatures() {
      this.$parent.getAllFeatures();
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

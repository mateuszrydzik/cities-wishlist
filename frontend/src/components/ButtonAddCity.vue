<template>
  <div id="button">
    <v-container>
      <v-btn
        icon
        elevation="10"
        color="green"
        @click="$store.commit('enterEditMode')"
      >
        {{ icon }}
      </v-btn>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "ButtonAddCity",
  data: () => ({
    icon: "+",
  }),
};
</script>

<style scoped>
#button {
  position: fixed;
  right: 5%;
  bottom: 5%;
  z-index: 1;
}
</style>

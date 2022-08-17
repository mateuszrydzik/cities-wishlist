<template>
  <v-dialog ref="modal" v-model="dialog">
    <v-card>
      <v-card-title>Add new location!</v-card-title>
      <v-card-text>{{ city }}, {{ countryName }}</v-card-text>
      <v-text-field label="Notes"></v-text-field>
      <v-btn @click="dialog = false">X</v-btn>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "Modal",
  props: {
    city: String,
    countryName: String,
  },
  data: () => ({
    dialog: false,
  }),
};
</script>

<style scoped></style>

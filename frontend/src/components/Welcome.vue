<template>
  <v-container>
    <h1 class="tagline">
      Find all the <span>cities</span> you ever <span>wished</span> to visit
    </h1>
    <p class="description">
      Easy to use app that helps you plan your future trips
    </p>
    <v-card-actions class="justify-center">
      <v-btn
        :rounded="0"
        min-width="300px"
        variant="outlined"
        color="green"
        @click="App()"
        >launch app</v-btn
      ></v-card-actions
    >
    <v-row>
      <v-col>
        <v-card
          min-height="150px"
          variant="outlined"
          color="green"
          title="Select"
          text="Mark your travel destination on the map with a single click. It's
            name will be automatically saved."
        >
        </v-card>
      </v-col>
      <v-img src="selection.png"></v-img></v-row
    ><v-row
      ><v-col>
        <v-card
          min-height="150px"
          variant="outlined"
          color="green"
          title="Modify"
          text="Add notes to your markers and access it's information in a pop-up."
        >
        </v-card></v-col
    ></v-row>
    <v-row
      ><v-col>
        <v-card
          min-height="150px"
          variant="outlined"
          color="green"
          title="Save"
          text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id ipsum bibendum, feugiat ligula vitae, molestie nisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas quis neque sed leo blandit consectetur nec ut ligula.
"
        >
        </v-card
      ></v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Welcome",
  methods: {
    Login() {
      this.$router.push("/login");
    },
    App() {
      this.$router.push("/app");
    },
  },
};
</script>
<style scoped>
.tagline {
  text-align: center;
  font-size: 60px;
  padding: 2%;
}
.description {
  text-align: center;
  font-size: 30px;
  color: gray;
  padding: 2%;
}
.v-btn {
  margin-bottom: 20px;
}
span {
  color: green;
}
</style>

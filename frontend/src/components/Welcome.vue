<template>
  <Appbar />
  <v-container>
    <h1 class="tagline">
      Find all the <span>cities</span> you ever <span>wished</span> to visit
    </h1>
    <p class="description">
      Easy to use app that helps you plan your future trips
    </p>
    <div class="text-center">
      <v-btn
        :rounded="0"
        min-width="300px"
        min-height="60px"
        color="green"
        @click="App()"
        >launch app</v-btn
      >
    </div>
    <v-row align="center" justify="center">
      <v-col>
        <div class="text-h4 text-center" id="mainFeatures">
          With <span>Cities Wishlist</span>, you can:
        </div>
      </v-col>
      <v-col>
        <v-carousel
          cycle
          height="300"
          hide-delimiter-background
          :show-arrows="false"
        >
          <v-carousel-item v-for="(color, i) in colors" :key="color">
            <v-sheet height="100%" tile>
              <div class="d-flex fill-height justify-center align-center">
                <div class="text-h2">
                  {{ color }}
                </div>
              </div>
            </v-sheet>
          </v-carousel-item>
        </v-carousel>
      </v-col>
    </v-row>

    <div
      class="text-h3 text-center"
      style="margin-bottom: 50px; margin-top: 20px"
    >
      main features
    </div>

    <v-row align="center" justify="center">
      <v-col>
        <v-card
          min-height="150px"
          variant="outlined"
          color="green"
          title="Select"
          text="Browse the map, searching for your travel destination. When you're ready, press the plus button and mark it! City's name and it's country will be automatically saved!"
        >
        </v-card>
      </v-col>
      <v-col
        ><v-img max-height="100px" src="./selection.png"></v-img
      ></v-col> </v-row
    ><v-row align="center" justify="center">
      <v-col>
        <v-img max-height="100px" src="./edit.png"></v-img>
      </v-col>
      <v-col>
        <v-card
          min-height="150px"
          variant="outlined"
          color="green"
          title="Modify"
          text="Add notes to your cities and plan your trip ahead! With an edit feature, you can modify existing points, to change their notes"
        >
        </v-card></v-col
    ></v-row>
    <v-row align="center" justify="center"
      ><v-col>
        <v-card
          min-height="150px"
          variant="outlined"
          color="green"
          title="Save"
          text="All your cities will be saved and accesible in the future! You don't need to worry about losing progress"
        >
        </v-card
      ></v-col>
      <v-col>
        <v-img max-height="100px" src="./save.png"></v-img>
      </v-col>
    </v-row>
    <div class="text-center">
      <v-btn
        :rounded="0"
        min-width="300px"
        min-height="60px"
        color="green"
        @click="App()"
        style="margin-top: 20px"
        >test the features</v-btn
      >
    </div>
    <div
      class="text-h3 text-center"
      style="margin-bottom: 20px; margin-top: 20px"
      id="contact"
    >
      you can reach me on
    </div>
    <v-row>
      <v-col>
        <div class="text-h5 text-center" style="height: 80px">
          GitHub

          <a href="https://github.com/mateuszrydzik" target="_blank"
            >mateuszrydzik</a
          >
        </div>
      </v-col>
      <v-col>
        <div class="text-h5 text-center" style="height: 80px">
          Mail

          <a href="mailto:matrydzik@gmail.com" target="_blank"
            >matrydzik@gmail.com</a
          >
        </div>
      </v-col>
    </v-row>
  </v-container>

  <v-footer class="d-flex flex-column pa-0">
    <div class="px-4 py-2 bg-black text-center w-100">
      {{ new Date().getFullYear() }} — <strong>mateusz rydzik</strong>
    </div>
  </v-footer>
</template>

<script>
import Appbar from "./Appbar.vue";

export default {
  data: () => ({
    colors: [
      "search the world for inspirations",
      "plan all your activities",
      "save your trip ideas",
      "pinpoint all previously visited locations",
      "organise your holidays",
    ],
  }),
  name: "Welcome",
  components: {
    Appbar,
  },
  methods: {
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
  margin-bottom: 50px;
}
span {
  color: green;
}
.v-container {
  margin-top: 60px;
}
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.9;
  position: absolute;
  width: 100%;
}
</style>

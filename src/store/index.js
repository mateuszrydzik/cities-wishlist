import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    editModeIsActive: false,
    cursor: "default",
  },
  mutations: {
    enterEditMode(state) {
      state.editModeIsActive = !state.editModeIsActive;
      state.cursor = state.editModeIsActive ? "crosshair" : "default";
    },
    logRevgeocode(data) {
      try {
        const city = data.items[0].address.city;
        const country = data.items[0].address.countryName;
        console.log(city, country);
      } catch (error) {
        console.log(error);
      }
      console.log(city, ",", country);
    },
  },
  actions: {
    async getRevgeocode({ commit }, coords) {
      axios
        .get(
          `https://revgeocode.search.hereapi.com/v1/revgeocode?at=${coords}&lang=en-US&apikey=LVvT59dcc74KpvXZ2cnoSZ2jLBObvuBXWqCzUMUGGo0`
        )
        .then((response) => {
          console.log(
            response.data.items[0].address.city,
            ",",
            response.data.items[0].address.countryName
          );
          // commit("logRevgeocode", data);
        });
    },
  },
  getters: {
    editModeIsActiveState(state) {
      return state.editModeIsActive;
    },
  },
});

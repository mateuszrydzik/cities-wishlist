import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    editModeIsActive: false,
    cursor: "default",
    city: undefined,
    country: undefined,
  },
  mutations: {
    enterEditMode(state) {
      state.editModeIsActive = !state.editModeIsActive;
      state.cursor = state.editModeIsActive ? "crosshair" : "default";
    },
    logRevgeocode(state, response) {
      try {
        state.city = response.data.items[0].address.city;
        state.country = response.data.items[0].address.countryName;
      } catch (error) {
        console.log(error);
      }
    },
  },
  actions: {
    async getRevgeocode({ commit }, coords) {
      await axios
        .get(
          `https://revgeocode.search.hereapi.com/v1/revgeocode?at=${coords}&lang=en-US&apikey=LVvT59dcc74KpvXZ2cnoSZ2jLBObvuBXWqCzUMUGGo0`
        )
        .then((response) => {
          commit("logRevgeocode", response);
        });
    },
  },
  getters: {
    editModeIsActiveState(state) {
      return state.editModeIsActive;
    },
  },
});

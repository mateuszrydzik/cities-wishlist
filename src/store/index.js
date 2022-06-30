import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    editModeIsActive: false,
    cursor: "default",
    city: undefined,
    country: undefined,
    user: undefined,
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
    setUser(state, username) {
      state.user = username;
    },
    Logout(state) {
      state.user = undefined;
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
    async Login({ commit }, User) {
      await axios.post("login", User);
      await commit("setUser", User.get("username"));
    },
    async Logout({ commit }) {
      let user = undefined;
      commit("logout", user);
    },
  },
  getters: {
    editModeIsActiveState(state) {
      return state.editModeIsActive;
    },
    StateUser: (state) => state.user,
    isAuthenticated: (state) => !!state.user,
  },
});

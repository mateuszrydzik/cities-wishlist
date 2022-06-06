import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    editModeIsActive: false,
    icon: '+',
    cursor: 'default',
    lat: '0',
    lon: '15'
  },
  mutations: {
    enterEditMode(state) {
      state.editModeIsActive = !state.editModeIsActive;
      state.icon = state.editModeIsActive ? 'edit' : '+';
      state.cursor= state.editModeIsActive ? 'crosshair' : 'default';
    },
    logRevgeocode(data) {
      try {
        const city = data.items[0].address.city
        const country = data.items[0].address.countryName
      } catch (error) {
        console.log(error)
      }
      console.log(city, ',', country)
    }
  },
  actions: {
    getRevgeocode({ state, commit }){
      axios.get(`https://revgeocode.search.hereapi.com/v1/revgeocode?at=${state.lat},${state.lon}&lang=en-US&apikey=LVvT59dcc74KpvXZ2cnoSZ2jLBObvuBXWqCzUMUGGo0`).then(response => { commit('logRevgeocode', response.data)})
    }
  },
  getters: {
    editModeIsActiveState(state){
      return state.editModeIsActive
    }
  },

})




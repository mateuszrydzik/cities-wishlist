import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    editModeIsActive: false,
    icon: '+',
    cursor: 'default',
    city: '',
    country: '',
    lat: '0',
    lon: '15'
  },
  mutations: {
    enterEditMode(state) {
      state.editModeIsActive = !state.editModeIsActive;
      state.icon = state.editModeIsActive ? 'edit' : '+';
      state.cursor= state.editModeIsActive ? 'crosshair' : 'default';
    },
    logRevgeocode(state, data) {
      try {
        state.city = data.items[0].address.city
        state.country = data.items[0].address.countryName
      } catch (error) {
        console.log(error)
      }
      console.log(state.city, ',', state.country)
    }
  },
  actions: {
    getRevgeocode({ state, commit }){
      axios.get(`https://revgeocode.search.hereapi.com/v1/revgeocode?at=${state.lat},${state.lon}&lang=en-US&apikey=LVvT59dcc74KpvXZ2cnoSZ2jLBObvuBXWqCzUMUGGo0`).then(response => { commit('logRevgeocode', response.data)})
    }
  },
  getters: {
    formattedLocation(state){
      return `${state.city} , ${state.country}`
    }
  },

})




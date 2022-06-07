<template>
  <div 
    ref="map-root"
    :style="{ cursor: $store.state.cursor }">
  </div>
</template>

<script>
  import View from 'ol/View'
  import Map from 'ol/Map'
  import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer'
  import {OSM, Vector as VectorSource } from 'ol/source';
	import {Draw} from 'ol/interaction';
  import {fromLonLat} from 'ol/proj';
  // importing the OpenLayers stylesheet is required for having
  // good looking buttons!
  import 'ol/ol.css'

  export default {
    name: 'MapContainer',
    computed: {
      watchEditMode(){
        return this.$store.getters.editModeIsActiveState
      }
    },
    mounted() {
      const raster = new TileLayer({
            source: new OSM()
          });
			const source = new VectorSource();
      const vector = new VectorLayer({
        source:source
      });
      const map = new Map({
        target: this.$refs['map-root'],
        layers: [raster, vector],
        view: new View({
          zoom: 4,
          projection: 'EPSG:3857',
          center: fromLonLat([15, 52]),
          constrainResolution: true
        }),
      });
      const draw = new Draw({
        type:'Point',
        source:source
      });
      this.addMap(map,draw) //dziala
    },
    methods: {
      addMap(map, draw){
        map.addInteraction(draw)
      },
      changeDraw(state, map, draw){
        if (state===true){
          map.addInteraction(draw)
          } else if (state===false){
          map.removeInteraction(draw)
          }
        },
        testLog(state){
          console.log(`current state: ${state}`)
        }
			},
    watch: {
      watchEditMode: {
        handler: function(newState, oldState){
          // this.testLog(newState) poprawnie loguje, this z metodami dziala
          this.changeDraw(newState, this.map, this.draw) 
          //TypeError: undefined is not an object
          //map i draw jest undefined w watch
          }
        }
      }
    }

</script>

<style scoped>
div {
  width:100%;
  height:calc(100% - 60px);
  position:fixed;
}
</style>


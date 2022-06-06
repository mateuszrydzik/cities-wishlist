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
      })
    },
    methods: {
      addDraw(map, draw){
        map.addInteraction(draw)
        },
      removeDraw(map, draw){
        map.removeInteraction(draw)
        }
			},
    watch: {
      watchEditMode(newState, oldState) {
        if (newState === true) {
          this.addDraw(this.map, this.draw)
        } else if (newState === false){
          this.removeDraw(this.map, this.draw)
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


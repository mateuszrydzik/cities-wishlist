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
  import {Circle as CircleStyle, Fill, Style} from 'ol/style';
  import {fromLonLat} from 'ol/proj';
  import GeoJSON from 'ol/format/GeoJSON';

  // importing the OpenLayers stylesheet is required for having
  // good looking buttons!
  import 'ol/ol.css'

  export default {
    name: 'MapContainer',
    mounted() {
      const raster = new TileLayer({
            source: new OSM()
          });
			const source = new VectorSource({
        format: new GeoJSON({dataProjection: 'EPSG:3857'})
      });
      const vector = new VectorLayer({
        source:source,
        style: new Style({
          image: new CircleStyle({
            radius:5 ,
            fill: new Fill({
              color: '#ffcc3'
            })
          })
        })
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
      this.addInteractions(map);
    },
    methods: {
			addInteractions(map) {
          let draw = new Draw({
    			source: this.source,
    			type: 'Point',
  			  });
  			  map.addInteraction(draw);
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


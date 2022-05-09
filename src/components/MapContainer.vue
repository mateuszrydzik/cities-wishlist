<template>
  <div ref="map-root"
       style="width: 100%; height: 100%"
       @click="GeolocationCoordinates">
  </div>
</template>

<script>
  import View from 'ol/View'
  import Map from 'ol/Map'
  import TileLayer from 'ol/layer/Tile'
  import OSM from 'ol/source/OSM'

  // importing the OpenLayers stylesheet is required for having
  // good looking buttons!
  import 'ol/ol.css'
  import {ScaleLine, defaults as defaultControls} from 'ol/control';
  import { fromLonLat, toLonLat  } from 'ol/proj';
  
  export default {
    name: 'MapContainer',
    mounted() {
      // this is where we create the OpenLayers map
      new Map({
        // the map will be created using the 'map-root' ref
        target: this.$refs['map-root'],
        layers: [
          // adding a background tiled layer
          new TileLayer({
            source: new OSM() // tiles are served by OpenStreetMap
          }),
        ],

        // the map view will initially show the whole world
        view: new View({
          zoom: 4,
          projection: 'EPSG:3857',
          center: fromLonLat([15, 52]),
          constrainResolution: true
        }),
      })
    },
    methods: {
      reverseGeocode(coords) {
      fetch('http://nominatim.openstreetmap.org/reverse?format=json&lon=' + coords[0] + '&lat=' + coords[1])
      .then(function(response) {
            return response.json();
        }).then(function(json) {
            console.log(json);
        });
      },
      getCoords() {
         console.log(this.map.getView().getCenter())
      }
  }
}
</script>
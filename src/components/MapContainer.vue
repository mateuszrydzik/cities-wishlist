<template>
  <div ref="map-root" :style="{ cursor: $store.state.cursor }"></div>
</template>

<script>
import View from "ol/View";
import Map from "ol/Map";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { OSM, Vector as VectorSource } from "ol/source";
import { Draw } from "ol/interaction";
import { fromLonLat, transform } from "ol/proj";
import Overlay from "ol/Overlay";
import "ol/ol.css";

export default {
  name: "MapContainer",
  data: () => ({
    active: false,
    map: undefined,
  }),
  computed: {
    watchEditMode() {
      return this.$store.getters.editModeIsActiveState;
    },
  },
  methods: {
    addDrawInteraction() {
      const vectorLayer = new VectorLayer({
        source: new VectorSource(),
      });
      const draw = new Draw({
        type: "Point",
        source: vectorLayer.getSource(),
      });
      // const overlay = new Overlay({
      //   element: this.$refs["modal"],
      // });
      draw.on("drawend", (event) => {
        const coordinates = transform(
          event.feature.getGeometry().getCoordinates(),
          "EPSG:3857",
          "EPSG:4326"
        );
        console.log(coordinates);
        this.$store.dispatch("getRevgeocode", coordinates.reverse());
        // overlay.setPosition(coordinates);
        this.toggleEditMode();
      });
      draw.setActive(false);
      draw.set("name", "drawInteraction");
      this.map.addLayer(vectorLayer);
      // this.map.addOverlay(overlay);
      this.map.addInteraction(draw);
    },
    toggleEditMode() {
      this.$store.commit("enterEditMode");
    },
    getInteractionByName(interactionName) {
      let interaction = undefined;
      for (const i of this.map.getInteractions().getArray()) {
        if (i.get("name") === interactionName) {
          interaction = i;
        }
      }
      return interaction;
    },
  },
  watch: {
    watchEditMode: {
      handler: function (newState, oldState) {
        const interaction = this.getInteractionByName("drawInteraction");
        interaction.setActive(newState);
      },
    },
  },
  mounted() {
    this.map = new Map({
      target: this.$refs["map-root"],
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
      view: new View({
        zoom: 4,
        projection: "EPSG:3857",
        center: fromLonLat([15, 52]),
        constrainResolution: true,
      }),
    });
    this.addDrawInteraction();
  },
};
</script>

<style scoped>
div {
  width: 100%;
  height: calc(100% - 60px);
  position: fixed;
}
</style>

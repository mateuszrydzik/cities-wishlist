<template>
  <div id="map" ref="map-root" :style="{ cursor: $store.state.cursor }"></div>
  <div id="modal" :city="city" :country="country" :notes="notes" ref="modal">
    {{ city }}, {{ country }} <br />
    <textarea id="input" v-model="notes" placeholder="notes"></textarea>
    <v-btn size="small" color="green" @click="saveNotesToFeature()">
      save notes</v-btn
    >
  </div>
  <ButtonAddCity />
  <ButtonImportCity />
</template>

<script>
import Modal from "./Modal.vue";
import ButtonAddCity from "./ButtonAddCity.vue";
import ButtonImportCity from "./ButtonImportCity.vue";
import View from "ol/View";
import Map from "ol/Map";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { OSM, Vector as VectorSource } from "ol/source";
import { Draw } from "ol/interaction";
import { fromLonLat, transform } from "ol/proj";
import Overlay from "ol/Overlay";
import { Style, Text, Fill, Stroke, Circle } from "ol/style";
import "ol/ol.css";
import GeoJSON from "ol/format/GeoJSON";

export default {
  name: "MapContainer",
  components: {
    Modal,
    ButtonAddCity,
    ButtonImportCity,
  },
  data: () => ({
    active: false,
    vectorLayer: undefined,
    map: undefined,
    city: undefined,
    country: undefined,
    notes: undefined,
    id: 0,
    currentId: undefined,
  }),
  computed: {
    watchEditMode() {
      return this.$store.getters.editModeIsActiveState;
    },
    cityName() {
      return this.$store.state.city;
    },
  },
  methods: {
    addDrawInteraction() {
      this.vectorLayer = new VectorLayer({
        source: new VectorSource(),
      });
      const draw = new Draw({
        type: "Point",
        source: this.vectorLayer.getSource(),
      });
      const overlay = new Overlay({
        element: this.$refs["modal"],
      });
      draw.on("drawend", (event) => {
        const coordinates = transform(
          event.feature.getGeometry().getCoordinates(),
          "EPSG:3857",
          "EPSG:4326"
        );
        this.$store
          .dispatch("getRevgeocode", coordinates.reverse())
          .then(() => {
            event.feature.setProperties({
              city: this.$store.state.city,
              country: this.$store.state.country,
              notes: "",
            });
            event.feature.setId(this.id);
            event.feature.setStyle(
              new Style({
                image: new Circle({
                  stroke: new Stroke({
                    color: "green",
                  }),
                  fill: new Fill({
                    color: "green",
                  }),
                  radius: 5,
                }),
                text: new Text({
                  font: "12px Trebuchet MS",
                  text: event.feature.get("city"),
                  scale: 1.2,
                  textBaseline: "bottom",
                  offsetY: -5,
                }),
              })
            );
          });
        this.toggleEditMode();
        this.getFeauturesOnClick();
        this.id += 1;
      });
      draw.setActive(false);
      draw.set("name", "drawInteraction");
      this.map.addLayer(this.vectorLayer);
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
    getFeauturesOnClick() {
      this.map.on("singleclick", (event) => {
        const feature = this.map.forEachFeatureAtPixel(
          event.pixel,
          function (feature, layer) {
            return feature;
          }
        );
        const overlay = new Overlay({
          element: this.$refs["modal"],
        });
        if (feature) {
          this.notes = "";
          const coord = this.map.getCoordinateFromPixel(event.pixel);
          const object = feature.getProperties();
          if (object.notes) {
            this.notes = object.notes;
          }
          this.city = object.city;
          this.country = object.country;
          this.currentId = feature.getId();
          this.map.addOverlay(overlay);
          overlay.setPosition(coord);
        }
      });
    },
    saveNotesToFeature() {
      const currentFeature = this.vectorLayer
        .getSource()
        .getFeatureById(this.currentId);
      currentFeature.setProperties({
        notes: this.notes,
      });
    },
    importPlace() {
      const importedVectorLayer = new VectorLayer({
        source: new VectorSource({
          format: new GeoJSON({
            dataProjection: "EPSG:3857",
            featureProjection: "EPSG:4326",
          }),
          url: "http://127.0.0.1:5000/place",
        }),
      });

      importedVectorLayer.getSource().on("change", function (evt) {
        const source = evt.target;
        if (source.getState() === "ready") {
          for (const feature in source.getFeatures()) {
            // console.log(source.getFeatures()[feature].values_);
            source.getFeatures()[feature].setStyle(
              new Style({
                image: new Circle({
                  stroke: new Stroke({
                    color: "green",
                  }),
                  fill: new Fill({
                    color: "green",
                  }),
                  radius: 5,
                }),
                text: new Text({
                  font: "12px Trebuchet MS",
                  text: source.getFeatures()[feature].values_.city,
                  scale: 1.2,
                  textBaseline: "bottom",
                  offsetY: -5,
                }),
              })
            );
          }
        }
      });
      this.map.addLayer(importedVectorLayer);
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
    this.getFeauturesOnClick();
  },
};
</script>

<style scoped>
#map {
  width: 100%;
  height: calc(100% - 60px);
  position: fixed;
}
#modal {
  position: absolute;
  background-color: white;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
  padding: 15px;
  border-radius: 10px;
  border: 1px solid #cccccc;
  bottom: 12px;
  left: -50px;
  min-width: 200px;
}
#input {
  font-size: small;
  width: 150px;
  height: 60px;
}
</style>

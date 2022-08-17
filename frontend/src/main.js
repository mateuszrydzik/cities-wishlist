import "vuetify/styles";
import { createApp } from "vue";
import { createVuetify } from "vuetify";
import App from "./App.vue";
import { loadFonts } from "./plugins/webfontloader";
import store from "./store/index.js";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import router from "./router";

loadFonts();

const app = createApp(App);

const vuetify = createVuetify({
  components,
  directives,
});

app.use(vuetify);
app.use(store);
app.use(router);
app.mount("#app");

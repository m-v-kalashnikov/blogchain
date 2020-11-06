import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import titleMixin from "@/mixins/titleMixin";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;
Vue.mixin(titleMixin);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

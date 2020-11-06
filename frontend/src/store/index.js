import Vue from "vue";
import Vuex from "vuex";
import createLogger from "vuex/dist/logger";
import posts from "@/store/posts";
import signup from "@/store/signup";
import password from "@/store/password";
import auth from "@/store/auth";

const debug = process.env.NODE_ENV !== "production";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    posts,
    signup,
    auth,
    password
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
});

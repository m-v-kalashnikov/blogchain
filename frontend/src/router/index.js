import Vue from "vue";
import VueRouter from "vue-router";
import Blog from "@/views/Blog.vue";
import Login from "@/views/Login.vue";
import Lost from "@/views/Lost.vue";
import Register from "@/views/Register.vue";
import PasswordReset from "@/views/PasswordReset.vue";
import PasswordResetConfirm from "@/views/PasswordResetConfirm.vue";
import Profile from "@/views/Profile.vue";
import ProfileOther from "@/views/ProfileOther.vue";
import VerifyEmail from "@/views/VerifyEmail.vue";
import Post from "@/views/Post.vue";
import PostRead from "@/views/PostRead.vue";
import store from "@/store";

const requireAuthenticated = (to, from, next) => {
  store.dispatch("auth/initialize").then(() => {
    if (!store.getters["auth/isAuthenticated"]) {
      next("/login");
    } else {
      next();
    }
  });
};

const requireUnauthenticated = (to, from, next) => {
  store.dispatch("auth/initialize").then(() => {
    if (store.getters["auth/isAuthenticated"]) {
      next("/blog");
    } else {
      next();
    }
  });
};

const redirectLogout = (to, from, next) => {
  store.dispatch("auth/logout").then(() => next("/login"));
};

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/blog"
  },
  {
    path: "/blog",
    name: "Blog",
    component: Blog
  },
  {
    path: "/register",
    name: "Register",
    component: Register
  },
  {
    path: "/register/:key",
    name: "VerifyEmail",
    component: VerifyEmail
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    beforeEnter: requireUnauthenticated
  },
  {
    path: "/password-reset",
    name: "Password Reset",
    component: PasswordReset,
    beforeEnter: requireUnauthenticated
  },
  {
    path: "/password-reset/:uid/:token",
    name: "Password Reset Confirm",
    component: PasswordResetConfirm,
    beforeEnter: requireUnauthenticated
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    beforeEnter: requireAuthenticated
  },
  {
    path: "/profile/:username",
    name: "Profile Other",
    component: ProfileOther,
    beforeEnter: requireAuthenticated
  },
  {
    path: "/post",
    name: "Post",
    component: Post,
    beforeEnter: requireAuthenticated
  },
  {
    path: "/read/:slug",
    name: "Post Read",
    component: PostRead
  },
  {
    path: "/logout",
    name: "Logout",
    beforeEnter: redirectLogout
  },
  {
    path: "*",
    name: "Lost",
    component: Lost
  }
];

const router = new VueRouter({
  base: process.env.BASE_URL,
  routes
});

export default router;

<template>
  <b-navbar sticky toggleable type="dark" variant="info">
    <b-navbar-brand to="/">BlogChain</b-navbar-brand>

    <b-navbar-toggle target="navbar-toggle-collapse">
      <template #default="{ expanded }">
        <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
        <b-icon v-else icon="chevron-bar-down"></b-icon>
      </template>
    </b-navbar-toggle>

    <b-collapse id="navbar-toggle-collapse" is-nav>
      <b-navbar-nav class="ml-auto">
        <div v-if="isAuthenticated">
          <b-nav-item to="/profile">Профиль</b-nav-item>
          <b-nav-item to="/post">Добавить пост</b-nav-item>
          <b-nav-item to="/logout">Выйти</b-nav-item>
        </div>
        <div v-if="!isAuthenticated">
          <b-nav-item to="/login">Войти</b-nav-item>
          <b-nav-item to="/register">Зарегистрироваться</b-nav-item>
        </div>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  computed: mapGetters("auth", ["isAuthenticated"])
};
</script>

<style scoped></style>

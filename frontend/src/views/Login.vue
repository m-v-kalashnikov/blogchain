<template>
  <div class="login">
    <b-card title="Вход">
      <b-form @submit="onSubmit" @reset="onReset" class="login-form">
        <b-form-group
          id="input-group-1"
          label="Имя пользователя:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.username"
            type="text"
            required
            placeholder="Введите имя пользователя"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Ваш пароль:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.password"
            type="password"
            required
            placeholder="Введите пароль"
          ></b-form-input>
        </b-form-group>
        <div class="d-flex justify-content-center">
          <b-button
            class="mr-3"
            type="submit"
            variant="primary"
            :disabled="loading"
          >
            <b-icon
              icon="question-circle-fill"
              animation="spin-reverse"
              variant=""
              v-show="loading"
            >
            </b-icon>
            <span v-show="!loading">Войти</span>
          </b-button>
          <b-button type="reset" variant="danger">Очистить</b-button>
        </div>
      </b-form>
      <b-list-group class="mt-3" v-show="error">
        <b-list-group-item
          variant="danger"
          v-for="(field, error, i) in errorMsg"
          :key="i"
        >
          <b-list-group-item
            variant="danger"
            v-for="(text, i) in field"
            :key="i"
          >
            {{ text }}
          </b-list-group-item>
        </b-list-group-item>
      </b-list-group>
    </b-card>
    <div class="mt-4">
      <router-link to="/register">Создать аккаунт</router-link> |
      <router-link to="/password-reset">Сменить пароль</router-link>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Login",
  title: "Вход | BlogChain",
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  computed: mapState("auth", ["error", "loading", "errorMsg"]),
  methods: {
    login({ username, password }) {
      this.$store
        .dispatch("auth/login", { username, password })
        .then(() => this.$router.push("/"))
        .catch(() => {});
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.login(this.form);
    },
    onReset(evt) {
      evt.preventDefault();
      this.form.username = "";
      this.form.password = "";
    }
  }
};
</script>

<style scoped>
.login {
  min-height: calc(100vh - 66px);
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.login-form {
  min-width: 350px;
}
</style>

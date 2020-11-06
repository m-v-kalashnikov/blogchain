<template>
  <div class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1>Профиль</h1>
    </div>
    <b-card>
      <b-form class="register-form">
        <b-form-group
          id="input-group-1"
          label="Имя пользователя:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.username"
            readonly
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Имя:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.first_name"
            readonly
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-3" label="Фамилия:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="form.last_name"
            readonly
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-4" label="Email:" label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="form.email"
            readonly
          ></b-form-input>
        </b-form-group>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  title: "Профиль | BlogChain",
  name: "ProfileOther",
  data() {
    return {
      form: {
        username: "",
        first_name: "",
        last_name: "",
        email: ""
      }
    };
  },
  computed: {
    ...mapState("auth", ["userData", "errorMsg"])
  },
  mounted() {
    this.getUserInfo();
  },
  methods: {
    getUserInfo() {
      this.$store
        .dispatch("auth/getUserDetails", this.$route.params.username)
        .then(() => {
          this.form.username = this.userData.results[0].username;
          this.form.first_name = this.userData.results[0].first_name;
          this.form.last_name = this.userData.results[0].last_name;
          this.form.email = this.userData.results[0].email;
        });
    }
  }
};
</script>

<style scoped></style>

<template>
  <div class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1>Добавь свое звено в наш BlogChain</h1>
    </div>
    <b-card>
      <b-badge
        :variant="setStyle(msg) ? 'success' : 'danger'"
        block
        v-show="msg"
        class="my-2"
        >{{ msg }}</b-badge
      >
      <b-form class="register-form" @submit="saveData">
        <b-form-file
          class="mb-3"
          required
          type="file"
          accept="image/*"
          v-model="form.picture"
          :state="Boolean(form.picture)"
          placeholder="Выбирете или перетяните сюда файл..."
          drop-placeholder="Тяни сюда..."
        ></b-form-file>
        <b-form-group
          id="input-group-1"
          label="Назвиние поста:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.title"
            type="text"
            required
            placeholder="Придумайте Название которое захочется прочитать"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-3" label="Ваш текст:" label-for="input-3">
          <b-form-textarea
            id="textarea"
            v-model="form.text"
            rows="3"
            max-rows="9"
            required
            placeholder="Ну что ж... Творите)"
          ></b-form-textarea>
        </b-form-group>
        <div class="d-flex justify-content-center">
          <b-button block class="mr-3" type="submit" variant="info"
            >Отправить</b-button
          >
        </div>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  title: "Пост | BlogChain",
  name: "Post",
  data() {
    return {
      msg: "",
      form: {
        title: "",
        picture: null,
        text: ""
      }
    };
  },
  methods: {
    setStyle(msg) {
      return msg.startsWith("Пост") === true;
    },
    redirect() {
      this.$router.push("/");
    },
    async saveData(evt) {
      evt.preventDefault();
      this.posting = true;
      this.msg = "";
      const rt = await this.$store.dispatch("posts/createPost", this.form);
      this.posting = false;
      if (rt) {
        this.msg = "Пост создан!";
        this.redirect();
      } else {
        this.msg = "Что-то... Где-то... Как-то... Пошло не так.";
      }
    }
  }
};
</script>

<style scoped></style>

<template>
  <div class="post-read">
    <b-container>
      <b-row class="mt-5">
        <b-col>
          <h2 class="text-md-left text-dark">{{ data.title }}</h2>
        </b-col>
        <b-col class="text-right">
          <router-link
            class="text-info text-decoration-none"
            :to="{
              name: 'Profile Other',
              params: { username: data.author.username }
            }"
            >{{ data.author.username }}</router-link
          >
          | {{ data.created_at }}
          <span
            v-if="isAuthenticated && data.author.username === userData.username"
          >
            |
            <b-button
              size="sm"
              pill
              variant="outline-danger"
              @click="removePost()"
              >Удалить пост</b-button
            >
          </span>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-img
            thumbnail
            fluid
            center
            :src="data.picture"
            :alt="data.title"
          ></b-img>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <hr class="border-dark" />
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <p class="text-left">{{ data.text }}</p>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <hr class="border-dark" />
        </b-col>
      </b-row>
      <Comment
        :data="data"
        :routeSlug="this.$route.params.slug"
        class="mt-3"
      ></Comment>
    </b-container>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";
import Comment from "@/components/Comment";

export default {
  title: "Чтение | BlogChain",
  name: "PostRead",
  components: {
    Comment
  },
  data() {
    return {
      post: null,
      currentUser: null
    };
  },
  computed: {
    ...mapState("posts", ["loading", "error", "data", "errorMsg"]),
    ...mapState("auth", ["userData"]),
    ...mapGetters("auth", ["isAuthenticated"])
  },
  methods: {
    ...mapActions("posts", ["getPost", "deletePost"]),
    getPostInfo() {
      this.getPost(this.$route.params.slug);
    },
    getAuthor() {
      this.$store.dispatch("auth/getAccountDetails").then(() => {
        this.currentUser = this.userData;
      });
    },
    removePost() {
      this.deletePost(this.data.id);
      this.$router.push("/");
    }
  },
  mounted() {
    this.getPostInfo();
    this.getAuthor();
  }
};
</script>

<style scoped></style>

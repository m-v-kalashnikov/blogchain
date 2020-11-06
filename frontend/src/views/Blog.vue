<template>
  <div class="blog">
    <b-container>
      <b-row v-for="(post, i) in this.data.results" :key="i" class="my-5">
        <div class="col-md-6">
          <b-img
            thumbnail
            fluid
            center
            class="rounded-circle"
            :src="post.picture"
            :alt="post.title"
          ></b-img>
        </div>
        <div class="col-md-6">
          <h4 class="text-md-left text-dark">{{ post.title }}</h4>
          <p class="text-muted text-md-left">{{ post.created_at }}</p>
          <hr class="border-info" />
          <div class="card-text-overflow-hidden h-25">
            <p>{{ post.text }}</p>
            <p class="read-more"></p>
          </div>
          <router-link
            :to="{
              name: 'Post Read',
              params: { slug: post.slug }
            }"
            class="btn btn-outline-info"
          >
            Читать дальше
          </router-link>
        </div>
        <div class="col-12">
          <p class="mt-3">
            Автор:
            <router-link
              :to="{
                name: 'Profile Other',
                params: { username: post.author.username }
              }"
              class="text-info text-decoration-none"
            >
              {{ post.author.username }}
            </router-link>
          </p>
          <hr class="border-dark" />
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  title: "Главная | BlogChain",
  name: "Blog",
  computed: {
    ...mapState("posts", ["loading", "error", "data", "errorMsg"])
  },
  methods: {
    ...mapActions("posts", ["getAllPosts"])
  },
  mounted() {
    this.getAllPosts();
  }
};
</script>

<style scoped>
.card-text-overflow-hidden {
  overflow: hidden;
  position: relative;
  max-height: 15vmax;
  background-image: linear-gradient(to bottom, transparent, white);
}

.card-text-overflow-hidden .read-more {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  text-align: center;
  margin: 0;
  padding: 30px 0;

  /* "transparent" only works here because == rgba(0,0,0,0) */
  background-image: linear-gradient(to bottom, transparent, white);
}
</style>

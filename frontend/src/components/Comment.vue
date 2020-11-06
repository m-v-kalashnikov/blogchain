<template>
  <b-container>
    <b-row class="mt-5">
      <b-col>
        <h3 class="text-center">Коментарии</h3>
      </b-col>
    </b-row>
    <b-form class="row" v-if="isAuthenticated" @submit="onSubmit">
      <b-col>
        <b-form-group>
          <b-form-input
            v-model="comment.text"
            type="text"
            required
            placeholder="Поделитесь своим мнением о посте"
          ></b-form-input>
        </b-form-group>
      </b-col>
      <b-col class="col-md-2">
        <b-button class="mr-3" type="submit" variant="info">Отправить</b-button>
      </b-col>
    </b-form>
    <b-row class="mb-4" v-for="(item, i) in this.data.comments" :key="i">
      <b-col class="card">
        <b-row class="mt-3">
          <b-col class="text-left">
            <p>
              От:
              <router-link
                class="text-info text-decoration-none"
                :to="{
                  name: 'Profile Other',
                  params: { username: item.author.username }
                }"
                >{{ item.author.username }}</router-link
              >
            </p>
          </b-col>
          <b-col class="text-right" v-if="isAuthenticated">
            <b-button
              v-if="
                userData.username === item.author.username ||
                  userData.username === data.author.username
              "
              size="sm"
              pill
              variant="outline-danger"
              @click="preRemoveComment(item)"
              >Х</b-button
            >
          </b-col>
        </b-row>
        <b-row>
          <b-col
            class="text-left card-text-overflow-hidden"
            :id="dinamicId(i, 1)"
          >
            <p>{{ item.text }}</p>
            <p class="read-more">
              <b-button variant="transparent" block @click="reveal(i)"
                ><b-icon
                  icon="view-list"
                  variant="danger"
                  size="sm"
                  animation="fade"
                ></b-icon
              ></b-button>
            </p>
          </b-col>
        </b-row>
        <hr class="border-dark" />
        <b-row>
          <b-col class="text-left">
            <p class="text-secondary">{{ item.created_at }}</p>
          </b-col>
          <b-col class="text-right mb-3 ">
            <div v-if="!isAuthenticated">
              <b-button
                size="sm"
                pill
                variant="outline-success"
                class="m-1"
                disabled
                >{{ item.positive }}</b-button
              >
              <b-button
                size="sm"
                pill
                variant="outline-danger"
                class="m-1"
                disabled
                >{{ item.negative }}</b-button
              >
            </div>
            <div v-if="isAuthenticated">
              <b-button
                v-if="userData.username === data.author.username"
                size="sm"
                pill
                variant="outline-info"
                class="m-1"
                @click="getVoted(item.id)"
                >Кто голосовал?</b-button
              >
              <b-button
                size="sm"
                pill
                variant="outline-success"
                class="m-1"
                @click="preMakeRate('P', item)"
                >{{ item.positive }}</b-button
              >
              <b-button
                size="sm"
                pill
                variant="outline-danger"
                class="m-1"
                @click="preMakeRate('N', item)"
                >{{ item.negative }}</b-button
              >
            </div>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
    <b-modal
      v-if="votedData"
      size="xl"
      ok-only="true"
      scrollable="true"
      ref="voted-modal"
      title="Кто за что голосовал?"
    >
      <div>
        <b-icon v-show="loading" icon="arrow-repeat"></b-icon>
        <b-row
          v-show="votedData"
          v-for="(item, a) in this.votedData.results"
          :key="a"
        >
          <b-col>
            <b-button
              block="true"
              pill="true"
              :variant="getVariant(item)"
              :to="{
                name: 'Profile Other',
                params: { username: item.author.username }
              }"
              >{{ item.author.username }}</b-button
            >
          </b-col>
        </b-row>
      </div>
    </b-modal>
  </b-container>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";

export default {
  name: "Comment",
  props: ["data", "routeSlug"],
  data() {
    return {
      comment: {
        text: "",
        post: null,
        slug: ""
      }
    };
  },
  computed: {
    ...mapGetters("auth", ["isAuthenticated"]),
    ...mapState("auth", ["userData"]),
    ...mapState("posts", ["error", "loading", "errorMsg", "votedData"])
  },
  mounted() {
    this.comment.post = this.data.id;
    this.comment.slug = this.routeSlug;
  },
  methods: {
    ...mapActions("posts", ["addComment", "deleteComment"]),
    onSubmit(evt) {
      evt.preventDefault();
      this.addComment(this.comment);
      this.comment.text = "";
    },
    preMakeRate(opinion, comment) {
      this.makeRate(opinion, comment, this.routeSlug);
    },
    makeRate(opinion, comment, slug) {
      this.$store.dispatch("posts/makeRateStore", { opinion, comment, slug });
    },
    dinamicId(i, int) {
      return `anchor-${i}-${int}`;
    },
    reveal(id) {
      let element1 = document.getElementById(this.dinamicId(id, 1));
      element1.classList.toggle("card-text-overflow-hidden");
    },
    preRemoveComment(item) {
      this.removeComment(item.id, this.routeSlug);
    },
    removeComment(id, slug) {
      this.$store.dispatch("posts/deleteComment", { id, slug });
    },
    showModal() {
      this.$refs["voted-modal"].show();
    },
    getVariant(item) {
      if (item.opinion === "P") {
        return "success";
      } else if (item.opinion === "N") {
        return "danger";
      }
    },
    getVoted(commentId) {
      this.$store.dispatch("posts/getVotedStore", { commentId }).then(() => {
        this.showModal();
      });
    }
  }
};
</script>

<style scoped>
.card-text-overflow-hidden {
  overflow: hidden;
  position: relative;
  max-height: 10vmax;
  background-image: linear-gradient(to bottom, transparent, white);
}

.card-text-overflow-hidden .read-more {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  text-align: center;
  margin: 0;
  padding: 10px 0;

  /* "transparent" only works here because == rgba(0,0,0,0) */
  background-image: linear-gradient(to bottom, transparent, white);
}
</style>

import posts from "@/api/posts";
import {
  LOADING_START,
  SET_DATA,
  LOADING_SUCCESS,
  SET_VOTED_DATA,
  LOADING_FAILURE
} from "@/store/types";

const initialState = {
  loading: false,
  error: false,
  data: null,
  votedData: null,
  errorMsg: String
};

const getters = {
  data: state => state.data
};

const actions = {
  getAllPosts({ commit }) {
    commit(LOADING_START);
    return posts
      .getPosts()
      .then(({ data }) => commit(SET_DATA, data))
      .then(() => {
        commit(LOADING_SUCCESS);
      })
      .catch(() => {
        commit(LOADING_FAILURE);
      });
  },
  getPost({ commit }, slug) {
    commit(LOADING_START);
    return posts
      .getPostApi(slug)
      .then(({ data }) => commit(SET_DATA, data.results[0]))
      .then(() => commit(LOADING_SUCCESS))
      .catch(() => commit(LOADING_FAILURE));
  },
  createPost({ commit }, data) {
    commit(LOADING_START);
    return new Promise(resolve => {
      posts
        .createPostApi(data)
        .then(() => {
          resolve(true);
          commit(LOADING_SUCCESS);
        })
        .catch(err => {
          commit(LOADING_FAILURE, err.response.data.detail);
          return resolve(false);
        });
    });
  },
  deletePost({ commit, dispatch }, id) {
    commit(LOADING_START);
    return posts
      .removePost(id)
      .then(() => {
        commit(LOADING_SUCCESS);
        dispatch("getAllPosts");
      })
      .catch(() => commit(LOADING_FAILURE));
  },
  addComment({ commit }, comment) {
    commit(LOADING_START);
    return new Promise(resolve => {
      posts
        .createComment(comment)
        .then(() => {
          resolve(true);
          commit(LOADING_SUCCESS);
          posts
            .getPostApi(comment.slug)
            .then(({ data }) => commit(SET_DATA, data.results[0]))
            .then(() => commit(LOADING_SUCCESS))
            .catch(() => commit(LOADING_FAILURE));
        })
        .catch(err => {
          commit(LOADING_FAILURE, err.response.data.detail);
          return resolve(false);
        });
    });
  },
  deleteComment({ commit }, { id, slug }) {
    commit(LOADING_START);
    return posts
      .removeCommentApi(id)
      .then(() => {
        commit(LOADING_SUCCESS);
        posts
          .getPostApi(slug)
          .then(({ data }) => commit(SET_DATA, data.results[0]))
          .then(() => commit(LOADING_SUCCESS))
          .catch(() => commit(LOADING_FAILURE));
      })
      .catch(() => commit(LOADING_FAILURE));
  },
  makeRateStore({ commit, dispatch }, { opinion, comment, slug }) {
    commit(LOADING_START);
    return posts
      .makeRateApi(opinion, comment)
      .then(() => {
        commit(LOADING_SUCCESS);
        dispatch("getPost", slug);
      })
      .catch(() => commit(LOADING_FAILURE));
  },
  getVotedStore({ commit }, { commentId }) {
    commit(LOADING_START);
    return posts
      .getVotedApi(commentId)
      .then(({ data }) => {
        commit(LOADING_SUCCESS);
        commit(SET_VOTED_DATA, data);
      })
      .catch(() => commit(LOADING_FAILURE));
  }
};

const mutations = {
  [LOADING_START](state) {
    state.loading = true;
    state.error = false;
    state.errorMsg = "";
  },
  [LOADING_FAILURE](state, errorMsg = "") {
    state.loading = false;
    state.error = true;
    state.errorMsg = errorMsg;
  },
  [LOADING_SUCCESS](state) {
    state.loading = false;
    state.error = false;
  },
  [SET_DATA](state, data) {
    state.data = data;
  },
  [SET_VOTED_DATA](state, data) {
    state.votedData = data;
  }
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations
};

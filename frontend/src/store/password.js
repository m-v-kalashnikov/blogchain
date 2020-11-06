import auth from "../api/auth";
import {
  PASSWORD_EMAIL_BEGIN,
  PASSWORD_EMAIL_SUCCESS,
  PASSWORD_EMAIL_FAILURE,
  PASSWORD_EMAIL_CLEAR,
  PASSWORD_RESET_BEGIN,
  PASSWORD_RESET_SUCCESS,
  PASSWORD_RESET_FAILURE,
  PASSWORD_RESET_CLEAR
} from "@/store/types";

export default {
  namespaced: true,
  state: {
    emailCompleted: false,
    emailError: false,
    emailLoading: false,
    resetCompleted: false,
    resetError: false,
    resetLoading: false,
    errorMsg: ""
  },
  actions: {
    sendPasswordResetEmail({ commit }, { email }) {
      commit(PASSWORD_EMAIL_BEGIN);
      return auth
        .sendAccountPasswordResetEmail(email)
        .then(() => commit(PASSWORD_EMAIL_SUCCESS))
        .catch(() => commit(PASSWORD_EMAIL_FAILURE));
    },
    clearEmailStatus({ commit }) {
      commit(PASSWORD_EMAIL_CLEAR);
    },
    resetPassword({ commit }, { uid, token, password1, password2 }) {
      commit(PASSWORD_RESET_BEGIN);
      return auth
        .resetAccountPassword(uid, token, password1, password2)
        .then(() => commit(PASSWORD_RESET_SUCCESS))
        .catch(err => commit(PASSWORD_RESET_FAILURE, err.response.data));
    },
    clearResetStatus({ commit }) {
      commit(PASSWORD_RESET_CLEAR);
    }
  },
  mutations: {
    [PASSWORD_EMAIL_BEGIN](state) {
      state.emailLoading = true;
    },
    [PASSWORD_EMAIL_CLEAR](state) {
      state.emailCompleted = false;
      state.emailError = false;
      state.emailLoading = false;
    },
    [PASSWORD_EMAIL_FAILURE](state) {
      state.emailError = true;
      state.emailLoading = false;
    },
    [PASSWORD_EMAIL_SUCCESS](state) {
      state.emailCompleted = true;
      state.emailError = false;
      state.emailLoading = false;
    },
    [PASSWORD_RESET_BEGIN](state) {
      state.resetLoading = true;
    },
    [PASSWORD_RESET_CLEAR](state) {
      state.resetCompleted = false;
      state.resetError = false;
      state.resetLoading = false;
    },
    [PASSWORD_RESET_FAILURE](state, errData) {
      state.resetError = true;
      state.resetLoading = false;
      state.errorMsg = errData;
    },
    [PASSWORD_RESET_SUCCESS](state) {
      state.resetCompleted = true;
      state.resetError = false;
      state.resetLoading = false;
    }
  }
};

import session from "./session";

export default {
  login(username, password) {
    return session.post("/api/auth/login/", { username, password });
  },
  logout() {
    return session.post("/api/auth/logout/", {});
  },
  createAccount(username, password1, password2, email) {
    return session.post("/api/auth/registration/", {
      username,
      password1,
      password2,
      email
    });
  },
  verifyAccountEmail(key) {
    return session.post("/api/auth/registration/verify-email/", { key });
  },
  sendAccountPasswordResetEmail(email) {
    return session.post("/api/auth/password/reset/", { email });
  },
  resetAccountPassword(uid, token, new_password1, new_password2) {
    return session.post("/api/auth/password/reset/confirm/", {
      uid,
      token,
      new_password1,
      new_password2
    });
  },
  getAccountDetailsApi() {
    return session.get("/api/auth/user/");
  },
  updateAccountDetails(data) {
    return session.patch("/api/auth/user/", data);
  },
  getUser(username) {
    return session.get(`/api/users/?username=${username}`);
  }
};

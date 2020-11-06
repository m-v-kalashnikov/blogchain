import session from "./session";

export default {
  getPosts() {
    return session.get("/api/post/");
  },
  getPostApi(slug) {
    return session.get(`/api/post/?slug=${slug}`);
  },
  createPostApi(data) {
    let formData = new FormData();

    formData.append("title", data.title);
    formData.append("picture", data.picture);
    formData.append("text", data.text);

    return session.post("/api/post/", formData, {
      headers: { "Content-Type": "multipart/form-data" }
    });
  },
  removePost(id) {
    return session.delete(`/api/post/${id}/`);
  },
  createComment(comment) {
    let formData = new FormData();
    formData.append("text", comment.text);
    formData.append("post_id", comment.post);
    return session.post("/api/comment/", formData);
  },
  makeRateApi(opinion, comment) {
    let formData = new FormData();
    formData.append("opinion", opinion);
    formData.append("comment", comment.id);
    return session.post("/api/rate-of-comment/", formData);
  },
  removeCommentApi(id) {
    return session.delete(`/api/comment/${id}/`);
  },
  getVotedApi(commentId) {
    return session.get(`/api/rate-of-comment/?comment__id=${commentId}`);
  }
};

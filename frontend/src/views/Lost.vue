<template>
  <div class="lost">
    <h1>404</h1>
    <h4>Похоже кто-то потерялся.</h4>
    <router-link to="/">Верните меня на путь истиный</router-link>
  </div>
</template>

<script>
export default {
  name: "lost",
  title: "Потеряшка | BlogChain"
};
</script>

<style>
.lost {
  min-height: calc(100vh - 66px);
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>

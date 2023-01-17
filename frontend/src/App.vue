<template>
  <div class="body">
    <Auth
      @updateToken="updateToken"
      @updateLoginStatus="updateLoginStatus"
    ></Auth>
    <div class="content" v-if="loggedIn">
      <Uploader class="content-item" :token="token"></Uploader>
      <Gallery class="content-item"></Gallery>
    </div>
  </div>
</template>

<script>
import Auth from "./components/Auth.vue";
import Gallery from "./components/Gallery.vue";
import Uploader from "./components/Uploader.vue";

export default {
  data() {
    return {
      loggedIn: false,
      token: "",
    };
  },
  components: {
    Auth,
    Gallery,
    Uploader,
  },
  methods: {
    updateToken(token) {
      this.token = token;
    },
    updateLoginStatus(loggedIn) {
      this.loggedIn = loggedIn;
    },
  },
};
</script>

<style>
.content {
  display: flex;
  width: 100%;
  max-width: 1200px;
  padding: 0 40px;
}

.content-item {
  width: 50%;
  padding: 10px;
}
.btn-close {
  background-color: red;
}
.body {
  min-height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.input {
  display: block;
  min-width: 250px;
  padding: 7px 10px;
  font-size: 14px;
}

.btn {
  padding: 7px 10px;
  font-size: 14px;
  background-color: rgb(233, 82, 82);
  border: none;
  border-radius: 3px;
  color: white;
  cursor: pointer;
  font-weight: 500;
  display: inline-block;
}

.btn-secondary {
  padding: 1px 2px;
  background-color: transparent;
}
</style>

<template>
  <div class="auth" v-if="!loggedIn">
    <div v-if="!accountExists">
      <h3>Sign up</h3>
      <form @submit.prevent="signup">
        <label>Name:</label>
        <input class="input auth-btn" type="text" v-model="name" required>
        <label>Email:</label>
        <input class="input auth-btn" type="email" v-model="email" required>
        <label>Password:</label>
        <input class="input auth-btn" type="password" v-model="password" required>
        <button class="btn" type="submit">Sign up</button>
        <p>
          Already have an account?
          <div class="btn btn-secondary" @click="toggleAccountExists">Log in</div>
        </p>
      </form>
    </div>
    <div v-else>
      <h3>Log in</h3>
      <form @submit.prevent="login">
        <label>Email:</label>
        <input class="input auth-btn" type="email" v-model="email" required>
        <label>Password:</label>
        <input class="input auth-btn" type="password" v-model="password" required>
        <button class="btn" type="submit">Log in</button>
        <p>You don't have an account? <button class="btn btn-secondary" @click="toggleAccountExists">Sign up</button></p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations } from 'vuex';

export default {
  data() {
    return {
      loggedIn: false,
      accountExists: false,
      name: "",
      email: "",
      password: "",
    };
  },
  methods: {
    ...mapMutations(['setToken']),
    toggleAccountExists() {
      this.accountExists = !this.accountExists;
    },
    signup() {
      axios
        .post("http://localhost:8000/api/auth/signup/", {
          name: this.name,
          email: this.email,
          password: this.password
        })
        .then(response => {
          console.log(response.data.success);
        })
        .catch(error => {
          alert("Some error");
          console.log(error);
        });
    },
    login() {
      axios
        .post("http://localhost:8000/api/auth/login/", {
          email: this.email,
          password: this.password
        })
        .then(response => {
          this.loggedIn = true;
          const token = response.data.token;
          this.setToken(token);
          this.$emit('updateToken', token);
          this.$emit('updateLoginStatus', true);
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};

</script>

<style>
@import '../assets/elements.css';
</style>


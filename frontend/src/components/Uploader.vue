<template>
  <div class="uploader">
    <h3>Upload Image</h3>
    <form @submit.prevent="uploadImage">
      <label>Image:</label>
      <input class="input" type="file" ref="image" required />
      <label>Geo Location:</label>
      <input class="input" type="text" v-model="geoLocation" />
      <label>Description:</label>
      <input class="input" type="text" v-model="description" />
      <label>People:</label>
      <input class="input" type="text" v-model="people" />
      <button class="btn" type="submit">Upload</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      loggedIn: false,
      geoLocation: "",
      description: "",
      people: "",
    };
  },
  computed: {
    ...mapState(["token"]),
  },
  methods: {
    ...mapActions(["getImages"]),
    uploadImage() {
      const image = this.$refs.image.files[0];
      let people = "[]";
      let formData = new FormData();
      formData.append("image", image);
      formData.append("geo_location", this.geoLocation);
      formData.append("description", this.description);

      if (this.people.length) {
        people = JSON.stringify(Array.from(this.people.split(',').map(name => {return {"name": name.trim()}})))
      }
      formData.append("people", people);
      axios
        .post("http://localhost:8000/api/manager/upload/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "Authorization": `Token ${this.token}`,
          },
        })
        .then((response) => {
          console.log("suc");
          this.getImages();
        })
        .catch((error) => {
          alert("Some error");
          console.log(error);
        });
    },
  },
  created() {
    console.log(this.token);
  },
};
</script>

<style>
@import "../assets/elements.css";
.uploader {
  display: flex;
  flex-direction: column;
}
</style>

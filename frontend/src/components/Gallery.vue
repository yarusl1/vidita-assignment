
<template>
  <div class="gallery">
    <div class="filter-container">
      <label for="people">People:</label>
      <input
        class="input gallery-input"
        type="text"
        v-model="filters.people_string"
        id="people"
        @input="filterImages"
      />
      <label for="geo_location">Geo Location:</label>
      <input
        class="input gallery-input"
        type="text"
        v-model="filters.geo_location"
        id="geo_location"
        @input="filterImages"
      />
      <label for="date">Date:</label>
      <input
        class="input gallery-input"
        type="text"
        v-model="filters.date"
        id="date"
        @input="filterImages"
      />
      <label for="description">Description:</label>
      <input
        class="input gallery-input"
        type="text"
        v-model="filters.description"
        id="description"
        @input="filterImages"
      />
    </div>
    <div class="image-list">
      <a class="gallery-image" v-for="image in gallery">
        <img :src="image" />
      </a>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  
  data() {
    return {
      images: [],
      filters: {
        people_string: "",
        people: "",
        geo_location: "",
        date: "",
        description: "",
      },
    };
  },
  computed: {
    ...mapState(["token", "gallery"]),
  },
  methods: {
    ...mapActions(["getImages"]),
    filterImages() {
      let filters = Object.assign({}, this.filters);
      if (this.filters.people_string.length) {
        filters.people = JSON.stringify(Array.from(this.filters.people_string.split(',').map(name => {return {"name": name.trim()}})));
      } else {
        filters.people = "[]";
      }
      this.getImages(filters);
    }
  },
  created() {
    this.getImages();
  },
};
</script>

<style>
@import "../assets/elements.css";

.filter-container {
  display: flex;
  flex-direction: column;
}
.gallery-image {
  width: 100%;
}
.gallery-image img {
  width: 100%;
}
</style>
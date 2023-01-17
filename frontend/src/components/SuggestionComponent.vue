<template>
  <div>
    <vue-suggestion 
      v-model="value" 
      :items="items" 
      :setLabel="setLabel" 
      @changed="inputChange" 
      @selected="itemSelected" 
    >
    </vue-suggestion>
  </div>
</template>

<script>
import VueSuggestion from "vue-suggestion";
import axios from "axios";
import { mapState } from "vuex";

export default {
  components: {
    VueSuggestion
  },
  computed: {
    ...mapState(["token"]),
  },
  data() {
    return {
      value: "",
      items: []
    };
  },
  methods: {
    setLabel(item) {
      return item.name;
    },
    inputChange(text) {
      axios
        .get(`http://localhost:8000/api/manager/people_autocomplete/${text}`, {
          headers: {
            "Authorization": `Token ${this.token}`,
          },
        })
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    itemSelected(item) {
      this.value = item.name;
    }
  }
};
</script>



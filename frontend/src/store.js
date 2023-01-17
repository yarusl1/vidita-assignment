import Vuex from "vuex";
import axios from "axios";

const store = new Vuex.Store({
  state: {
    token: "",
    gallery: [],
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
    },
    setGallery(state, gallery) {
      state.gallery = gallery;
    },
  },
  actions: {
    async getImages(context, filters={}) {
      try {
        const { data } = await axios.get(
          "http://localhost:8000/api/manager/list/",
          {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `Token ${context.state.token}`,
            },
            params: filters,
          }
        );

        const images = Array.from(
          Object.values(data).map((entry) => {
            return "http://localhost:8000" + entry;
          })
        );
        context.commit("setGallery", images);
      } catch (error) {
        console.log(error);
      }
    },
  },
  getters: {
    getToken: (state) => state.token,
    getGallery: (state) => state.gallery,
  },
});

export default store;

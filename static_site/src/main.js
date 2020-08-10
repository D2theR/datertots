window.app = new Vue({
  el: "#app",
  data: {
    name: "Dan",
    mrtots: "./src/tat_ico.png",
    logo: "./src/logo.png",
  },
  computed: {
    showAlert() {
      return this.name.length > 4 ? true : false;
    },
  },
});

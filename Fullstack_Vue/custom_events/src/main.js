import Vue from 'vue'
import App from './App.vue'

// ________________________________

// EventBus created globaly
window.EventBus = new Vue({

  data: {
    count: 0
  },

  methods: {
    updateCount(i) {
      this.count = i;
    }
  },

  watch: {
    count() {
      this.$emit('update-count', this.count);
    }
  }


});

// ________________________________

// EventBus created for project with import and/export

// const EventBus = new Vue();
// export default EventBus;

// ________________________________

new Vue({
  el: '#app',
  render: h => h(App)
})

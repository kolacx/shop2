// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App'
import router from './router'
// import BootstrapVue from 'bootstrap-vue'

// import './assets/css/core-style.css';
// import './assets/style.css';


// import './assets/js/jquery/jquery-2.2.4.min.js';
// import './assets/js/popper.min.js';
// import './assets/js/bootstrap.min.js';
// import './assets/js/plugins.js';
// import './assets/js/classy-nav.min.js';
// import './assets/js/active.js';

Vue.config.productionTip = false

Vue.use(VueAxios, axios)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

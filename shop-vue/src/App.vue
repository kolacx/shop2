<template>
  <div id="app">
      <app-header></app-header>
      <router-view/>
      <app-footer></app-footer>
  </div>
</template>

<script>

import appHeader from './components/Header.vue'
import appFooter from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    'app-header': appHeader,
    'app-footer': appFooter,
  },
}
</script>




<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

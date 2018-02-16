<template>
  <div id="app">
    <hr/>
    <CategoryList/>
    <hr/>
  </div>
</template>

<script>
import CategoryList from './components/CategoryList'


export default {
  name: 'App',
  components: {
    CategoryList
  }
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


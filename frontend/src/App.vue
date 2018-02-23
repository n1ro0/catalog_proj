<template>
  <div id="app">
    <hr/>
    <CategoryList/>
    <ProductList/>
    <hr/>
  </div>
</template>

<script>
import CategoryList from './components/CategoryList'
import ProductList from './components/ProductList'

export default {
  name: 'App',
  components: {
    CategoryList,
    ProductList
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


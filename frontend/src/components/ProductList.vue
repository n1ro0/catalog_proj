<template>
  <div>
    <h1>Products List</h1>
    <img
      v-if="loading"
      src="https://i.imgur.com/JfPpwOA.gif"
    >
    <ul v-else>
      <input v-model='text' placeholder='filter name'>
      <button @click='getProducts(text)'>filter</button>
      <li v-for="product in products">
          {{ product.id }}:{{ product.name }} - {{ product.description }}
        <button
          @click='remove(product)'
          >
          remove
        </button>
      </li>

    </ul>

  </div>
</template>

<script>
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    components: {
    },
    data () {
      return {
        text: '',
        loading: false
      }
    },
    computed: {
      ...mapState('products', {
        products: state => state.items
      }),
    },

    methods: {
      ...mapActions('products', {
        getProducts: (dispatch, text) => {
          this.loading = true
          dispatch('getProducts', text)
            .then(() => this.loading = false)
        },
        remove: 'deleteProduct',
      }),


    },

    created () {
        this.getProducts()
        // setInterval(this.getProducts, 30000)
    }
  }
</script>

<style scoped>
</style>

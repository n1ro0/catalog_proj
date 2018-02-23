import {Product} from '@/api/products'


export default {
  namespaced: true,
  state: {
    items: [],
  },

  getters: {

  },

  actions: {
    getProducts ({ commit }, text) {
      Product.list(text).then(categories => {
        commit('setProducts', categories)
      })
    },

    createProduct ({ commit }, productData) {
      Product.create(categoryData).then(product => {
        commit('createProduct', product)
      })
    },

    deleteProduct ({ commit }, product) {
      Product.delete(product).then(response => {
        commit('deleteProduct', product)
      })
    },
  },

  mutations: {

    setProducts (state, products) {
      state.items = products
    },

    createProduct (state, products) {

      state.items = [products, ...state.items]
    },

    deleteProduct (state, { id }) {
      state.items = state.items.filter(item => {
        return item.id !== id
      })
    }
  },



}

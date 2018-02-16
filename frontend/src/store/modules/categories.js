import shop from '@/api/shop'
import {Category} from '@/api/categories'


export default {
  namespaced: true,
  state: {
    items: [],
  },

  getters: {

  },

  actions: {
    getCategories ({ commit }) {
      Category.list().then(categories => {
        commit('setCategories', categories)
      })
    }
  },

  mutations: {
    setCategories (state, categories) {
      state.items = categories
    }
  },

}

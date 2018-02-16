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
    },

    createCategory ({ commit }, categoryData) {
      Category.create(categoryData).then(category => {
        commit('addCategory', category)
      })
    },

    deleteCategory ({ commit }, category) {
      Category.delete(category).then(response => {
        commit('deleteCategory', category)
      })
    },
  },

  mutations: {
    setCategories (state, categories) {
      state.items = categories
    },

    addCategory (state, category) {
      state.items = [category, ...state.categories]
    },

    deleteCategory (state, { id }) {
      state.items = state.items.filter(item => {
        return item.id !== id
      })
    }
  },



}

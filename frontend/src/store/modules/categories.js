import {Category} from '@/api/categories'


export default {
  namespaced: true,
  state: {
    items: [],
  },

  getters: {

  },

  actions: {


    showOrHideCategory ({ commit }, index) {
      commit('showOrHideCategory', index)
    },

    getCategoryItems ({ commit, state }, indexAndName) {
      Category.items(state.items[indexAndName.index], indexAndName.name).then(items => {
        commit('setCategoryItems', {index: indexAndName.index, items})
      })
    },
    getCategories ({ commit }, name) {
      Category.list(name).then(categories => {
        commit('setCategories', categories)
      })
    },

    createCategory ({ commit }, categoryData) {
      Category.create(categoryData).then(category => {
        commit('createCategory', category)
      })
    },

    deleteCategory ({ commit }, category) {
      Category.delete(category).then(response => {
        commit('deleteCategory', category)
      })
    },
  },

  mutations: {

    showOrHideCategory (state, index) {
      if (state.items[index].opened) {
        state.items[index].opened = false
      } else {
        state.items[index].opened = true
      }

    },

    setCategoryItems (state, indexAndItems) {
      state.items[indexAndItems.index].items = indexAndItems.items
    },

    setCategories (state, categories) {
      state.items = categories
    },

    createCategory (state, category) {

      state.items = [category, ...state.items]
    },

    deleteCategory (state, { id }) {
      state.items = state.items.filter(item => {
        return item.id !== id
      })
    }
  },



}

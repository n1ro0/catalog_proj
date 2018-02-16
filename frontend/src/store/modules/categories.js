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

    getCategoryItems ({ commit, state }, index) {
      Category.items(state.items[index]).then(items => {
        commit('setCategoryItems', {index, items})
      })
    },
    getCategories ({ commit }) {
      Category.list().then(categories => {
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

<template>
  <div>
    <h1>Categories List</h1>
    <img
      v-if="loading"
      src="https://i.imgur.com/JfPpwOA.gif"
    >
    <ul v-else>
      <input v-model='name' placeholder='filter name'>
      <button @click='getCategories(name)'>filter</button>
      <li v-for="(category, index) in categories">
        <a @click.prevent='showOrHideCategory(index)'>
          {{ category.id }}:{{ category.name }} - {{ category.parent_category }}
        </a>
        <button
          @click='remove(category)'
          >
          remove
        </button>
        <div v-if="category.opened">
          <CategoryItems :index='index'/>
        </div>
      </li>

    </ul>
    <CreateCategory/>
  </div>
</template>

<script>
  import CreateCategory from './CreateCategory'
  import CategoryItems from './CategoryItems'
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    components: {
      CreateCategory,
      CategoryItems
    },
    data () {
      return {
        name: '',
        loading: false
      }
    },
    computed: {
      ...mapState('categories', {
        categories: state => state.items
      }),
    },

    methods: {
      ...mapActions('categories', {
        getCategories: (dispatch, name) => {
          this.loading = true
          dispatch('getCategories', name)
            .then(() => this.loading = false)
        },
        remove: 'deleteCategory',
        showOrHideCategory: 'showOrHideCategory'
      }),


    },

    created () {
        this.getCategories()
        // setInterval(this.getCategories, 30000)
    }
  }
</script>

<style scoped>
</style>

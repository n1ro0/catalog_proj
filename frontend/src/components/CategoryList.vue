<template>
  <div>
    <h1>Categories List</h1>
    <img
      v-if="loading"
      src="https://i.imgur.com/JfPpwOA.gif"
    >
    <ul v-else>
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
        getCategories: (dispatch) => {
          this.loading = true
          dispatch('getCategories')
            .then(() => this.loading = false)
        },
        remove: 'deleteCategory',
        showOrHideCategory: 'showOrHideCategory'
      }),


    },

    created () {
        this.getCategories()
        setInterval(this.getCategories, 30000)
    }
  }
</script>

<style scoped>
</style>

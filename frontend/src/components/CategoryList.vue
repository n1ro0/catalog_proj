<template>
  <div>
    <h1>Categories List</h1>
    <img
      v-if="loading"
      src="https://i.imgur.com/JfPpwOA.gif"
    >
    <ul v-else>
      <li v-for="category in categories">
        {{ category.id }}:{{ category.name }} - {{ category.parent_category }}
        <button
          @click='remove(category)'
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
        add: 'addCategory',
        remove: 'deleteCategory',
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

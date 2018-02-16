<template>
  <div>
    <h1>Category Items</h1>
    <img
      v-if="loading"
      src="https://i.imgur.com/JfPpwOA.gif"
    >
    <ul v-else>
      <li v-for="item in items">
        <img :src="item.image"></img>
         {{ item.id }}:{{ item.name }} - {{ item.price | currency }}
      </li>

    </ul>
  </div>
</template>

<script>
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    props: ['index'],
    data () {
      return {
        loading: false
      }
    },
    computed: {
      ...mapState('categories', {
        items (state) {
          return state.items[this.index].items}
      }),
    },

    methods: {
      ...mapActions('categories', {
        getCategoryItems: (dispatch, index) => {
          this.loading = true
          dispatch('getCategoryItems', index)
            .then(() => this.loading = false)
        },
      }),


    },

    created () {
        this.getCategoryItems(this.index)
    }
  }
</script>

<style scoped>
</style>

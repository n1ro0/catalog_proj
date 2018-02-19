<template>
  <div>
    <h1>Category Items</h1>
    <input v-model='name' placeholder='filter name'>
    <button @click='getCategoryItems(index, name)'>filter</button>
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
        name: '',
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
        getCategoryItems: (dispatch, index, name) => {
          this.loading = true
          dispatch('getCategoryItems', {index, name})
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

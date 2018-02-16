<template>
  <form @submit.prevent='submitCategory'>
    <input v-model='name' placeholder='category name'>
    <input type='number' v-model='parent_category' placeholder='parent category'>
    <input type='submit' value='create'>
  </form>
</template>

<script>
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    data () {
      return {
        parent_category: null,
        name: ''
      }
    },
    computed: {
    },

    methods: {
      submitCategory () {
        this.create({
          name: this.name,
          parent_category: this.parent_category
        })
        this.parent_category = null,
        this.name = ''
      },


      ...mapActions('categories', {
        create: 'createCategory',
      }),


    },

  }
</script>

<style scoped>
</style>

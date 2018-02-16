import { HTTP } from './common'

export const Category = {
  create (data) {
    return HTTP.post('/categories/', data).then(response => {
      return {...response.data, opened: false, items: []}
    })
  },
  delete (category) {
    return HTTP.delete('/categories/' + category.id + '/')
  },
  list () {
    return HTTP.get('/categories/').then(response => {
      response.data.forEach(category => {
        Object.assign(category, {opened: false, items: []})
      })
      return response.data
      })
  },
  items (category) {
    return HTTP.get('/categories/' + category.id + '/items/').then(response => {
      return response.data
    })
  }
}

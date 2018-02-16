import { HTTP } from './common'

export const Category = {
  create (config) {
    return HTTP.post('/categories/', config).then(response => {
      return response.data
    })
  },
  delete (category) {
    return HTTP.delete(`/categories/${category.id}/`)
  },
  list () {
    return HTTP.get('/categories/').then(response => {
      return response.data
    })
  }
}

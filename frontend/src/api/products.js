import { HTTP } from './common'

export const Product = {
  create (data) {
    return HTTP.post('/items/', data).then(response => {
      return response.data
    })
  },
  delete (category) {
    return HTTP.delete('/items/' + category.id + '/')
  },
  list (text) {
    if (text === undefined || text === '') {
      return HTTP.get('/items/').then(response => {
        return response.data
      })
    } else {
      return HTTP.get('/items/search/?text__contains=' + text).then(response => {
        return response.data['results']
      })
    }
  },
}

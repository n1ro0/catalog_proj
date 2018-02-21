import { HTTP } from './common'

export const Product = {
  create (data) {
    return HTTP.post('/items/', data).then(response => {
      return response.data
    })
  },
  delete (category) {
    return HTTP.delete('/categories/' + category.id + '/')
  },
  list (name) {
    if (name === undefined || name === '') {
      return HTTP.get('/categories/').then(response => {
        if (response.data !== '') {
          response.data.forEach(category => {
            Object.assign(category, {opened: false, items: []})
          })
        }
        return response.data
      })
    } else {
      return HTTP.get('/categories/?name=' + name).then(response => {
        if (response.data !== '') {
          response.data.forEach(category => {
            Object.assign(category, {opened: false, items: []})
          })
        }
        return response.data
      })
    }
  },
  items (category, name) {
    if (name === undefined) {
      return HTTP.get('/categories/' + category.id + '/items/').then(response => {
        return response.data
      })
    } else {
      return HTTP.get('/categories/' + category.id + '/items/?name=' + name).then(response => {
        return response.data
      })
    }
  }
}
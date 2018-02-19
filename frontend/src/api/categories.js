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
  list (name) {
    if (name === undefined) {
      return HTTP.get('/categories/').then(response => {
        response.data.forEach(category => {
          Object.assign(category, {opened: false, items: []})
        })
        return response.data
      })
    } else {
      return HTTP.get('/categories/?name=' + name).then(response => {
        response.data.forEach(category => {
          Object.assign(category, {opened: false, items: []})
        })
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

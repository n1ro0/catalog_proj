import axios from 'axios'

var config = {
  baseURL: 'http://localhost:5001/api/v1/',
  headers: {'Authorization': 'Token 09121c51bc14199cda3d7c84d84a1d93edf48296'}
}

export const HTTP = axios.create(config)


HTTP.post(
  '/api-token-auth/login/', {username: 'test', password: 'qwerty12'}
).then(response => {
  var token = response.data['token']
  console.log(token)
  config.headers = {'Authorization': 'Token ' + token}
})


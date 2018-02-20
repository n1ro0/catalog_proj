import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:5001/api/v1/'
})


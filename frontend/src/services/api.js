import axios from 'axios'

const API_URL = 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add token to requests if it exists
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const authService = {
  login: async (email, password) => {
    const response = await api.post('/login/', { email, password })
    if (response.data.token) {
      localStorage.setItem('access_token', response.data.token)
    }
    return response.data
  },

  register: async (username, email, password) => {
    const response = await api.post('/register/', {
      username,
      email,
      password,
    })
    return response.data
  },

  logout: () => {
    localStorage.removeItem('access_token')
  },
}

export const newsService = {
  getNews: async () => {
    const response = await api.get('/news/')
    return response.data
  },

  getNewsDetail: async (id) => {
    const response = await api.get(`/news/${id}/`)
    return response.data
  },

  createNews: async (title, category, content) => {
    const response = await api.post('/news/', {
      title,
      category,
      content,
    })
    return response.data
  },
}

export default api

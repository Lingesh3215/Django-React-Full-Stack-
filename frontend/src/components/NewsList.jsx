import { useState, useEffect } from 'react'
import { newsService, authService } from '../services/api'
import './NewsList.css'

export default function NewsList({ onLogout }) {
  const [news, setNews] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({
    title: '',
    category: '',
    content: '',
  })

  useEffect(() => {
    fetchNews()
  }, [])

  const fetchNews = async () => {
    try {
      setLoading(true)
      const data = await newsService.getNews()
      setNews(data)
      setError('')
    } catch (err) {
      setError('Failed to load news')
    } finally {
      setLoading(false)
    }
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await newsService.createNews(
        formData.title,
        formData.category,
        formData.content
      )
      setFormData({ title: '', category: '', content: '' })
      setShowForm(false)
      fetchNews()
    } catch (err) {
      setError('Failed to create news')
    }
  }

  const handleLogout = () => {
    authService.logout()
    onLogout()
  }

  if (loading) return <div className="container">Loading...</div>

  return (
    <div className="news-container">
      <div className="navbar">
        <h1>📰 News Aggregator</h1>
        <button onClick={handleLogout} className="logout-btn">
          Logout
        </button>
      </div>

      <div className="container">
        <button
          onClick={() => setShowForm(!showForm)}
          className="add-news-btn"
        >
          {showForm ? 'Cancel' : '+ Add News'}
        </button>

        {showForm && (
          <form className="news-form" onSubmit={handleSubmit}>
            <input
              type="text"
              name="title"
              placeholder="News Title"
              value={formData.title}
              onChange={handleInputChange}
              required
            />
            <input
              type="text"
              name="category"
              placeholder="Category"
              value={formData.category}
              onChange={handleInputChange}
              required
            />
            <textarea
              name="content"
              placeholder="News Content"
              value={formData.content}
              onChange={handleInputChange}
              rows="4"
              required
            />
            <button type="submit" className="submit-btn">
              Post News
            </button>
          </form>
        )}

        {error && <div className="error-message">{error}</div>}

        <div className="news-list">
          {news.length === 0 ? (
            <p className="no-news">No news available</p>
          ) : (
            news.map((item) => (
              <div key={item.id} className="news-card">
                <div className="news-header">
                  <h3>{item.title}</h3>
                  <span className="category">{item.category}</span>
                </div>
                <p className="news-content">{item.content}</p>
                <div className="news-footer">
                  <small>By {item.author_id}</small>
                  <small>
                    {new Date(item.created_at).toLocaleDateString()}
                  </small>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  )
}

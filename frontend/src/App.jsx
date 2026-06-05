import { useState, useEffect } from 'react'
import Login from './components/Login'
import NewsList from './components/NewsList'
import './App.css'

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check if user is already logged in
    const token = localStorage.getItem('access_token')
    setIsLoggedIn(!!token)
    setLoading(false)
  }, [])

  const handleLoginSuccess = () => {
    setIsLoggedIn(true)
  }

  const handleLogout = () => {
    setIsLoggedIn(false)
  }

  if (loading) {
    return <div className="container">Loading...</div>
  }

  return (
    <>
      {isLoggedIn ? (
        <NewsList onLogout={handleLogout} />
      ) : (
        <Login onLoginSuccess={handleLoginSuccess} />
      )}
    </>
  )
}

export default App

# News Aggregator Frontend

This is a React frontend for the News Aggregator Django project, built with Vite.

## Getting Started

### Prerequisites
- Node.js 16+ (download from https://nodejs.org/)
- npm (comes with Node.js)

### Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### Features

- **Login/Logout**: Authenticate with your Django backend using email and password
- **View News**: See all aggregated news articles
- **Post News**: Create new news articles (requires authentication)
- **Categories**: News articles are organized by category
- **JWT Authentication**: Secure token-based authentication

### Build for Production

```bash
npm run build
```

This creates an optimized production build in the `dist` folder.

### How It Works

1. **Backend Communication**: The React app communicates with your Django API at `http://localhost:8000`
2. **Authentication**: JWT tokens are stored in localStorage after login
3. **API Client**: Uses Axios to make HTTP requests to the backend
4. **State Management**: Uses React hooks (useState, useEffect) for state management

### Troubleshooting

**npm not recognized**: 
- Close and reopen your terminal after installing Node.js
- Or restart your computer

**Can't connect to Django**:
- Make sure Django is running: `python manage.py runserver`
- Verify the API URL in `src/services/api.js` is correct

**Port 5173 already in use**:
- Either kill the process using that port or change it in `vite.config.js`

### File Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Login.jsx          # Login component
│   │   ├── Login.css
│   │   ├── NewsList.jsx       # News display component
│   │   └── NewsList.css
│   ├── services/
│   │   └── api.js             # API client & services
│   ├── App.jsx                # Main app component
│   ├── App.css
│   ├── main.jsx               # Entry point
│   └── index.css              # Global styles
├── package.json               # Dependencies
├── vite.config.js             # Vite configuration
└── index.html                 # HTML template
```

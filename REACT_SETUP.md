# Getting Your React App Running

## Summary
✅ React frontend created with Vite  
✅ Django backend configured for CORS  
✅ API client ready to communicate  
✅ Login, news list, and post news components built  

---

## Step-by-Step Setup

### 1. Install Frontend Dependencies
Double-click the **install.bat** file in your project root, OR manually run:

```cmd
cd frontend
npm install
```

Wait for it to finish (takes 1-2 minutes).

### 2. Start Django Backend
In a terminal, navigate to your project root and run:

```cmd
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### 3. Start React Development Server
In another terminal, run:

```cmd
cd frontend
npm run dev
```

You should see:
```
  ➜  Local:   http://localhost:5173/
```

### 4. Open Your App
Go to **http://localhost:5173** in your browser!

---

## How to Use

### First Time
1. Create a user account using the Django admin panel:
   - Go to http://127.0.0.1:8000/admin/
   - Login with your superuser credentials (if you have one)
   - Or insert a test user directly into the database

2. Login with those credentials in the React app

### Create a Test User (Django Shell)
```bash
python manage.py shell

# In the shell:
from Newsapp.models import UserModel, RoleModel

role = RoleModel.objects.get_or_create(id=1, defaults={'role_name': 'user'})[0]
user = UserModel.objects.create(
    username='testuser',
    email='test@example.com',
    password='password123',  # ⚠️ Not hashed! Fix this in production
    role=role
)
```

---

## File Structure

```
NewsAggregator/
├── frontend/                          # React app (NEW!)
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.jsx
│   │   │   └── NewsList.jsx
│   │   ├── services/
│   │   │   └── api.js                 # Django API client
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
├── Newsapp/                           # Django app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
├── NewsAggregator/                    # Django project settings
│   ├── settings.py                    # ✅ Updated with CORS
│   └── urls.py
└── manage.py
```

---

## Common Issues & Fixes

### "npm is not recognized"
- Close your terminal completely and open a NEW one
- Or restart your computer
- PowerShell can be problematic - use **Command Prompt (cmd)** instead

### "Cannot GET /"
- Your React server isn't running. Run `npm run dev` in the frontend folder

### "Cannot connect to backend"
- Make sure Django is running at http://127.0.0.1:8000
- Check that CORS is enabled in `NewsAggregator/settings.py`

### "Login failed"
- Make sure you created a user in Django admin
- Check the browser console (F12) for error messages

---

## Next Steps (When Ready)

1. **Add password hashing**: Update your Django UserModel to properly hash passwords
2. **Database**: Currently using SQLite, consider PostgreSQL for production
3. **Styling**: Customize the components in `src/components/*.css`
4. **Features**: Add ability to edit/delete news, filter by category, search, etc.
5. **Deployment**: Deploy Django on a server (Heroku, PythonAnywhere, etc.) and React on Vercel/Netlify

---

## Notes

- **JWT Authentication**: Tokens are stored in localStorage after login
- **API Base URL**: `http://localhost:8000` (configured in `src/services/api.js`)
- **Development Port**: `http://localhost:5173` (can be changed in `vite.config.js`)
- **Hot Reload**: Changes to React code auto-reload in the browser!


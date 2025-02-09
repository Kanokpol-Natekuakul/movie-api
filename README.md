# Getting Started
Install Backend
bash
Copy
Edit
cd backend
pip install flask mysql-connector-python requests
python app.py
Install Frontend
bash
Copy
Edit
cd frontend
npm install
npm run dev
summarize
Backend (Flask + MySQL)

app.py (Server Start)
database.py (Database Connection)
models.py (Create Table Structure)
routes/movies.py (Movie Retrieval API)
routes/reviews.py (API Review)
Frontend (React + Vite)

App.js (main body)
components/MovieList.jsx (Show Movie)
pages/Home.jsx (home)
This structure allows the backend and frontend to be clearly separated, with support for future 🚀 feature additions.

import requests
import mysql.connector

API_KEY = "your_api_key"
BASE_URL = "https://api.themoviedb.org/3/movie/popular"

db = mysql.connector.connect(host="localhost", user="root", password="password", database="movie_db")
cursor = db.cursor()

def fetch_movies():
    response = requests.get(f"{BASE_URL}?api_key={API_KEY}")
    movies = response.json()["results"]
    
    for movie in movies:
        cursor.execute("""
            INSERT INTO movies (api_id, title, poster_url, release_date, rating)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title), poster_url=VALUES(poster_url), rating=VALUES(rating)
        """, (movie["id"], movie["title"], movie["poster_path"], movie["release_date"], movie["vote_average"]))
    
    db.commit()

fetch_movies()

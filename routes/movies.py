from flask import Blueprint, jsonify
import requests
from database import get_db_connection

movies_bp = Blueprint("movies", __name__)

API_KEY = "your_api_key"

@movies_bp.route("/", methods=["GET"])
def get_movies():
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}")
    return jsonify(response.json()["results"])

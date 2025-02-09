from flask import Blueprint, request, jsonify
from database import get_db_connection

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/<int:movie_id>", methods=["POST"])
def add_review(movie_id):
    data = request.json
    user_id = data["user_id"]
    rating = data["rating"]
    comment = data["comment"]

    db = get_db_connection()
    cursor = db.cursor()
    
    cursor.execute("""
        INSERT INTO reviews (movie_id, user_id, rating, comment)
        VALUES (%s, %s, %s, %s)
    """, (movie_id, user_id, rating, comment))
    
    db.commit()
    db.close()

    return jsonify({"message": "Review added successfully!"})

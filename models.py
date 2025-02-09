from database import get_db_connection

db = get_db_connection()
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    api_id VARCHAR(255) UNIQUE,
    title VARCHAR(255),
    poster_url VARCHAR(255),
    release_date DATE,
    rating FLOAT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    email VARCHAR(100) UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    rating FLOAT CHECK (rating BETWEEN 0 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

db.commit()
db.close()

CREATE TABLE movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    api_id VARCHAR(255) UNIQUE, -- เก็บ ID หนังจาก API
    title VARCHAR(255),
    poster_url VARCHAR(255),
    release_date DATE,
    rating FLOAT
);

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    rating FLOAT CHECK (rating BETWEEN 0 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE emojis (
    id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    emoji_type ENUM('👍', '❤️', '😂', '😢', '😡'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

from flask import Flask
from routes.movies import movies_bp
from routes.users import users_bp
from routes.reviews import reviews_bp
from routes.emojis import emojis_bp

app = Flask(__name__)

# ลงทะเบียน Blueprint (Route)
app.register_blueprint(movies_bp, url_prefix="/movies")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(reviews_bp, url_prefix="/reviews")
app.register_blueprint(emojis_bp, url_prefix="/emojis")

if __name__ == "__main__":
    app.run(debug=True)

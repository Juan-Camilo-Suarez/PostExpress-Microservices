from dataclasses import dataclass

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# initialize SQLAlchemy with app instance
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://your_username:your_password@db/main'
db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    description: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    description = db.Column(db.String(300))
    image = db.Column(db.String(200))


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/products")
def index():
    return jsonify(Product.query.all())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

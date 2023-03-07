from dataclasses import dataclass

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from app import Product, app


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/products")
def index():
    return jsonify(Product.query.all())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

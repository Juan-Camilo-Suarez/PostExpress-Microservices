from dataclasses import dataclass

import requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from app import Product, app


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/products")
def index():
    return jsonify(Product.query.all())

@app.route("/api/products/<int:id>/like", methods=["POST"])
def like(id):
    req = requests.get('http://djangoadmin-backend-1:8000/api/user')
    return jsonify(req.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


from dataclasses import dataclass

import requests
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

from producer import publish
from app import Product, app, ProductUser, db


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/products")
def index():
    return jsonify(Product.query.all())


@app.route("/api/products/<int:id>/like", methods=["POST"])
def like(id):
    req = requests.get('http://djangoadmin-backend-1:8000/api/user')
    json = req.json()
    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success'
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

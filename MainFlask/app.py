from dataclasses import dataclass

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

from main import app

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://your_username:your_password@db/main'
CORS(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db, command='db')


# models
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


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


if __name__ == '__main__':
    app.run()

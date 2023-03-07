import pika, json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import Product
from app import db, app

params = pika.URLParameters('amqps://mjwdfmdv:1IvG-RJ-ZLYLN92M9HPWPZNwrCuSO1RS@rat.rmq2.cloudamqp.com/mjwdfmdv')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

# # create Flask app instance
# app = Flask(__name__)
# initialize SQLAlchemy with app instance
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://your_username:your_password@db/main'
# db = SQLAlchemy(app)


def callback(ch, method, properties, body):
    # create app context
    with app.app_context():
        print('received in main')
        data = json.loads(body)
        print(data)
        if properties.content_type == 'product_created':
            product = Product(id=data['id'], title=data['title'], description=data['description'],
                              image=data['image'], )
            db.session.add(product)
            db.session.commit()
        elif properties.content_type == 'product_updated':
            product = Product.query.get(data['id'])
            product.title = data['title']
            product.image = data['image']
            product.description = data['description']
            db.session.commit()
        elif properties.content_type == 'product_deleted':
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started Consuming')

channel.start_consuming()

channel.close()

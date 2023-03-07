import json
import os, django
import traceback

import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


from DjangoAdmin.products.models import Product

params = pika.URLParameters('amqps://mjwdfmdv:1IvG-RJ-ZLYLN92M9HPWPZNwrCuSO1RS@rat.rmq2.cloudamqp.com/mjwdfmdv')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    try:
        product = Product.objects.get(id=id)
        print(product)
        product.likes = product.likes + 1
        product.save()
        print('Product likes increased!')
    except Exception as e:
        print(traceback.format_exc())
        print('Error: %s' % e)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started Consuming')

channel.start_consuming()

channel.close()

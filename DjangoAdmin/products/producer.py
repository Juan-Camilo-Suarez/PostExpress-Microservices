import pika, json

params = pika.URLParameters('amqps://mjwdfmdv:1IvG-RJ-ZLYLN92M9HPWPZNwrCuSO1RS@rat.rmq2.cloudamqp.com/mjwdfmdv')
connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

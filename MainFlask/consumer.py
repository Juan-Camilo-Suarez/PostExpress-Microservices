import pika

params = pika.URLParameters('amqps://mjwdfmdv:1IvG-RJ-ZLYLN92M9HPWPZNwrCuSO1RS@rat.rmq2.cloudamqp.com/mjwdfmdv')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('started Consuming')

channel.start_consuming()

channel.close()

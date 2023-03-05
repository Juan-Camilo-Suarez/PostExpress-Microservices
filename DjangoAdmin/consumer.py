import pika

params = pika.URLParameters('amqps://mjwdfmdv:1IvG-RJ-ZLYLN92M9HPWPZNwrCuSO1RS@rat.rmq2.cloudamqp.com/mjwdfmdv')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started Consuming')

channel.start_consuming()

channel.close()

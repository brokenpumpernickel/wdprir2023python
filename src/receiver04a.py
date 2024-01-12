import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='wdprir_fanout', exchange_type='fanout')

queue = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='wdprir_fanout', queue=queue.method.queue)

def callback(channel, method, properties, body):
    print(f'Received fanout - {body}!')

channel.basic_consume(queue=queue.method.queue, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

channel.close()
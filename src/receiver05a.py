import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='wdprir_direct', exchange_type='direct')

queue = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='wdprir_direct', queue=queue.method.queue, routing_key='warning')

def callback(channel, method, properties, body):
    print(f'Received fanout - {body}!')

channel.basic_consume(queue=queue.method.queue, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

channel.close()
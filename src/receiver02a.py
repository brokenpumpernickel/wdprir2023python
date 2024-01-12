import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='wdprir_durable', durable=True)

def callback(channel, method, properties, body):
    print(f'Received - {body.decode()}!')

channel.basic_consume(queue='wdprir_durable', on_message_callback=callback, auto_ack=True)
channel.start_consuming()

channel.close()
import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.basic_qos(prefetch_count=1)

channel.queue_declare(queue='wdprir_durable', durable=True)

def callback(channel, method, properties, body):
    time.sleep(5)
    print(f'Received - {body.decode()}!')
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='wdprir_durable', on_message_callback=callback)
channel.start_consuming()

channel.close()
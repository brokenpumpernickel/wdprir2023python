import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='wdprir_durable', durable=True)

counter = 0
while True:
    channel.basic_publish(exchange='',
                          routing_key='wdprir_durable',
                          body=f'Udanej Sesji LOL - {counter = }',
                          properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
    counter += 1
    print(f'Sent - {counter = }')
    time.sleep(1)

channel.close()
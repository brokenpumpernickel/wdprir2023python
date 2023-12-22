import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='wdprir')

counter = 0
while True:
    channel.basic_publish(exchange='', routing_key='wdprir', body=f'Hello WdPRiR - {counter = }!')
    counter += 1
    time.sleep(1)

channel.close()
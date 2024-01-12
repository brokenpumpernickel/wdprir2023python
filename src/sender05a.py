import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='wdprir_direct', exchange_type='direct')

counter = 0
routing_keys = ['info', 'warning', 'error']
while True:
    routing_key = routing_keys[counter % 3]
    channel.basic_publish(exchange='wdprir_direct', routing_key=routing_key, body=f'Hello WdPRiR from direct - {counter = } {routing_key = }!')
    counter += 1
    time.sleep(1)

channel.close()


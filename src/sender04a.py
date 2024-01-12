import pika
import time

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='wdprir_fanout', exchange_type='fanout')

counter = 0
while True:
    channel.basic_publish(exchange='wdprir_fanout', routing_key='', body=f'Hello WdPRiR from fanout - {counter = }!')
    counter += 1
    time.sleep(1)

channel.close()
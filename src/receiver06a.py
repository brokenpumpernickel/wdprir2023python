import pika
import time

def fibon(n):
    if n < 2:
        return n

    return fibon(n - 1) + fibon(n - 2)

credential = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters(host='', credentials=credential, virtual_host='')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.basic_qos(prefetch_count = 1)

channel.queue_declare('wdprir_queue_durable', durable = True)

def callback(channel, method, properties, body):
    print(f'Received: {body.decode() = }')
    n = int(body.decode())
    value = fibon(n)
    print(f'Calculated {n} -> {value}')
    channel.basic_publish('', properties.reply_to, f'{value}', pika.BasicProperties(correlation_id = properties.correlation_id))
    channel.basic_ack(method.delivery_tag)

channel.basic_consume('wdprir_queue_durable', callback)
channel.start_consuming()

channel.close()
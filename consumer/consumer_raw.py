import pika


def minha_callback(ch, method, properties, body):
    print(body.decode())


connection_parameters = pika.ConnectionParameters(
    host="localhost",  # type: ignore
    port=5672,  # type: ignore
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest",
    ),  # type: ignore
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(queue="data_queue", durable=True)
channel.basic_consume(
    queue="data_queue", auto_ack=True, on_message_callback=minha_callback
)


print("Listen RabbitMQ on Port 5672")

channel.start_consuming()

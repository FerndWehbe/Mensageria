import pika

connection_parameters = pika.ConnectionParameters(
    host="localhost",  # type: ignore
    port=5672,  # type: ignore
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest",
    ),  # type: ignore
)


channel = pika.BlockingConnection(connection_parameters).channel()
channel.exchange_declare(exchange="data_exchange", durable=True)
channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="Teste",
    properties=pika.BasicProperties(
        delivery_mode=2,
    ),
)

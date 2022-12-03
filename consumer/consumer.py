import pika


class RabbitMQConsumer:
    def __init__(self, callback) -> None:
        self.__host = "localhost"
        self.__port = "5672"
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.create_channel()

    def __create_connection_parameters(self):
        self.connection_parameters = pika.ConnectionParameters(
            host=self.__host,  # type: ignore
            port=self.__port,  # type: ignore
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password,
            ),  # type: ignore
        )

    def create_channel(self):
        self.__create_connection_parameters()
        channel = pika.BlockingConnection(self.connection_parameters).channel()
        channel.queue_declare(queue=self.__queue, durable=True)
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback,
        )
        self.__channel = channel
        return channel

    def start_channel(self):
        print(f"Listen RabbitMQ on Port {self.__port}")
        self.__channel.start_consuming()


def my_callback(channel, method, properties, body):
    print(body.decode())


if __name__ == "__main__":
    consumer = RabbitMQConsumer(my_callback)
    consumer.start_channel()

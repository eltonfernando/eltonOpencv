
import logging
import pika
logging.basicConfig(level=logging.ERROR)

LOGGER = logging.getLogger(__name__)


class Consumer():
    def __init__(self,name_queue):
        creds = pika.PlainCredentials(username='guest', password='guest')
        params = pika.ConnectionParameters(host='localhost', credentials=creds, )
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.name_queue = name_queue
        self.channel.basic_qos(prefetch_count=2)

    def start(self,on_message):
        arg = {"x-stream-offset": "last"}
        self.channel.basic_consume(self.name_queue, on_message, arguments=arg)
        try:
            self.channel.start_consuming()
        except Exception as error:
            self.channel.start_consuming()
            raise error

    @staticmethod
    def on_message(chan, method_frame, header_frame, body, userdata=None):
        """Called when a message is received. Log message and ack it."""
        # print(chan)
        print(method_frame)
        chan.basic_ack(delivery_tag=method_frame.delivery_tag)


if __name__ == '__main__':
    consu = Consumer()
    consu.start(consu.on_message)

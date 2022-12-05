# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103,R0205
import cv2
import time
import json
import pika


class Producer():
    def __init__(self, exchange, queue):
        creds = pika.PlainCredentials(username='guest', password='guest')
        params = pika.ConnectionParameters(host='localhost', credentials=creds, )
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.name_exchange = exchange
        self.name_queue = queue
        self.routing_key = "x"
        self.__generate_exchange()
        self.__generate_stream_queue()

    def __generate_exchange(self):
        self.channel.exchange_declare(
            exchange=self.name_exchange,
            exchange_type="fanout",
            passive=False,
            durable=True,
            auto_delete=False)

    def __generate_stream_queue(self):
        argumnets = {"x-queue-type": "stream",
                     "x-max-length-bytes": 1_000_000_000,  # maximum stream size 1GB
                     "x-stream-max-segment-size-bytes": 5_000_000}  # size of segment 5MB
        self.channel.queue_declare(queue=self.name_queue, durable=True, arguments=argumnets)

    def start(self):
        self.channel.queue_bind(queue=self.name_queue, exchange=self.name_exchange, routing_key=self.routing_key)

    def set_routing_key(self, key):
        self.routing_key = key

    def append_json(self, data: dict):
        content_type = 'application/json'
        self.channel.basic_publish(
            exchange=self.name_exchange,
            routing_key=self.routing_key,
            body=json.dumps(data),
            properties=pika.BasicProperties(content_type=content_type,
                                            content_encoding="utf-8"))

    def append_byte(self, data: bytes):
        content_type = "text/plain"
        self.channel.basic_publish(
            exchange=self.name_exchange,
            routing_key=self.routing_key,
            body=data,
            properties=pika.BasicProperties(content_type=content_type))

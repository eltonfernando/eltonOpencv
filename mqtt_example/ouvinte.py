import paho.mqtt.client as mqtt
import sys
import logging

import broker
from paho.mqtt import  subscribe

logging.basicConfig(filename="loger.log", level=logging.ERROR)
logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexao: " + str(rc))
    # faz subscribe automatico no topico
    client.subscribe(broker.TOPICO+'/#')

# Callback - mensagem recebida do broker
def on_message(client, userdata, msg):
    MensagemRecebida =msg.payload.decode("utf-8")
    print(f"[ON_MSG] Conectado {msg.topic} msg : {MensagemRecebida}")
 #   comando="config"
#    if MensagemRecebida!=comando:
#        client.publish(msg.topic,comando)

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(f'log: {string}')

if __name__ == "__main__":
    print("[STATUS] Inicializando MQTT...")
    # inicializa MQTT:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish =on_publish
    client.enable_logger(logger)
    #client.on_log=on_log
    client.on_subscribe=on_subscribe
    print("[CONNECT]")

    client.connect(broker.BROKER, broker.PORT, broker.KEEP_ALIVE_BROKER)
    print("[CONNECTED]")
    while True:
        client.loop()


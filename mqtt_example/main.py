#https://iot.eclipse.org/projects/sandboxes/
import logging
import paho.mqtt.client as mqtt
import broker

logging.basicConfig(filename="loger.log", level=logging.ERROR)
logger = logging.getLogger(__name__)

class Publicador():
    def __init__(self):
        self.cliente = mqtt.Client()
        self.cliente.enable_logger(logging.getLogger("tes"))
        self.cliente.on_message = self.on_message
        self.cliente.on_connect = self.on_connect
        self.cliente.enable_logger(logger)
       # self.cliente.on_log=self.on_log
        self.cliente.on_subscribe=self.on_subscribe
        self.id_client="bela_vista"
        self.cam_id="cam01"
        self.cliente.connect(broker.BROKER, broker.PORT, broker.KEEP_ALIVE_BROKER)

    def send_msg(self,msg):
        self.cliente.publish(f'{broker.TOPICO}/{self.id_client}/{self.cam_id}', msg)

    def on_connect(self,client, userdata, flags, rc):
        print(f"[STATUS] Conectado cliente {client} userdata: {userdata} flags: {flags} rc : {rc}")
        client.subscribe(f'{broker.TOPICO}/{self.cliente}/{self.cam_id}')
        #client.publish(broker.TOPICO,"ok conectado")

    @staticmethod
    def on_message(client, userdata, msg):
        MensagemRecebida = str(msg.payload)
        print(f"[MSG RECEBIDA] Topico: {msg.topic} Mensagem: {MensagemRecebida}")

    @staticmethod
    def on_log(mosq, obj, level, string):
        print(f'log: mosq:{mosq}, obj: {obj} level:{level}  string: {string}')

    @staticmethod
    def on_subscribe(mosq, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
if __name__=="__main__":
    from time import sleep
    senseor=Publicador()
    count=0
    while True:
        senseor.send_msg(count)
        senseor.cliente.loop()
        #senseor.cliente.wait_for_publish()
        count+=1
        sleep(2)

    #Ouvinte()
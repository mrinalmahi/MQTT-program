import random
import time
from paho.mqtt import client as mqtt_client


broker = 'inet-mqtt-broker.mpi-inf.mpg.de'
port = 1883
topic = "login"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'mrmr00001@stud.uni-saarland.de'
password = '7028742'
reply=[]
reply_dict = { 'CMD1': 'Apple',
                'CMD2': 'Cat',
                'CMD3': 'Dog',
                'CMD4': 'Rat',
                'CMD5': 'Boy',
                'CMD6': 'Girl',
                'CMD7': 'Toy',
                            }
final='Well done my IoT!'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
def publish(client,msg,topic):
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
             print(f" Topic:{topic} , Message:{msg}")
        else:
            print(f"Failed to send message to topic {topic}")


def subscribe(client,topic='7028742/UUID'):
    def on_message(client, userdata, msg):
        reply.append(str(msg.payload.decode()))
        print(f"Received {reply[0]} from {msg.topic} topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)
    time.sleep(1)
    publish(client,password,topic)
    time.sleep(1)
    subscribe(client, reply[0])
    time.sleep(2)
    while True:
        if(len(reply)>1):
            for com in reply[1:]:
                publish(client,reply_dict[com],reply[0]+'/'+com)
        if(reply[-1]==final):
            break

    
    client.loop_stop()
    print("\n Disconnecting from MQTT Broker")
    client.disconnect()
    


if __name__ == '__main__':
    run()
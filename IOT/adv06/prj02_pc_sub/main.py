from http import client
from pydoc import cli
import paho.mqtt.client as mqtt


def on_connect(client, uderdata, flags, rc):
    print("connected with result code" + str(rc))
    client.subscribe("Leon")


def on_message(client, userdata, msg):
    print(f"我訂閱的主題是:{msg.topic},收到訊息:{msg.payload.decode('utf-8')}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("singular", "1234")

client.connect("singularmakers.asuscomm.com", 1883, 60)
client.loop_forever()
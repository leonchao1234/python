from umqtt.simple import MQTTClient
import time
from mcu_def import mcu_fun

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")

mq_server = "singularmakers.asuscomm.com"
mq_id = "singular"
mq_user = "singular"
mq_pass = "1234"
mqClient0 = MQTTClient(mq_id,
                       mq_server,
                       user=mq_user,
                       password=mq_pass,
                       keepalive=30)

try:
    mqClient0.connect()
except Exception as e:
    print(e)
    exit()
finally:
    print("connected MQTT server")


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")


mqClient0.set_callback(on_message)
mqClient0.subscribe("Leon")

while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(1)

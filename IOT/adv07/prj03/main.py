from umqtt.simple import MQTTClient
import time
from mcu_def import mcu_fun, gpio
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2), freq=4000)
lcd = I2cLcd(i2c, 0x3f, 2, 16)

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")

RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D7, Pin.OUT)
BLUE = Pin(gpio.D6, Pin.OUT)

RED.value(0)
BLUE.value(0)
GREEN.value(0)

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
    # mqClient0.disconnect()
    exit()
finally:
    print("connected MQTT server")


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    lcd.clear()
    lcd.putstr(msg)
    if msg == "on":
        RED.value(1)
        BLUE.value(1)
        GREEN.value(1)
    elif msg == "off":
        RED.value(0)
        BLUE.value(0)
        GREEN.value(0)


mqClient0.set_callback(on_message)
mqClient0.subscribe("Leon")

while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(0.5)

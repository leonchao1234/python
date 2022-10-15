from email.charset import add_charset
from time import sleep
from machine import Pin, ADC
from mcu_def import gpio

adc = ADC(0)
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D7, Pin.OUT)
BLUE = Pin(gpio.D6, Pin.OUT)

RED.value(0)
BLUE.value(0)
GREEN.value(0)

while True:
    for i in range(10):
        GREEN.value(1)
        sleep(0.5)
        GREEN.value(0)
        sleep(0.5)

    for i in range(10):
        RED.value(1)
        GREEN.value(1)
        sleep(0.5)
        RED.value(0)
        GREEN.value(0)
        sleep(0.5)

    for i in range(10):
        RED.value(1)
        sleep(0.5)
        RED.value(0)
        sleep(0.5)

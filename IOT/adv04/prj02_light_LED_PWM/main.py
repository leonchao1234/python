from email.charset import add_charset
from time import sleep
from machine import Pin, ADC
from mcu_def import gpio

adc = ADC(0)
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D7, Pin.OUT)
BLUE = Pin(gpio.D6, Pin.OUT)
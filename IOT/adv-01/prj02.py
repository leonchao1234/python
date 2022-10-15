from machine import Pin, PWM
from time import sleep

frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

led.duty(0)
sleep(1)
led.duty(512)
sleep(2)
led.duty(1023)
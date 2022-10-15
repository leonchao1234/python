from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import network
from mcu_def import gpio

w1SSID = "SingularClass0"
w1PWD = "Singular#1234"

wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)

ap.active(False)
wlan.active(True)
wlan.scan()
wlan.connect(w1SSID, w1PWD)
while not (wlan.isconnected()):
    pass

print("connect successfully", wlan.ifconfig())

i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2), freq=4000)
lcd = I2cLcd(i2c, 0x3f, 2, 16)
lcd.putstr("network config:")
lcd.move_to(0, 1)
lcd.putstr(str(wlan.ifconfig()[0]))

from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
from mcu_def import gpio, mcu_fun

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2), freq=4000)
lcd = I2cLcd(i2c, 0x3f, 2, 16)
lcd.putstr("network config:")
lcd.move_to(0, 1)
lcd.putstr(str(wlan.ip))
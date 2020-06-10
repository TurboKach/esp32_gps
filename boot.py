# This file is executed on every boot (including wake-boot from deepsleep)
try:
    import usocket as socket
except:
    import socket

import gc
import esp
import esp32
import network
import os
import machine


MHZ = 10**6
machine.freq(240*MHZ)  # 240 MHz Frequency

esp.osdebug(None)

gc.collect()
# import webrepl

# webrepl.start()

WIFI_SSID = "Wireless Lab"
WIFI_PWD = "manowawafli"

led = machine.Pin(2, machine.Pin.OUT)  # blue led on your ESP32 board
led.value(1)  # turn in on

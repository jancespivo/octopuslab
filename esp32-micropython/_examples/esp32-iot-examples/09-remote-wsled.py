# usage:
# __import__('09-remote-wsled')
# Android: RoboRemo/menu/connect IP:PORT
# Win: ncat -u IP PORT 

from time import sleep
from machine import Pin
from neopixel import NeoPixel

import WiFiConfig  # Remember set SSID and password in WiFiConfig.py file
from WiFiConnect import WiFiConnect # Include wifi
import usocket

# Import OctopusLab Robot board definition file
import octopus_robot_board as o # octopusLab main library - "o" < octopus

# Warning: RobotBoard version 1 use different WS Pin 13 !
pin_ws = Pin(13, Pin.OUT)
WSUDPPort = 12811
WSBindIP = None

# Robot Board v2 (and newer)
# pin_ws = Pin(o.WS_LED_PIN, Pin.OUT)

np = NeoPixel(pin_ws, 1)
pin_led = Pin(o.BUILT_IN_LED, Pin.OUT)

def simple_blink():
    pin_led.value(1)
    sleep(0.1)
    pin_led.value(0)
    sleep(0.1)

# Default WS led light RED as init
np[0] = (128, 0, 0)
np.write()
simple_blink()

# Define function callback for connecting event
def connected_callback(sta):
    global WSBindIP
    simple_blink()
    np[0] = (0, 128, 0)
    np.write()
    simple_blink()
    print(sta.ifconfig())
    WSBindIP = sta.ifconfig()[0]

def connecting_callback():
    np[0] = (0, 0, 128)
    np.write()
    simple_blink()

w = WiFiConnect()
w.events_add_connecting(connecting_callback)
w.events_add_connected(connected_callback)

w.connect(WiFiConfig.WIFI_SSID, WiFiConfig.WIFI_PASS)

if WSBindIP is not None:
    print("UDP Server run on {}:{}".format(WSBindIP, WSUDPPort))

    us = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
    us.bind((WSBindIP, WSUDPPort))

    ws_red = 0
    ws_green = 0
    ws_blue = 0

    def parseWS_LED(data):
        global ws_red
        global ws_green
        global ws_blue
        global np

        if len(data) < 1:
            return

        if data.decode()[0] == 'R':
            ws_red = int(data[1:])

        elif data.decode()[0] == 'G':
            ws_green = int(data[1:])

        elif data.decode()[0] == 'B':
            ws_blue = int(data[1:])

        else:
            print("Unknown data: {}".format(data.decode()))
            return

        print(data.decode())
        np[0] = (ws_red, ws_green, ws_blue)
        np.write()

    while True:
        data = us.recv(1024)
        parseWS_LED(data)

# library for ws rgb neopixel led - single / strip / ring
# octopusLAB 2019
from time import sleep, sleep_ms
from machine import Pin
from neopixel import NeoPixel

# WS neopixel:
RED = (255, 0, 0)
ORANGE = (255, 64, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0) # = off

class Rgb(NeoPixel):
    def __init__(self, pin, num=1):
        self.pin = pin
        self.num = num
        self.np = NeoPixel(Pin(self.pin, Pin.OUT), self.num)    
    
    def simpleTest(self, wait_ms=500):

        self.np[0] = RED
        self.np.write()
        sleep_ms(wait_ms)

        self.np[0] = GREEN
        self.np.write()
        sleep_ms(wait_ms)

        self.np[0] = BLUE
        self.np.write()
        sleep_ms(wait_ms)

        self.np[0] = (0, 0, 0)
        self.np.write()   

    def color(self, color=RED, i=0):
        self.np[i] = color
        self.np.write()

    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

    def color_chase(self, np, num_pixels, color, wait):
        for i in range(self.num):
            self.np[i] = color
            self.np.write()
            sleep(wait)

    def rainbow_cycle(self, np, num_pixels,wait):
        for j in range(255):
            for i in range(self.num):
                rc_index = (i * 256 // self.num) + j
                self.np[i] = self.wheel(rc_index & 255)
            self.np.write()
            sleep_ms(wait)

    def test(self):
        #https://github.com/maxking/micropython/blob/master/rainbow.py
        self.simpleTest()

        self.color_chase(self.np, self.num,RED, 0.1)  # Increase the number to slow down the color chase
        self.color_chase(self.np, self.num,YELLOW, 0.1)
        self.color_chase(self.np, self.num,GREEN, 0.1)
        self.color_chase(self.np, self.num,CYAN, 0.1)
        self.color_chase(self.np, self.num,BLUE, 0.1)
        self.color_chase(self.np, self.num,PURPLE, 0.1)

        self.rainbow_cycle(self.np, self.num,2)  # Increase the number to slow down the rainbow
        sleep(1)

        self.np.fill(BLACK)
        self.np.write()   
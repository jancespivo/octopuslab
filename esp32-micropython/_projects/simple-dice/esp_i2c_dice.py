from micropython import const
from machine import Pin, I2C, TouchPad
from time import sleep_ms
from urandom import randint

from util.pinout import set_pinout
pinout = set_pinout()


#PCF address = 35 #33-0x21/35-0x23
ADDRESS = 0x20 #0x20(000) 0x23(100)

i2c_sda = Pin(pinout.I2C_SDA_PIN, Pin.IN,  Pin.PULL_UP)
i2c_scl = Pin(pinout.I2C_SCL_PIN, Pin.OUT, Pin.PULL_UP)

i2c = I2C(scl=i2c_scl, sda=i2c_sda, freq=100000) 
# 100kHz as Expander is slow

dice = (
const(0b11101111), #0; int = 239
const(0b11100111), #1; int = 231
const(0b01101011), #2; int = 107
const(0b01100011), #3; int = 99
const(0b01011010), #4; int = 90
const(0b01000010), #5; int = 66
const(0b00011000)  #6; int = 24
)

# touchPin
t1 = TouchPad(Pin(4))
pin_led = Pin(2, Pin.OUT)

def controlCycle():
    autoGen = True
    generate = True
    buttonHeld = 0.0
    cycleTime = 0.0
    phaseTime = 0.1
    phaseDice = 0
    phaseAdv = 0.2
    phaseEnd = phaseAdv * 7 + 0.1
    
    pin_led.value(1)
    
    while True:
        #round(cislo, pocet desetinnych mist)
        cycleTime = round(cycleTime + 0.1, 1)
        phaseTime = round(phaseTime, 1)
                      
        
        if autoGen and not generate:
            generate = True
        
        if generate == True:
            if cycleTime == phaseTime:
                print("Phase timer: " + str(cycleTime) + " next stop: " + str(phaseTime) + " phaseEnd: " + str(phaseEnd), end=" ")
            
                if cycleTime < phaseEnd:
                    i2c.writeto(ADDRESS, bytearray([dice[phaseDice]]))
                    print("Dice generation: " + str(dice[phaseDice]))
                    phaseTime += phaseAdv
                    phaseDice += 1
            
                elif cycleTime == phaseEnd:                    
                        randDice = dice[randint(1, 6)]
                        print("Dice roll: " + str(randDice))
                        i2c.writeto(ADDRESS, bytearray([randDice]))
                        
            if cycleTime == phaseEnd + 3.0:
                cycleTime = 0.0
                phaseTime = 0.1
                phaseDice = 0
                print("EndOfCycle")
        
                if not autoGen:
                    generate = False
                    
            
        if t1.read() < 300: 
            print("button held for {0} seconds.".format(buttonHeld))
            buttonHeld += 0.1
            
        elif buttonHeld > 0.0:
            print("Button pressed! Resetting phase.", end=" ")
            
            if buttonHeld > 2.0:
                autoGen = not autoGen 
                pin_led.value(int(autoGen))
                print("Autogen turned {0}".format("on." if autoGen else "off."), end=" ")
                
            print("")
            buttonHeld = 0.0
            generate = True
            cycleTime = 0.0 
            phaseTime = 0.1
            phaseDice = 0
            
        sleep_ms(100)

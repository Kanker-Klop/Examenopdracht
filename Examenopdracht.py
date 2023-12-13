import apgiotboard
from time import sleep
import random
from machine import Pin

apgiotboard.all_leds_off()

umoeder = ''
program1 = "flak"
while umoeder == '':
    while program1 == "flak":
        if apgiotboard.button_pressed(0):
            Pin(13, Pin.OUT).on()
            apgiotboard.led(1).on()
        else:
            Pin(13, Pin.OUT).off()
            apgiotboard.led(1).off()
        sleep(0.01)
        if apgiotboard.button_pressed(1):
            program1 = "VOLGENDES"
            program2 = "flak"
    while program2 == "flak":

        
    
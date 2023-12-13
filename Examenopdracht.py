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
        if apgiotboard.button_pressed(1,True):
            program1 = "VOLGENDES"
            program2 = "flak"
    while program2 == "flak":
        vorigekneker = None
        vorigeposipinne = None
        posipinne = round(apgiotboard.potentiometer(7))+14
        kneker = round(apgiotboard.potentiometer(apgiotboard.MAXLED))
        apgiotboard.led(kneker).on()
        if vorigekneker != kneker:
            vorigekneker = kneker
            apgiotboard.all_leds_off()
        Pin(posipinne, Pin.OUT).off()
        if vorigeposipinne != posipinne:
            vorigeposipinne = posipinne
            for crack in range(14,22):
                Pin(crack, Pin.OUT).on()
        if apgiotboard.button_pressed(1,True):
            program2 = "VOLGENDES"
            program3 = "flak"
    while program3 == "flak":
        nentemp = apgiotboard.tempsensor()
        if nentemp >= 25.8:
            for templedde in range(0,apgiotboard.MAXLED+1):
                apgiotboard.led(templedde).on()
        else:
            apgiotboard.all_leds_off()
        print(nentemp)
        sleep(0.05)
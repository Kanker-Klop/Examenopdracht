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
        ambtemp = round(apgiotboard.potentiometer(16)+19)
        if nentemp > ambtemp:
            leddenhoogte = (nentemp % ambtemp)
            for temphoogte in range(1,leddenhoogte+1):
                apgiotboard.led(temphoogte).on()
            sleep(0.00001)
            apgiotboard.all_leds_off()
        sleep(0.000001)
        if apgiotboard.button_pressed(1,True):
            program3 = "VOLGENDES"
            program4 = "flak"
    while program4 == "flak":
        vorigeaids = 0
        vorigeaids2 = 0
        vorigeaids3 = 0
        while True:
            apgiotboard.led(vorigeaids).off()
            apgiotboard.led(vorigeaids2).off()
            apgiotboard.led(vorigeaids3).off()
            aids = random.randint(1,apgiotboard.MAXLED)
            aids2 = random.randint(1,apgiotboard.MAXLED)
            aids3 = random.randint(1,apgiotboard.MAXLED)
            if aids == aids2 == aids3:
                for kakaidskak in range(1,apgiotboard.MAXLED+1):
                    apgiotboard.led(kakaidskak).on()
                    sleep(0.2)

            else:
                apgiotboard.led(aids).on()
                apgiotboard.led(aids2).on()
                apgiotboard.led(aids3).on()
            vorigeaids = aids
            vorigeaids2 = aids2
            vorigeaids3 = aids3
            tijdgat = apgiotboard.potentiometer(0.8) 
            sleep(tijdgat)
            

            
            
                
            
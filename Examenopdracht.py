import apgiotboard
from time import sleep
import random
from machine import Pin

apgiotboard.all_leds_off()

bestaan = ''
program1 = "AAN"
while bestaan == '':
    while program1 == "AAN":
        if apgiotboard.button_pressed(0):
            Pin(13, Pin.OUT).on()
            apgiotboard.led(1).on()
        else:
            Pin(13, Pin.OUT).off()
            apgiotboard.led(1).off()
        sleep(0.01)
        if apgiotboard.button_pressed(1,True):
            program1 = "VOLGENDES"
            program2 = "AAN"
    while program2 == "AAN":
        vorigeledje = None
        vorigeposipinne = None
        posipinne = round(apgiotboard.potentiometer(7))+14
        ledje = round(apgiotboard.potentiometer(apgiotboard.MAXLED))
        apgiotboard.led(ledje).on()
        if vorigeledje != ledje:
            vorigeledje = ledje
            apgiotboard.all_leds_off()
        Pin(posipinne, Pin.OUT).off()
        if vorigeposipinne != posipinne:
            vorigeposipinne = posipinne
            for draaien2 in range(14,22):
                Pin(draaien2, Pin.OUT).on()
        if apgiotboard.button_pressed(1,True):
            program2 = "VOLGENDES"
            program3 = "AAN"
    while program3 == "AAN":
        detemp = apgiotboard.tempsensor()
        ambtemp = round(apgiotboard.potentiometer(16)+19)
        if detemp > ambtemp:
            LEDshoogte = (detemp % ambtemp)
            for temphoogte in range(1,LEDshoogte+1):
                apgiotboard.led(temphoogte).on()
            sleep(0.00001)
            apgiotboard.all_leds_off()
        sleep(0.000001)
        if apgiotboard.button_pressed(1,True):
            program3 = "VOLGENDES"
            program4 = "AAN"
    while program4 == "AAN":
        vorigewillekeur = 0
        vorigewillekeur2 = 0
        vorigewillekeur3 = 0
        while True:
            apgiotboard.led(vorigewillekeur).off()
            apgiotboard.led(vorigewillekeur2).off()
            apgiotboard.led(vorigewillekeur3).off()
            willekeur = random.randint(1,apgiotboard.MAXLED)
            willekeur2 = random.randint(1,apgiotboard.MAXLED)
            willekeur3 = random.randint(1,apgiotboard.MAXLED)
            if willekeur == willekeur2 == willekeur3:
                for kakwillekeurkak in range(1,apgiotboard.MAXLED+1):
                    apgiotboard.led(kakwillekeurkak).on()
                    sleep(0.2)
            else:
                apgiotboard.led(willekeur).on()
                apgiotboard.led(willekeur2).on()
                apgiotboard.led(willekeur3).on()
            vorigewillekeur = willekeur
            vorigewillekeur2 = willekeur2
            vorigewillekeur3 = willekeur3
            tijd = apgiotboard.potentiometer(0.8) 
            sleep(tijd)
            if apgiotboard.button_pressed(1,True):
                program4 = "VOLGENDES"
                program5 = "AAN"
                apgiotboard.all_leds_off()
                break
    while program5 == "AAN":
        def willekeurige_meneeren():
           # """dus basically, deze functie maakt 2 willekeurige variabelen (met offset), en als deze gelijk zijn is de returnwaarde True;
#anders is deze False"""
                willeke1 = 2+random.randint(0,4)
                willeke2 = 5+random.randint(0,1)
                gelijkheid = (willeke1 == willeke2)
                return gelijkheid
        apgiotboard.all_leds_off()
        if apgiotboard.button_pressed(0):
            levenstoestand = willekeurige_meneeren()
            print(levenstoestand)
            if levenstoestand:
                for doodgaan in range(1,13):
                    for DOOD in range(1, apgiotboard.MAXLED+1):
                        apgiotboard.led(DOOD).on()
                    sleep(0.1)
                    for DOODuit in range(1, apgiotboard.MAXLED+1):
                        apgiotboard.led(DOODuit).off()
                    sleep(0.1)
            else:
                apgiotboard.led(2).on()
                sleep(1)
        if apgiotboard.button_pressed(1,True):
            program5 = "VOLGENDES"
            program1 = "AAN"
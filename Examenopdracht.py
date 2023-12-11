import apgiotboard
from time import sleep
import random

apgiotboard.all_leds_off()

while True:
    apgiotboard.led(1).on()
    sleep(0.05)
    apgiotboard.led(1).off()
    sleep(0.05)


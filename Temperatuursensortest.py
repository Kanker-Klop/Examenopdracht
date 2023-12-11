import apgiotboard
from time import sleep

while True:
    print(apgiotboard.tempsensor())
    sleep(0.05)
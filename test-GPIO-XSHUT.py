#import RPi.GPIO as GPIO
import time
import explorerhat as eh
import qwiic_vl53l1x

XSHUT_SENSOR1 = 17
XSHUT_SENSOR2 = 27

eh.setmode(GPIO.BCM)
eh.setup(XSHUT_SENSOR1, GPIO.OUT) 
eh.setup(XSHUT_SENSOR2, GPIO.OUT) 

sensor1 = qwiic_vl53l1x.QwiicVL53L1X()
sensor2 = qwiic_vl53l1x.QwiicVL53L1X()


eh.output(XSHUT_SENSOR1, GPIO.LOW) 
eh.output(XSHUT_SENSOR2, GPIO.LOW) 
time.sleep(0.1)

eh.output(XSHUT_SENSOR1, GPIO.HIGH) #enable sensor 1

eh.output(XSHUT_SENSOR1, GPIO.LOW) #disable sensor 1
eh.output(XSHUT_SENSOR2, GPIO.HIGH) #enable sensor 2
time.sleep(0.1)

import qwiic_vl53l1x
mySensor = qwiic_vl53l1x.QwiicVL53L1X()
import time
import sys
mySensor.get_distance()

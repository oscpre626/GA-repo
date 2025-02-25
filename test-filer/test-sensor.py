import qwiic_vl53l1x
import time
import sys
mySensor = qwiic_vl53l1x.QwiicVL53L1X()
mySensor.sensor_init()
print(mySensor.sensor_init())



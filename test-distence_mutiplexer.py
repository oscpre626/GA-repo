import time
from datetime import datetime
import sys
import signal
import qwiic_serlcd
from smbus2 import SMBus, i2c_msg
import VL53L1X
import qwiic_vl53l1x

print("""distance.py

Display the distance read from the sensor.

Press Ctrl+C to exit.

""")

"""
Open and start the VL53L1X ranging sensor for each channel of the TCA9548A
"""
myLCD = qwiic_serlcd.QwiicSerlcd()
sensor1 = qwiic_vl53l1x.QwiicVL53L1X()
sensor1.sensor_init()
print("Python: Initialized")
tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29, tca9548a_num=255, tca9548a_addr=0)
tof1.setI2CAdress(0x28)
tof1.open()
tof1.start_ranging(1)  # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
print("Python: Sensor 1 Opened")

tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29, tca9548a_num=4, tca9548a_addr=0x70)
#tof2.i2c_address(0x29)
tof2.open()

tof2.start_ranging(1)  # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
print("Python: Sensor 2 Opened with new address")

def exit_handler(signal, frame):
    global running
    running = False
    tof1.stop_ranging()
    tof2.stop_ranging()
    print()
    sys.exit(0)
    time.sleep(1)

myLCD.clearScreen()
running = True
signal.signal(signal.SIGINT, exit_handler)

try:
    while running:
        distance_in_mm = tof1.get_distance()
        myLCD.print("Sensor 1 distance: {}mm ".format(distance_in_mm))
        myLCD.clearScreen()
        distance_in_mm = tof2.get_distance()
        myLCD.print("Sensor 2 distance: {}mm ".format(distance_in_mm))
        time.sleep(1)
    

except KeyboardInterrupt:
    tof1.stop_ranging()
    tof2.stop_ranging()
    print("\n Stopped ranging. Exiting")
    time.sleep(1)
#ctrl + c to stop

import time
from datetime import datetime
import sys
import signal
import qwiic_serlcd
from smbus2 import SMBus, i2c_msg
import VL53L1X
import qwiic_vl53l1x
import explorerhat as eh

print("""distance.py

Display the distance read from the sensor.

Press Ctrl+C to exit.

""")

"""
Open and start the VL53L1X ranging sensor for each channel of the TCA9548A
"""
print("on")
eh.output.one.on()

myLCD = qwiic_serlcd.QwiicSerlcd()
sensor1 = qwiic_vl53l1x.QwiicVL53L1X()

print("Python: Initialized")
#tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29, tca9548a_num=255, tca9548a_addr=0)
sensor1.set_i2c_address(0x32)
sensor1.sensor_init()
#sensor1.on()
sensor1.start_ranging(1)  # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
#sensor1.set_distance_mode(1)
print("Python: Sensor 1 Opened")

#sensor2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29, tca9548a_num=4, tca9548a_addr=0x70)
#tof2.i2c_address(0x29)
#tof2.open()
#tof2.start_ranging(1)  # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range

sensor2.set_i2c_address(0x29)
sensor2 = qwiic_vl53l1x.QwiicVL53L1X()
sensor2.sensor_init()
#sensor2.on()
sensor2.start_ranging(1)

print("Python: Sensor 2 Opened with new address")

def exit_handler(signal, frame):
    global running
    running = False
    sensor1.stop_ranging()
    sensor2.stop_ranging()
    print()
    sys.exit(0)
    time.sleep(1)

myLCD.clearScreen()
running = True
signal.signal(signal.SIGINT, exit_handler)

try:
    while running:
        distance_in_mm = sensor1.get_distance()
        myLCD.print("Sensor 1 distance: {}mm ".format(distance_in_mm))
        myLCD.clearScreen()
        distance_in_mm = sensor2.get_distance()
        myLCD.print("Sensor 2 distance: {}mm ".format(distance_in_mm))
        time.sleep(1)
    


except KeyboardInterrupt:
    eh.output.one.off()
    sensor1.stop_ranging()
    sensor2.stop_ranging()
    print("\n Stopped ranging. Exiting")
    time.sleep(1)
#ctrl + c to stop

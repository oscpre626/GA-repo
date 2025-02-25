import sys
import smbus
sys.path.insert(0, "build/lib.linux-armv7l-2.7/")

import qwiic_serlcd
import VL53L1X
import time
from datetime import datetime

bus = smbus.SMBus(1) 
Sensor_ADDRESS = 0x29;
REGISTER = 0x00;
data = bus.read_(Sensor_ADDRESS, REGISTER);
print(f"Data: {data}");

myLCD = qwiic_serlcd.QwiicSerlcd()
tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
#tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
print("Python: Initialized")
tof1.open()
tof1.start_ranging(1)
print("Python: Sensor 1 Opened")

#tof2.open()
#tof2.change_address(0x28)
#tof2.start_ranging(1)
#print("Python: Sensor 2 Opened with new address")
time.sleep(1)
myLCD.clearScreen()

try:
    while True:
        distance_mm1 = tof1.get_distance()
        #distance_mm2 = tof2.get_distance()
        
        print("Time: {} Sensor 1 Distance: {}mm ".format(datetime.utcnow().strftime("%S.%f"), distance_mm1))
        
        myLCD.clearScreen()
        myLCD.print(f"S1: {str(distance_mm1)}mm\nS2")
        
        time.sleep(1)
except KeyboardInterrupt:
    tof1.stop_ranging()
    #tof2.stop_ranging()
    print("\nStopped ranging. Exiting")
#ctrl + c to stop

import sys
sys.path.insert(0, "build/lib.linux-armv7l-2.7/")
import explorerhat as eh
import qwiic_serlcd
import VL53L1X
import time

from datetime import datetime

tof1 = VL53L1X.VL53L1X( i2c_bus=1, i2c_address=0x29)
tof2 = VL53L1X.VL53L1X( i2c_bus=1, i2c_address=0x30)

myLCD = qwiic_serlcd.QwiicSerlcd()

print("Python: Initialized")
tof1.open()
print("Python: Opened")
myLCD.clearScreen()

eh.output.one.off()
eh.output.two.off()
time.sleep(0.1)

eh.output.one.on()
time.sleep(0.1)

tof1.change_address(0x32)
#tof1.open()

eh.output.two.on()
time.sleep(0.1)

#tof2.change_address(0x29)
tof2.open()
#öppnas på 0x29

try:
    while True:
        distance_mm1 = tof1.get_distance()
        distance_mm2 = tof2.get_distance()
        print(f"Sensor 1: {distance_mm1} mm | Sensor 2: {distance_mm2} mm")
        #print("Time: {} Distance: {}mm".format(datetime.utcnow().strftime("%S.%f"), distance_mm))
        time.sleep(0.1)
  
        myLCD.clearScreen()
        #myLCD.print(f"S1: {distance_mm}mm ")   
        time.sleep(0.1)
       
except KeyboardInterrupt:
    tof1.stop_ranging()
    tof2.stop_ranging()
    eh.output.one.off()
    eh.output.two.off()
    myLCD.ClearScreen()
#ctrl + c to stop


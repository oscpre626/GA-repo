import time
import sys
import signal
import qwiic_serlcd
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
myLCD.begin()
myLCD.clearScreen()

#tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29, tca9548a_num=255, tca9548a_addr=0)
sensor1 = qwiic_vl53l1x.QwiicVL53L1X()
sensor1.set_i2c_address(0x32)
sensor1.sensor_init()
#sensor1.on()
sensor1.start_ranging(1)  # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
#sensor1.set_distance_mode(1)

#sensor2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29, tca9548a_num=4, tca9548a_addr=0x70)
#tof2.i2c_address(0x29)
#tof2.open()
#tof2.start_ranging(1)  # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range

sensor2 = qwiic_vl53l1x.QwiicVL53L1X()
sensor2.set_i2c_address(0x38)
sensor2.sensor_init()
#sensor2.on()
sensor2.start_ranging(1)
print("Python: Sensors Initialized")

#print("Python: Sensor 2 Opened with new address")

def exit_handler(signal, frame):
    global running
    running = False
    sensor1.stop_ranging()
    sensor2.stop_ranging()
    eh.output.one.off()
    print("\nExisting...")
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

running = True

#try:
 #   while running:
  #      myLCD.clearScreen()
   #     distance_in_mm1 = sensor1.get_distance()
    #    myLCD.print("Sensor 1 distance: {}mm ".format(distance_in_mm))
     #   myLCD.clearScreen()
      #  distance_in_mm2 = sensor2.get_distance()
       # myLCD.print("Sensor 2 distance: {}mm ".format(distance_in_mm))
        #time.sleep(1)

try: 
    while running:
        myLCD.clearScreen()
    
    try:
        distance_in_mm1 = sensor1.get_distance()
        myLCD.print(f"Sensor 1: {distance1}mm\n")
    except Exception as e:
        print(f"Error reading Sensor 1: {e}")  
        myLCD.print("Sensor 1: Error\n")
        
    try:
        distance_in_mm2 = sensor2.get_distance()
        myLCD.print(f"Sensor 2: {distance2}mm\n")
    except Exception as e:
        print(f"Error reading Sensor 2: {e}")   
        myLCD.print("Sensor 2: Error\n")      

    time.sleep(1)

except KeyboardInterrupt:
   exit_handler(None, None)
#ctrl + c to stop

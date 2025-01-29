import qwiic_vl53l1x
import explorerhat as eh
import time
import sys
import signal
import qwiic_serlcd

print("sensor1 on")
eh.output.one.on()

sensor1 = qwiic_vl53l1x.QwiicVL53L1X()
sensor1.sensor_init()
if sensor1.sensor_init():
    print("Sensor1 initialized successfully!")
else:
    print("Sensor1 initialization failed.")

print("sensor1 off")
eh.output.one.off()


sensor2 = qwiic_vl53l1x.QwiicVL53L1X()
sensor2.sensor_init()
if sensor2.sensor_init():
    print("Sensor2 initialized successfully!")
else:
    print("Sensor2 initialization failed.")
  
try:
	print("Skiver adress")
	res = sensor2.set_i2c_address(0x30)
	print("set i2c address res: ", res)

except Exception as e:
	print(e)

print("sensor1 on again")
eh.output.one.on()

sensor1.start_ranging(1)
sensor2.start_ranging(1)

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
  myLCD.clearScreen()
  exit_handler(None, None)
	
	

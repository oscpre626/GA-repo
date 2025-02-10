import qwiic_vl53l1x
import time
import sys
import explorerhat as eh

print("on")
eh.output.one.on()
mySensor = qwiic_vl53l1x.QwiicVL53L1X()
     
#mySensor.sensor_init()

  
try:
    print("Skriver adress")
    res = mySensor.set_i2c_address(0x30)    # Write configuration bytes to initiate measurement

    print("set ii2c addres res: ", res)

except Exception as e:
    print(e)
    

print("off")
eh.output.one.off()


sensor1 = qwiic_vl53l1x.QwiicVL53L1X(address=0x29)
sensor2 = qwiic_vl53l1x.QwiicVL53L1X(address=0x30)
     
sensor2.sensor_init()
sensor1.sensor_init()
  
while True:
    try:
        sensor1.start_ranging()    # Write configuration bytes to initiate measurement
        sensor2.start_ranging()    # Write configuration bytes to initiate measurement
        time.sleep(.005)
        distance1 = sensor1.get_distance()      # Get the result of the measurement from the sensor
        distance2 = sensor2.get_distance()      # Get the result of the measurement from the sensor
        time.sleep(.005)
        sensor1.stop_ranging()
        sensor2.stop_ranging()

        print("Distance(mm) (1,2): (",distance1, ",",distance2, ")")

    except Exception as e:
        print(e)

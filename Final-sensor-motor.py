
import qwiic_vl53l1x
import time
import sys
import explorerhat as eh
import qwiic_serlcd

print("on")
eh.output.one.on()
mySensor = qwiic_vl53l1x.QwiicVL53L1X()
myLCD = qwiic_serlcd.QwiicSerlcd()     
     
#mySensor.sensor_init()

  
try:
    print("Skriver adress")
    res = mySensor.set_i2c_address(0x30)    # Write configuration bytes to initiate measurement

    print("set ii2c addres res: ", res)

except Exception as e:
    print(e)
    

print("off")
eh.output.one.off()
myLCD.clearScreen()

sensor1 = qwiic_vl53l1x.QwiicVL53L1X(address=0x29)
sensor2 = qwiic_vl53l1x.QwiicVL53L1X(address=0x30)
     
sensor2.sensor_init()
sensor1.sensor_init()
  
while True:
    try:
        sensor1.start_ranging()    # Write configuration bytes to initiate measurement
        sensor2.start_ranging()    # Write configuration bytes to initiate measurement
        time.sleep(.05)
        distance1 = sensor1.get_distance()      # Get the result of the measurement from the sensor
        distance2 = sensor2.get_distance()      # Get the result of the measurement from the sensor
        time.sleep(.05)
        sensor1.stop_ranging()
        sensor2.stop_ranging()
        
        eh.motor.forwards(50)
        y = str(distance1)
        x = str(distance2)
        
        if distance1 < 100:
            eh.motor.one.forwards(25)
        
        
        if distance2 < 100:
            eh.motor.two.forwards(25)
        
        time.sleep(.05)
        myLCD.clearScreen()
        myLCD.print(y + "," + x)
        
        print("Distance(mm) (1,2): (",distance1, ",",distance2, ")")
    except Exception as e:
        print(e)

  

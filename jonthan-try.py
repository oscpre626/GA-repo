import qwiic_vl53l1x
import RPi.GPIO as GPIO
import explorerhat as eh

print("on")
eh.output.one.on()
mySensor = qwiic_vl53l1x.QwiicVL53L1X()

mySensor.sensor_init()
try:
	print("Skiver adress")
	res = mySensor.set_i2c_address(0x29)
	
	print("set i2c addres res: ", res)

except Exception as e:
	print(e)
	
print("off")
eh.output.one.off()		

#XSHUT_SENSOR1 = 17
#XSHUT_SENSOR2 = 27

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(XSHUT_SENSOR1, GPIO:OUT) 
#GPIO.setup(XSHUT_SENSOR2, GPIO:OUT) 

#GPIO.output(XSHUT_SENSOR1, GPIO:LOW) 
#GPIO.output(XSHUT_SENSOR2, GPIO:LOW) 
#time.sleep(0.1)

#GPIO.output(XSHUT_SENSOR1, GPIO:HIGH) enable sensor 1

#GPIO.output(XSHUT_SENSOR1, GPIO:LOW) disable sensor 1
#GPIO.output(XSHUT_SENSOR2, GPIO:HIGH) enable sensor 2
#time.sleep(0.1)


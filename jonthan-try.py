import qwiic_vl53l1x
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

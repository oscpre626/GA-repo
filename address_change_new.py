import VL53L1X
import RPi.GPIO as GPIO
import time
import explorerhat as eh

XSHUT = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(XSHUT,GPIO.OUT)

GPIO.output(XSHUT,GPIO.LOW)

time.sleep(1)

VL53L1X.VL53L1X().change_address(new_address = 0x29)

time.sleep(1)

tof = VL53L1X.VL53L1X(i2c_bus=0, i2c_address=0x29)

tof.open()

GPIO.output(XSHUT,GPIO.HIGH)

time.sleep(1)

tof.start_ranging(1) 
distance_in_mm = tof.get_distance() 
tof.stop_ranging() 

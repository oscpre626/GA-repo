import VL53L1X
import RPi.GPIO as GPIO
import time
import explorerhat as eh

XSHUT = 6

eh.XSHUT.off()

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

tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
distance_in_mm = tof.get_distance() # Grab the range in mm
tof.stop_ranging() # Stop ranging

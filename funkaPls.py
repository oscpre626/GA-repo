import VL53L1X
import explorerhat as eh
import sleep

XSHUT_PIN1 = eh.output.one
#XSHUT_PIN2 = eh.output.two behövs inte för att ändra i2c-adress

# default adress är 0x29
#SENSOR1_NEWADDRESS = 0x29
SENSOR2_NEWADDRESS = 0x30

SENSOR1 = VL53L1X.VL53L1x()
SENSOR2 = VL53L1X.VL53L1x()

XSHUT_PIN1.off()

SENSOR2.change_address(SENSOR2_NEWADDRESS)
XSHUT_PIN1.on()
time.sleep(0.1)

SENSOR1.begin()
SENSOR2.begin()

SENSOR1.start_ranging()
SENSOR2.start_ranging()

#skapa någon loop
SENSOR1.get_distance()
SENSOR2.get_distance()
time.sleep(0.1)

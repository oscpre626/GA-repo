import qwiic_vl53l1x
import qwiic_serlcd
import time
import explorerhat as eh
import smbus
import serial

ser = serial.Serial("/dev/serial0", baudrate=57600, timeout=1)

i2c_bus = smbus.SMBus(1)

def scan_i2c():
    print("Skannar I2C...")
    for address in range(0x03, 0x78):
        try:
            i2c_bus.write_quick(address)
            print(f" Hittade enhet på: 0x{address:02X}")
        except OSError:
            pass
    
def test_serial():
    ser.write(b"Hello, UART!\n")
    time.sleep(1)
    if ser.in_waiting > 0:
        print(f" UART svar: {ser.readline().decode().strip()}")
        
scan_i2c()
test_serial()

ser.close()

# Standard I2C-adress för VL53L1X är 0x29
NEW_I2C_ADDRESS = 0x32  # Ny adress för andra sensorn
#NEW_I2C_ADDRESS_LCD = 0x72 

XSHUT_SENSOR1 = eh.output.one
XSHUT_SENSOR2 = eh.output.two

# Skapa sensorobjekt
sensor1 = qwiic_vl53l1x.QwiicVL53L1X()
sensor2 = qwiic_vl53l1x.QwiicVL53L1X(NEW_I2C_ADDRESS)

# Skapa LCD-objekt
myLCD = qwiic_serlcd.QwiicSerlcd()

# Initiera LCD
if not myLCD.begin:
    print("Kunde inte hitta LCD-skärmen")
    exit(1)

myLCD.clearScreen()
myLCD.setBacklight(255, 255, 255)  # Vit bakgrund

XSHUT_SENSOR1.off()
XSHUT_SENSOR2.off()
time.sleep(0.1)

XSHUT_SENSOR1.on()
time.sleep(0.1)

#sensor1.set_timing_budget_in_ms(100)

# Initiera första sensorn
if not sensor1.sensor_init():
    print("Sensor 1 kunde inte initieras")
    exit(1)

# Ändra adressen på första sensorn
print("Ändrar adress på Sensor 1 till", hex(NEW_I2C_ADDRESS))
sensor1.set_i2c_address(NEW_I2C_ADDRESS)

time.sleep(0.1)

XSHUT_SENSOR2.on()
time.sleep(0.1)
                                                 
# Initiera andra sensorn på standardadressen
sensor2 = qwiic_vl53l1x.QwiicVL53L1X(0x32)
if not sensor2.sensor_init():
    print("Sensor 2 kunde inte initieras")
    exit(1)

# Starta båda sensorerna
sensor1.start_ranging()
sensor2.start_ranging()

try:
    while True:
        # Hämta avstånd
        dist1 = sensor1.get_distance()
        dist2 = sensor2.get_distance()

        # Skriv ut i terminalen
        print(f"Sensor 1: {dist1} mm | Sensor 2: {dist2} mm")

        # Uppdatera LCD-displayen
        myLCD.clearScreen()
        myLCD.print(f"S1: {dist1}mm  " + " \n "+f" S2: {dist2}mm")   
        
        time.sleep(0.5)  # Uppdateringsfrekvens
except KeyboardInterrupt:
    print("Stoppar mätning")
    sensor1.stop_ranging()
    sensor2.stop_ranging()
    myLCD.clearScreen()
    myLCD.print("Program avslutat")

import qwiic_vl53l1x
import qwiic_serlcd
import time

# Standard I2C-adress för VL53L1X är 0x29
NEW_I2C_ADDRESS = 0x30  # Ny adress för andra sensorn

# Skapa sensorobjekt
sensor1 = qwiic_vl53l1x.QwiicVL53L1X()
sensor2 = qwiic_vl53l1x.QwiicVL53L1X(NEW_I2C_ADDRESS)

# Skapa LCD-objekt
myLCD = qwiic_serlcd.QwiicSerlcd()

# Initiera LCD
if not myLCD.begin():
    print("Kunde inte hitta LCD-skärmen")
    exit(1)

myLCD.clearScreen()
myLCD.setBacklight(255, 255, 255)  # Vit bakgrund

# Initiera första sensorn
if not sensor1.sensor_init():
    print("Sensor 1 kunde inte initieras")
    exit(1)

# Ändra adressen på första sensorn
print("Ändrar adress på Sensor 1")
sensor1.set_i2c_address(NEW_I2C_ADDRESS)
time.sleep(0.1)

# Initiera andra sensorn på standardadressen
sensor2 = qwiic_vl53l1x.QwiicVL53L1X(0x29)
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
        myLCD.print(f"S1: {dist1}mm\nS2: {dist2}mm")
        
        time.sleep(0.5)  # Uppdateringsfrekvens
except KeyboardInterrupt:
    print("Stoppar mätning")
    sensor1.stop_ranging()
    sensor2.stop_ranging()
    myLCD.clearScreen()
    myLCD.print("Program avslutat")

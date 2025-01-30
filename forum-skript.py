import time
import busio
import explorerhat as eh
import qwiic_vl53l1x

# Define shutdown pins
XSHUT_pins = [1,2,3,4]  # GPIO-pins for sensor enable

# Define new I2C addresses
SENSOR_ADDRESSES = [44,45]  # New addresses

def init_sensors():
    #i2c = busio.I2C(eh.SCL, eh.SDA)
    sensors = []
    
    # Set all shutdown pins to LOW to disable all sensors
    for pin in XSHUT_pins:
        eh.DigitalInOut(pin).direction = eh.output.off()
        eh.DigitalInOut(pin).value = False
        time.sleep(0.01)
    
    # Initialize sensors one by one
    for i, pin in enumerate(XSHUT_pins):
        eh.DigitalInOut(pin).value = True  # Power up sensor
        time.sleep(0.01)  # Wait for boot-up
        sensor = VL53L1X(i2c)
        sensor.set_address(SENSOR_ADDRESSES[i])
        sensors.append(sensor)
    
    # Initialize first sensor (default address)
    sensor1 = VL53L0X(i2c)
    sensors.insert(0, sensor1)
    
    return sensors

sensors = init_sensors()

# Start continuous measurement
for sensor in sensors:
    sensor.start_continuous()

while True:
    readings = [sensor.range for sensor in sensors]
    print(','.join(map(str, readings)))
    time.sleep(0.1)

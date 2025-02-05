import time
import board
import busio
from adafruit_vl53l0x import VL53L0X

i2c = busio.I2C(board.SCL, board.SDA)

def set_id(sensor, new_address):
    sensor.set_address(new_address)

def setup_sensors():
    global lox1, lox2
    
    lox1 = VL53L0X(i2c)
    time.sleep(0.1)
    set_id(lox1, 0x30)
    
    lox2 = VL53L0X(i2c)
    time.sleep(0.1)
    set_id(lox2, 0x31)

def read_dual_sensors():
    sensor1 = lox1.range
    sensor2 = lox2.range
    
    print(f"1: {sensor1}mm" if sensor1 is not None else "1: Out of range")
    print(f"2: {sensor2}mm" if sensor2 is not None else "2: Out of range")

def main():
    print("Starting...")
    setup_sensors()
    while True:
        read_dual_sensors()
        time.sleep(0.1)

if __name__ == "__main__":
    main()

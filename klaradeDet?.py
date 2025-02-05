import VL53L1X

addr_current = 0x29
addr_desired1 = 0x30
addr_desired2 = 0x31

tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)

tof1.open()
tof2.open()

tof1.change_address(addr_desired1)
tof2.change_address(addr_desired2)

tof1.close()
tof2.close()

tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_desired1)
tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_desired2)

tof1.open()
tof2.open()

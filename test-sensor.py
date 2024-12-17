Python 3.11.2 (main, Sep 14 2024, 03:00:30) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello vorld")
hello vorld
>>> import qwiic_vl53l1x
>>> import time
>>> import sys
>>> mySensor = qwiic_vl53l1x.QwiicVL53L1X()
>>> mySensor.sensor_init()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mySensor.sensor_init()
  File "/home/ojga/.local/lib/python3.11/site-packages/qwiic_vl53l1x.py", line 651, in sensor_init
    self.status = self.__i2cWrite(self.address, Addr, VL51L1X_DEFAULT_CONFIGURATION[Addr - 0x2D], 1)
  File "/home/ojga/.local/lib/python3.11/site-packages/qwiic_vl53l1x.py", line 1574, in __i2cWrite
    self.status = self._i2c.writeBlock(address, registerMSB, buffer)
  File "/home/ojga/.local/lib/python3.11/site-packages/qwiic_i2c/linux_i2c.py", line 251, in writeBlock
    self._i2cbus.write_i2c_block_data(address, commandCode, tmpVal)
  File "/usr/lib/python3/dist-packages/smbus2/smbus2.py", line 643, in write_i2c_block_data
    ioctl(self.fd, I2C_SMBUS, msg)
OSError: [Errno 5] Input/output error

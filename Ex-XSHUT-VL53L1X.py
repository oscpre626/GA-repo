import VL53L1X
import explorerhat as eh
import time

# 📝 I2C-adresser
I2C_SENSOR1 = 0x29  # Standard I2C-adress
I2C_SENSOR2 = 0x32  # Ny adress för andra sensorn

# ⚡ Explorer HAT: XSHUT för sensorer
XSHUT_SENSOR1 = eh.output.one   # Styr av/på för sensor 1
XSHUT_SENSOR2 = eh.output.two   # Styr av/på för sensor 2

# 🚗 Explorer HAT: Motorer
MOTOR_LEFT = eh.motor.one
MOTOR_RIGHT = eh.motor.two

# 🛑 Explorer HAT: Nödsignal (Buzzer)
#BUZZER = eh.output.four

# 🔻 Stäng av båda sensorerna för att ändra adress
XSHUT_SENSOR1.off()
XSHUT_SENSOR2.off()
time.sleep(0.1)

# 🟢 Starta första sensorn
XSHUT_SENSOR1.on()
time.sleep(0.1)
sensor1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=I2C_SENSOR1)
sensor1.open()
sensor1.start_ranging(1)  # Short mode

# ✏️ Ändra adress på första sensorn
sensor1.set_i2c_address(I2C_SENSOR2)
time.sleep(0.1)

# 🟢 Starta andra sensorn
XSHUT_SENSOR2.on()
time.sleep(0.1)
sensor2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=I2C_SENSOR1)
sensor2.open()
sensor2.start_ranging(1)  # Short mode

# 🚗 Motorstyrning
def stop():
    MOTOR_LEFT.stop()
    MOTOR_RIGHT.stop()
    print("🛑 Stannar")

def move_forward(speed=50):
    MOTOR_LEFT.forward(speed)
    MOTOR_RIGHT.forward(speed)
    print("⬆️ Framåt")

def move_backward(speed=50):
    MOTOR_LEFT.backward(speed)
    MOTOR_RIGHT.backward(speed)
    print("⬇️ Bakåt")

def turn_left(speed=50):
    MOTOR_LEFT.backward(speed)
    MOTOR_RIGHT.forward(speed)
    print("⬅️ Svänger vänster")

def turn_right(speed=50):
    MOTOR_LEFT.forward(speed)
    MOTOR_RIGHT.backward(speed)
    print("➡️ Svänger höger")

# 🔄 Huvudloop
try:
    while True:
        # 📡 Läs avstånd från båda sensorerna
        dist1 = sensor1.get_distance()
        dist2 = sensor2.get_distance()

        print(f"📡 S1: {dist1} mm | S2: {dist2} mm")

        # 🚧 Undvik hinder
        if dist1 < 200 or dist2 < 200:  # Om ett hinder är närmare än 20 cm
            stop()
          #  BUZZER.on()
            time.sleep(0.5)
           # BUZZER.off()

            if dist1 < dist2:
                turn_right(60)  # Svänger höger
            else:
                turn_left(60)   # Svänger vänster
            
            time.sleep(1)
            move_forward(50)

        else:
            move_forward(70)  # Standardhastighet
            
        time.sleep(0.5)

except KeyboardInterrupt:
    print("🛑 Stoppar roboten...")
    sensor1.stop_ranging()
    sensor2.stop_ranging()
    stop()
   # BUZZER.off()

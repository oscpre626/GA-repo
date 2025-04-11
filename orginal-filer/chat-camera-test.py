import qwiic_vl53l1x
import qwiic_serlcd
import explorerhat as eh
import smbus
import time
import csv
from picamera import PiCamera
from datetime import datetime

# 🟢 Starta kamera
camera = PiCamera()
camera.resolution = (1024, 768)

# 📝 CSV-loggfil
csv_file = "/home/pi/Desktop/distance_log.csv"

# 📡 Standard I2C-adresser
DEFAULT_I2C_ADDRESS = 0x29
NEW_I2C_ADDRESS = 0x32  

# ⚡ Explorer HAT kontroll
XSHUT_SENSOR1 = eh.output.one
XSHUT_SENSOR2 = eh.output.two
BUZZER = eh.output.four
MOTOR_LEFT = eh.motor.one
MOTOR_RIGHT = eh.motor.two

# 📟 Initiera LCD
myLCD = qwiic_serlcd.QwiicSerlcd()
if not myLCD.begin():
    print("⛔ Kunde inte hitta LCD!")
    exit(1)

myLCD.clearScreen()
myLCD.setBacklight(255, 255, 255)  

# ❌ Stäng av båda sensorerna innan initiering
XSHUT_SENSOR1.off()
XSHUT_SENSOR2.off()
time.sleep(0.1)

# 🟢 Starta första sensorn
XSHUT_SENSOR1.on()
time.sleep(0.1)
sensor1 = qwiic_vl53l1x.QwiicVL53L1X()

if not sensor1.sensor_init():
    print("⛔ Sensor 1 kunde inte initieras")
    exit(1)

# ✏️ Ändra adressen på sensor 1
sensor1.set_i2c_address(NEW_I2C_ADDRESS)
time.sleep(0.1)

# 🟢 Starta andra sensorn
XSHUT_SENSOR2.on()
time.sleep(0.1)
sensor2 = qwiic_vl53l1x.QwiicVL53L1X(DEFAULT_I2C_ADDRESS)

if not sensor2.sensor_init():
    print("⛔ Sensor 2 kunde inte initieras")
    exit(1)

# ▶️ Starta båda sensorerna
sensor1.start_ranging()
sensor2.start_ranging()

# 📸 Funktion för att ta en bild
def take_picture():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = f"/home/pi/Desktop/image_{timestamp}.jpg"
    camera.capture(image_path)
    print(f"📸 Bild sparad: {image_path}")

# 🎥 Funktion för att spela in video
def record_video(duration=3):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_path = f"/home/pi/Desktop/video_{timestamp}.h264"
    camera.start_recording(video_path)
    print(f"🎥 Spelar in video: {video_path}")
    time.sleep(duration)
    camera.stop_recording()
    print("✅ Video inspelad")

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

try:
    with open(csv_file, "a") as log:
        writer = csv.writer(log)
        writer.writerow(["Timestamp", "Sensor 1 (mm)", "Sensor 2 (mm)"])
        
        while True:
            # 📏 Hämta avstånd
            dist1 = sensor1.get_distance()
            dist2 = sensor2.get_distance()

            # 🖥️ Terminalutskrift
            print(f"📡 S1: {dist1} mm | S2: {dist2} mm")

            # 💾 Logga data
            writer.writerow([datetime.now(), dist1, dist2])

            # 🖥️ Uppdatera LCD
            myLCD.clearScreen()
            myLCD.print(f"S1: {dist1}mm\nS2: {dist2}mm")

            # 🚗 Undvik hinder
            if dist1 < 150 or dist2 < 150:  # Om ett hinder är närmare än 15 cm
                stop()
                BUZZER.on()
                take_picture()
                record_video(3)
                time.sleep(1)

                if dist1 < dist2:
                    turn_right()
                else:
                    turn_left()
                
                time.sleep(1)
                move_forward()
                BUZZER.off()

            else:
                move_forward()
                
            time.sleep(0.5)

except KeyboardInterrupt:
    print("🛑 Stoppar...")
    sensor1.stop_ranging()
    sensor2.stop_ranging()
    myLCD.clearScreen()
    myLCD.print("🔴 Program avslutat")
    stop()
    BUZZER.off()

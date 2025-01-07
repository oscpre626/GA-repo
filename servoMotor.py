# servo_motor test
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup( GPIO.OUT)

p = GPIO.PWM( 50)       # 50 Hz
p.start(0)                  # duty_cycle 
left_angle = 12
center_angle = 5
right_angle = 2

# setAngle 함수
def setAngle(angle):        
    p.ChangeDutyCycle(angle)
    time.sleep(0.5)

try: 
    while True:
        var = input("Enter A/W/D : ")
        if var == 'D' or var == 'd':
            setAngle(right_angle)
        elif var == 'W' or var == 'w':
            setAngle(center_angle)
        elif var == 'A' or var == 'a':
            setAngle(left_angle)
        else:
            p.stop()
            break
        print("--")

except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()

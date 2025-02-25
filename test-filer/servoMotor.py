# servo_motor test
#import RPi.GPIO as GPIO
import time
import explorerhat as eh
import keyboard

#GPIO.setmode(GPIO.BCM)
#GPIO.setup( GPIO.OUT)

#p = GPIO.PWM( 50)       # 50 Hz
#eh.start(0)                  # duty_cycle 
left_angle = 12
center_angle = 5
right_angle = 2

# setAngle 함수
def setAngle(angle):        
    eh.ChangeDutyCycle(angle)
    time.sleep(0.5)

try: 
    
    while True:
        var = input("Enter A/W/D : ")
        if var == 'D' or var == 'd':
            while key.is_pressed('d'):
            #setAngle(right_angle)
                eh.motor.one.forwards()
                eh.motor.two.backwards()
        elif var == 'W' or var == 'w':
            while key.is_pressed('w'):
                eh.motor.one.forwards()
                eh.motor.two.forwards()
            #setAngle(center_angle)
        elif var == 'A' or var == 'a':
            while key.is_pressed('a'):
                eh.motor.one.backwards()
                eh.motor.two.forwards()
            #setAngle(left_angle)
        else:
            #eh.motor.stop()
            break
        print("--")

except KeyboardInterrupt:
    eh.motor.stop()
#GPIO.cleanup()

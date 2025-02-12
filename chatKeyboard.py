from pynput import keyboard
from gpiozero import Motor

# Definiera motorerna
left_motor = Motor(forward=17, backward=18)
right_motor = Motor(forward=22, backward=23)

def on_press(key):
    try:
        if key.char == 'w':
            left_motor.forward()
            right_motor.forward()
            print("Moving forward")
        elif key.char == 's':
            left_motor.backward()
            right_motor.backward()
            print("Moving backward")
        elif key.char == 'a':
            left_motor.backward()
            right_motor.forward()
            print("Turning left")
        elif key.char == 'd':
            left_motor.forward()
            right_motor.backward()
            print("Turning right")
    except AttributeError:
        pass

def on_release(key):
    left_motor.stop()
    right_motor.stop()
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

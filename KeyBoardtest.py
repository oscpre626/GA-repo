from pynput import keyboard
import explorerhat as eh
import time

def on_press(key):
	try: 
			if key.char == 'd':
				eh.motor.one.forwards()
				eh.motor.two.backwards()
			elif key.char == 'w':
				eh.motor.one.forwards()
				eh.motor.two.forwards()
			elif key.char == 'a':
				eh.motor.one.backwards()
				eh.motor.two.forwards()
				time.sleep(0.1)
			
def on_release(key):
	eh.motor.stop()

except AttributeError:
		pass

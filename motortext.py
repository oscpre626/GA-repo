import explorerhat as eh

while True:
	try: 
		eh.motor.forwards()
	except KeyboardInterrupt:
		eh.motor.stop()

		
			

import time
import explorerhat

R1 = 4660
V = 5.125
#ckeaksksks
threshold = 2.5
delay = 0.25

while True:
    V2  = explorerhat.analog.one.read()
    V1 = V - V2
    R2 = V2*(R1/V1)
    print('  {0:5.2f} volts   {1:5.2f} ohms'.format(round(V2,2), round(R2,2)))
    if V2 > threshold:
        explorerhat.output.one.off()
        explorerhat.output.two.on()
    else:
        explorerhat.output.one.on()
        explorerhat.output.two.off()        
    time.sleep(delay)

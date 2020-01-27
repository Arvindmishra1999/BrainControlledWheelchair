import blink
import time
import RPi.GPIO as GPIO
import final

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 8  
ECHO = 10
t1 = 0
t2 = 0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def ultra():
    
    t1 = 0
    t2 = 0
    GPIO.output(TRIG,1)
    time.sleep(0.0001)
    GPIO.output(TRIG,0)
    while GPIO.input(ECHO)== 0:
        t1 = time.time()
    while GPIO.input(ECHO)== 1:
        t2 = time.time()    
    distance = (t2-t1) * 17150
        
    if (distance < 20):
        final.stop()
        print("Stopped                        Too Close")
        time.sleep(2)
    else:
        print("Moving Forward                 Distance = {}".format(distance))
        blink.main()
        
        
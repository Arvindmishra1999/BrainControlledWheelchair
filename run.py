from NeuroPy import NeuroPy
from time import time
from time import sleep
import RPi.GPIO as GPIO

inA1 = 3
inA2 = 5
enA = 7
inB1 = 12
inB2 = 15
enB = 11
#TRIG = 12  
#ECHO = 15  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inA1,GPIO.OUT)
GPIO.setup(inA2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(inB1,GPIO.OUT)
GPIO.setup(inB2,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
#GPIO.setup(TRIG,GPIO.OUT)
#GPIO.setup(ECHO,GPIO.IN)
GPIO.output(inA1,GPIO.LOW)
GPIO.output(inA2,GPIO.LOW)
p=GPIO.PWM(enA,1000)     #1000 /sec.
GPIO.output(inB1,GPIO.LOW)
GPIO.output(inB2,GPIO.LOW)
q=GPIO.PWM(enB,1000)

p.start(85) #25%
q.start(85)

def forward():
    GPIO.output(inA1,1)
    GPIO.output(inA2,0)
    GPIO.output(inB1,1)
    GPIO.output(inB2,0)

def stop():
    GPIO.output(inA1,GPIO.LOW)
    GPIO.output(inA2,GPIO.LOW)
    GPIO.output(inB1,GPIO.LOW)
    GPIO.output(inB2,GPIO.LOW)
    
neuropy = NeuroPy("/dev/rfcomm0")


def attention_level(attention_value):
    t1 = 0
    t2 = 0
    sleep(0.2)
    print "\nAttention level = ", attention_value
    if attention_value > 50:
        print "Moving forward"
        forward()

        '''
        GPIO.output(TRIG,1)
        sleep(0.0001)
        GPIO.output(TRIG,0)
        while GPIO.input(ECHO)== 0:
            t1 = time()
        while GPIO.input(ECHO)== 1:
            t2 = time()    
        distance = (t2-t1) * 17150
        
        if (distance < 20):
            stop()
            print("Stopped                        Too Close")
            sleep(0.5)
        else:
            print("Moving Forward                 Distance = {}".format(distance)) ''' 

        
    else :
        print("Stopped                  Low Attention")
        stop()

neuropy.setCallBack("attention",attention_level) 
neuropy.start() 

try:
    while True:
        sleep(1)
finally:
    neuropy.stop()
    
    


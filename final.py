import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

inR1 = 3
inR2 = 5
enR = 7
inL1 = 13
inL2 = 15
enL = 19
'''TRIG = 8  
ECHO = 10
t1 = 0
t2 = 0'''

'''GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)'''
GPIO.setup(inR1,GPIO.OUT)
GPIO.setup(inR2,GPIO.OUT)
GPIO.setup(enR,GPIO.OUT)
GPIO.setup(inL1,GPIO.OUT)
GPIO.setup(inL2,GPIO.OUT)
GPIO.setup(enL,GPIO.OUT)
GPIO.output(inR1,GPIO.LOW)
GPIO.output(inR2,GPIO.LOW)
p=GPIO.PWM(enR,1000)     #1000 /sec.
GPIO.output(inL1,GPIO.LOW)
GPIO.output(inL2,GPIO.LOW)
q=GPIO.PWM(enL,1000)

p.start(85) #25%
q.start(85)

def forward():
    GPIO.output(inR1,0)
    GPIO.output(inR2,1)
    GPIO.output(inL1,0)
    GPIO.output(inL2,1)
    print "forward"

def forward_left():
    GPIO.output(inR1,0)
    GPIO.output(inR2,0)
    GPIO.output(inL1,0)
    GPIO.output(inL2,1)

def forward_right():
    GPIO.output(inR1,0)
    GPIO.output(inR2,1)
    GPIO.output(inL1,0)
    GPIO.output(inL2,0)

def stop():
    GPIO.output(inR1,0)
    GPIO.output(inR2,0)
    GPIO.output(inL1,0)
    GPIO.output(inL2,0)
    
def speed_low():
    p.ChangeDutyCycle(15)
    q.ChangeDutyCycle(15)
    
def speed_medium():
    p.ChangeDutyCycle(40)
    q.ChangeDutyCycle(40)
    
def speed_high():
    p.ChangeDutyCycle(80)
    q.ChangeDutyCycle(80)
    
'''def ultra():
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
        stop()
        print("Stopped                        Too Close")
        time.sleep(2)
    else:
        print("Moving Forward                 Distance = {}".format(distance))'''
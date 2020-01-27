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
    GPIO.output(inR1,1)
    GPIO.output(inR2,0)
    GPIO.output(inL1,1)
    GPIO.output(inL2,0)
    print "forward"

def forward_left():
    GPIO.output(inR1,0)
    GPIO.output(inR2,0)
    GPIO.output(inL1,1)
    GPIO.output(inL2,0)
    print "left"


def forward_right():
    GPIO.output(inR1,1)
    GPIO.output(inR2,0)
    GPIO.output(inL1,0)
    GPIO.output(inL2,0)
    print "right"

    
while 1:
    forward()
    time.sleep(3)
    forward_left()
    time.sleep(3)
    forward_right()
    time.sleep(3)

from NeuroPy import NeuroPy
import time
from time import sleep
import RPi.GPIO as GPIO

inA1 = 3
inA2 = 5
enA = 7
inB1 = 8
inB2 = 10
enB = 11
TRIG = 12  
ECHO = 15  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inA1,GPIO.OUT)
GPIO.setup(inA2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(inB1,GPIO.OUT)
GPIO.setup(inB2,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
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
t1 = 0
t2 = 0
def attention_level(attention_value):
    sleep(0.2)
    print "\nAttention level = ", attention_value
    if attention_value > 50:
        forward()
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
            #sleep(0.5)
        else:
            print("Moving Forward                 Distance = {}".format(distance))     

        
    else :
        print("Stopped                  Low Attention")
        stop()
    return None

#def on_blink(neuropy,blink_strength):
#    print "blink detected. strength= %s" %blink_strength

global val

def attention_return(attention):
    val = attention
    
neuropy.setCallBack("attention",attention_return)

#neuropy.setCallBack("rawValue",blink_level)
#neuropy.blink_handlers.append(on_blink)

neuropy.start() 
start_time = 0
i = 0
blinked = False
last_blink_time = 0
double_blink = False
triple_blink = False
quadruple_blink = False
quintuple_blink = False

try:
    while True:
        value = neuropy.rawValue #gets the raw brain activity level
        print value
        
        
        if value > 100: #if the raw level gets above 200, which indicates a spike, start the clock
            start_time = time.clock()
        if start_time:
            if value <  -100: #if the spike in brain activity is over
                total_time = time.clock() - start_time #how long the spike was
                start_time = 0
                if 0.010 < total_time < 0.05: #if the spike was a certain length
                    if last_blink_time and time.clock() - last_blink_time < .4: #if the blink occured right after the previous blink
                        double_blink = True
                    last_blink_time = time.clock() #reset the clock
                    i+=1
                    blinked = True
        if blinked and time.clock()-last_blink_time > .41: #if a certain amount of time has passed since the last blink
            if double_blink:
                print "Double Blink"
                sleep(3)
            
            else:
                print "Single Blink"
                sleep(3)
                

            double_blink = blinked = triple_blink= quadruple_blink = quintuple_blink = False
                   
finally:
    neuropy.stop()
    
    



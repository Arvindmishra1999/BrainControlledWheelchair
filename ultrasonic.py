/*
*
* Project Name:     Mindwave Automation - Brain Controlled Wheelchair
* Author List:      Heeral Dedhia, Arvind Sridhar, Poonam Chawda, Arvind Mishra
* Filename:         ultrasonic.py
* Functions:        ultra()
* Global Variables: -
*
*/

import blink
import time
import RPi.GPIO as GPIO
import motor

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#initialaize GPIO pins for ultrasonic sensor
TRIG = 8  
ECHO = 10
t1 = 0 #initial time
t2 = 0 #final time

#set up assigned pins 
GPIO.setup(TRIG,GPIO.OUT) 
GPIO.setup(ECHO,GPIO.IN)

/*
*
* Function Name:    ultra
* Input:            -
* Output:           -
* Logic:            The distance of nearest obstacle is calculated when Wheelchair moves Forward.
*                   If obstacle is within safety radius, Wheelchair stops
* Example Call:     ultrasonic.ultra()
*
*/

def ultra():
    
    t1 = 0
    t2 = 0
    GPIO.output(TRIG,1)
    time.sleep(0.0001)
    GPIO.output(TRIG,0)
    while GPIO.input(ECHO)== 0:
        t1 = time.time() #initial time
    while GPIO.input(ECHO)== 1:
        t2 = time.time() #final time
    distance = (t2-t1) * 17150 #speed of sound is 343m/s
        
    if (distance < 20):
        motor.stop() #stop motors of obstacle too close
        print("Stopped                        Obstacle Too Close")
        time.sleep(2)
    else:
        print("Moving Forward                 Distance = {}".format(distance)) #Print distance of nearest obstacle
        blink.main() #call blinking code
        
        

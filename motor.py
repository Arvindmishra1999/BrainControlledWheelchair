/*
*
* Project Name:     Mindwave Automation - Brain Controlled Wheelchair
* Author List:      Heeral Dedhia, Arvind Sridhar, Poonam Chawda, Arvind Mishra
* Filename:         motor.py
* Functions:        attention_level
* Global Variables: inR1, inR2, enR, inL1, inL2, enL - to specify GPIO pins connected to the motor driver
*
*/

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

#initialize the GPIO pins
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

#initialize the motor PWM
p.start(85) #25%
q.start(85)

/*
*
* Function Name:    forward
* Input:            -
* Output:           forward motion of the motor
* Logic:            Sets the left and right motor for forward motion
* Example Call:     motor.forward()
*
*/

def forward():
    GPIO.output(inR1,0)
    GPIO.output(inR2,1)
    GPIO.output(inL1,0)
    GPIO.output(inL2,1)
    print "forward"


/*
*
* Function Name:    forward_left
* Input:            -
* Output:           left turn motion of the motor
* Logic:            Sets only the right motor and left motor is stationary to turn left
* Example Call:     motor.forward_left()
*
*/

def forward_left():
    GPIO.output(inR1,0)
    GPIO.output(inR2,0)
    GPIO.output(inL1,0)
    GPIO.output(inL2,1)


/*
*
* Function Name:    forward_right
* Input:            -
* Output:           right turn motion of the motor
* Logic:            Sets only the left motor and right motor is stationary to turn right
* Example Call:     motor.forward_right()
*
*/

def forward_right():
    GPIO.output(inR1,0)
    GPIO.output(inR2,1)
    GPIO.output(inL1,0)
    GPIO.output(inL2,0)


/*
*
* Function Name:    stop
* Input:            -
* Output:           motion of wheelchair stops
* Logic:            Resets all pins to stop motion
* Example Call:     motor.stop()
*
*/

def stop():
    GPIO.output(inR1,0)
    GPIO.output(inR2,0)
    GPIO.output(inL1,0)
    GPIO.output(inL2,0)


/*
*
* Function Name:    speed_low
* Input:            -
* Output:           reduce the speed of the wheelchair
* Logic:            Set PWM parameters at a lower value
* Example Call:     motor.speed_low()
*
*/
    
def speed_low():
    p.ChangeDutyCycle(15)
    q.ChangeDutyCycle(15)
  

/*
*
* Function Name:    speed_medium
* Input:            -
* Output:           moderate speed of the wheelchair
* Logic:            Set PWM parameters at a medium value
* Example Call:     motor.speed_medium()
*
*/  

def speed_medium():
    p.ChangeDutyCycle(40)
    q.ChangeDutyCycle(40)


/*
*
* Function Name:    speed_high
* Input:            -
* Output:           high speed of the wheelchair
* Logic:            Set PWM parameters at a high value
* Example Call:     motor.speed_high()
*
*/ 

def speed_high():
    p.ChangeDutyCycle(80)
    q.ChangeDutyCycle(80)

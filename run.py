/*
*
* Project Name: 	Mindwave Automation - Brain Controlled Wheelchair
* Author List: 		Heeral Dedhia, Arvind Sridhar, Poonam Chawda, Arvind Mishra
* Filename: 		run.py
* Functions: 		attention_level
* Global Variables:	av (attention_value), neuropy (object of Neuropy library)
*
*/

from NeuroPy import NeuroPy
import time
import RPi.GPIO as GPIO
import motor
import ultrasonic

neuropy = NeuroPy("/dev/rfcomm0")
av = 0

/*
*
* Function Name: 	attention_level
* Input: 			attention_value (parameter instantiated by setCallBack function from Neuropy library)
* Output: 			-
* Logic: 			Assigns attention value from raw data to variable av, if attention is above threshold
*					chair moves forward, ultrasonic sensor function is called while moving. 
*					Wheelchair stops moving when attention drops or an obstacle is detected. 
* Example Call:		neuropy.setCallBack("attention",attention_level)
*
*/

def attention_level(attention_value):
    neuropy.setCallBack("attention",attention_level)
    av = attention_value
    print "\nAttention level = ", attention_value
    if attention_value > 50:	#check if attention is above threshold
        print "Moving forward"
        motor.forward()	#forward motion of wheelchair
        time.sleep(1)
        ultrasonic.ultra()	#check for obbstacle distance
        
    else :
        print("Stopped                  Low Attention")
        motor.stop()
    return 

/*
*
* Function Name: 	main
* Input: 			-
* Output: 			-
* Logic: 			neuropy object used to create multiple threads by neuropy.start()
* Example Call:		run.main()
*
*/

if __name__=='__main__':
    neuropy.setCallBack("attention",attention_level)
    neuropy.start()
    

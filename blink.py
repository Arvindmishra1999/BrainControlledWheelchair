/*
*
* Project Name:     Mindwave Automation - Brain Controlled Wheelchair
* Author List:      Heeral Dedhia, Arvind Sridhar, Poonam Chawda, Arvind Mishra
* Filename:         blink.py
* Functions:        main()
* Global Variables: -
*
*/

from NeuroPy import NeuroPy
import time
import motor

def main():
    neuropy = NeuroPy("/dev/rfcomm0") #instantiate NeuroPy class

    neuropy.start() #start thread
    start_time = 0 
    blinked = False #if blink is detected
    last_blink_time = 0
    double_blink = False
    triple_blink = False
    i = 100
    j = 100

    try:
        while i < 20000:
            i = i + 1 
            value = neuropy.rawValue #gets the raw brain activity level
            print value, "   ", i 
            
            if value > 100: #if the raw level gets above 200, which indicates a spike, start the clock
                start_time = time.clock()
                #print value
            if start_time:
                if value <  -100: #if the spike in brain activity is over
                    total_time = time.clock() - start_time #how long the spike was
                    start_time = 0
                    if 0.01 < total_time < 0.050: #if the spike was a certain length
                        if last_blink_time and time.clock() - last_blink_time < .6: #if the blink occured right after the previous blink
                            if double_blink:
                                triple_blink = True
                            else :
                                double_blink = True
                        last_blink_time = time.clock() #reset the clock
                        i+=1
                        blinked = True
            if blinked and time.clock()-last_blink_time > .61: #if a certain amount of time has passed since the last blink
                if triple_blink:
                    print "Triple blink detected .......... turning left"
                    motor.forward_left()
                    time.sleep(3)
                    motor.forward()
                    break
                
                elif double_blink:
                    print "Double blink detected ........... turning right"
                    motor.forward_right()
                    time.sleep(3)
                    motor.forward()
                    break
                    
                double_blink = blinked = triple_blink = False
        time.sleep(2)
        return
    finally:
        neuropy.stop()

from NeuroPy import NeuroPy
import time
#import blink
import RPi.GPIO as GPIO
import final
import ultrasonic

neuropy = NeuroPy("/dev/rfcomm0")
av = 0

def attention_level(attention_value):
    neuropy.setCallBack("attention",attention_level)
    av = attention_value
    print "\nAttention level = ", attention_value
    #final.ultra()
    if attention_value > 30:
        print "Moving forward"
        final.forward()
        time.sleep(1)
        #blink.main()
        ultrasonic.ultra()
        
        
    else :
        print("Stopped                  Low Attention")
        final.stop()
    return 

if __name__=='__main__':
    neuropy.setCallBack("attention",attention_level)
    neuropy.start()
    
import RPi.GPIO as GPIO     
from time import sleep
GPIO.setwarnings(False)   
import numpy as np


#arr1 = np.array([1,1,1,0,0,0])


#___첫번째 레지스터___
pin_data1 = 2  
pin_latch1 = 3 
pin_clock1 = 4         

GPIO.setmode(GPIO.BCM)      
GPIO.setup(pin_data1,GPIO.OUT)         #GPIO 출력설정
GPIO.setup(pin_latch1,GPIO.OUT)
GPIO.setup(pin_clock1,GPIO.OUT)



########
def send_byte(states):  #___첫번쨰___
    for s in states:
        GPIO.output(pin_data1, int(s))
        GPIO.output(pin_clock1, True)
        sleep(.01)
        GPIO.output(pin_clock1, False)
        GPIO.output(pin_data1, False)
    GPIO.output(pin_latch1, True)
    sleep(.1)
    GPIO.output(pin_latch1, False)



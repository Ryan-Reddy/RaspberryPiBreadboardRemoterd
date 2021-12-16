import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "sr04 print" )

sr04_trig = 20
sr04_echo = 21

GPIO.setup( sr04_trig, GPIO.OUT )
GPIO.setup( sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

def sr04( trig_pin, echo_pin ):
   """
   Return the distance in cm as measured by an SR04
   that is connected to the trig_pin and the echo_pin.
   These pins must have been configured as output and input.s
   """
    
   # send trigger pulse    
   # inplement this step
   
   # wait for echo high and remember its start time
   # inplement this step
   
   # wait for echo low and remember its end time
   # inplement this step
   
   # calculate and return distance
   # inplement this step

while True:
   print( sr04( sr04_trig, sr04_echo ))
   time.sleep( 0.5 )

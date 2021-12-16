import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

led = 18
switch = 23

GPIO.setup( led, GPIO.OUT )
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
while True:
   if( GPIO.input( switch ) ):
      GPIO.output( led, GPIO.HIGH )
   else:
      GPIO.output( led, GPIO.LOW )
   time.sleep( 0.1 )

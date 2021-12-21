import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

led = 18
switch_on_23 = 23
switch_off_24 = 24

GPIO.setup( led, GPIO.OUT )
GPIO.setup(switch_on_23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_on_24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
   if( GPIO.input(switch_on_23)):
      GPIO.output( led, GPIO.HIGH )
   if( GPIO.input(switch_on_24)):
      GPIO.output( led, GPIO.LOW )
   # else:
   #    GPIO.output( led, GPIO.LOW )
   time.sleep( 0.1 )

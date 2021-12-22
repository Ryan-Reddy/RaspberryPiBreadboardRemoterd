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
GPIO.setup(switch_off_24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:

   if( GPIO.input(switch_on_23)):
      GPIO.output( led, GPIO.HIGH )
      GPIO.setup(switch_on_23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   if( GPIO.input(switch_off_24)):
      GPIO.output( led, GPIO.LOW )
      GPIO.setup(switch_on_23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
s

   time.sleep( 0.1 )

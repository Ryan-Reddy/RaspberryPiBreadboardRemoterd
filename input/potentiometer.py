import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

pot = 16

GPIO.setup(pot, GPIO.IN)

while True:

   time.sleep( 0.2 )

   # TODO:
   # I need a analoge to digital convertor to make this work..
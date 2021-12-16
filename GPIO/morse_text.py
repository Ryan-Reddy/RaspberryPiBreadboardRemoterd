import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO morse text" )


def pulse( pin_nr, high_time, low_time ):
   GPIO.output(pin_nr, GPIO.HIGH )
   time.sleep(high_time)
   GPIO.output(pin_nr,GPIO.LOW)
   time.sleep(low_time)


def morse( pin_nr, dot_length, text ):
   for i in text:
      if i == '.':
         pulse(pin_nr, dot_length, dot_length)
      if i == '-':
         pulse(pin_nr, dot_length*3, dot_length)
      if i == ' ':
         time.sleep(dot_length*3)


def morse_text( pin_nr, dot_length, text ):
   morse(pin_nr, dot_length, text)


led = 18
GPIO.setup( led, GPIO.OUT )
morse_text( led, 0.2, "Hello world" )

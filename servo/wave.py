import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "servo wave" )

def pulse(pin_nr, high_time, low_time):
   while True:
      GPIO.output(pin_nr, GPIO.HIGH)
      time.sleep(high_time)
      GPIO.output(pin_nr, GPIO.LOW)
      time.sleep(low_time)

def servo_pulse( pin_nr, position ):
   print('start servo_pulse',pin_nr,position)
   if position == 100:
      flag = 1
      print('flag-max')
   if position == 0:
      flag = 0
      print('flag-min')
   while flag == 0:
      pulse(pin_nr,0.0025/180,0.02)
      print('minimum hit')
   while flag == 1:
      pulse(pin_nr,0.0005/180,0.02)
      print('maximum hit')



   """
   Send a servo pulse on the specified gpio pin 
   that causes the servo to turn to the specified position, and
   then waits 20 ms.
   
   The position must be in the range 0 .. 100.
   For this range, the pulse must be in the range 0.5 ms .. 2.5 ms
   
   Before this function is called, 
   the gpio pin must be configured as output.
   """

   # implementeer deze functie

servo = 25
GPIO.setup( servo, GPIO.OUT )
while True:
   for i in range( 0, 100, 1 ):
      print(i)
      servo_pulse( servo, i )
   for i in range( 100, 0, -1 ):
      print(i)
      servo_pulse( servo, i )
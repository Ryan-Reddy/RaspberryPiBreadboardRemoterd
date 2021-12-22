import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

# ********************************************************************
print( "binair walk 6" )

led_pins = [ 18, 3, 17, 27, 22 ,10]

for gpio in led_pins:
   GPIO.setup( gpio, GPIO.OUT )

def leds( pins, value, delay ):
    for gpio in pins:
        if value % 2 == 1:
           GPIO.output( gpio, GPIO.HIGH )
        else:
           GPIO.output( gpio, GPIO.LOW )
        value = value // 2
    time.sleep( delay )

delay = 0.125
def KITT(switch):
    if switch == True:
        while True:
            leds( led_pins,  1, delay )
            leds( led_pins,  2, delay )
            leds( led_pins,  4, delay )
            leds( led_pins,  8, delay )
            leds( led_pins, 16, delay )
            leds( led_pins, 32, delay )

            leds( led_pins, 32, delay )
            leds( led_pins, 16, delay )
            leds( led_pins,  8, delay )
            leds( led_pins,  4, delay )
            leds( led_pins,  2, delay )
            leds( led_pins,  1, delay )
    if switch == False:
        return

# ********************************************************************
# KITTSWITCH

switch_on_23 = 23
switch_off_24 = 24

GPIO.setup(switch_on_23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_off_24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
   if( GPIO.input(switch_on_23)):
       switch = True
       KITT(switch)

   if( GPIO.input(switch_off_24)):
       switch = False
       KITT(switch)
   time.sleep( 0.1 )






# https://i.ytimg.com/vi/QmQRmZkUrVU/maxresdefault.jpg
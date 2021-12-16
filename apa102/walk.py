import time
import RPi.GPIO as GPIO
GPIO.setmode( GPIO.BCM ) 
GPIO.setwarnings( 0 )

print( "neopixels walk" )

clock_pin = 19
data_pin = 26

GPIO.setup( clock_pin, GPIO.OUT )
GPIO.setup( data_pin, GPIO.OUT )

def apa102_send_bytes( clock_pin, data_pin, bytes ):
    """
    zend de bytes naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin
    """
    
    # implementeer deze functie:
    
    # zend iedere byte in bytes:
    #    zend ieder bit in byte:
    #       maak de data pin hoog als het bit 1 is, laag als het 0 is
    #       maak de clock pin hoog
    #       maak de clock pin laag
   

def apa102( clock_pin, data_pin, colors ):
    """
    zend de colors naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin
    
    De colors moet een list zijn, met ieder list element een list van 3 integers,
    in de volgorde [ blauw, groen, rood ].
    Iedere kleur moet in de range 0..255 zijn, 0 voor uit, 255 voor vol aan.
    
    bv: colors = [ [ 0, 0, 0 ], [ 255, 255, 255 ], [ 128, 0, 0 ] ]
    zet de eerste LED uit, de tweede vol aan (wit) en de derde op blauw, halve strekte.
    """
    
    # implementeer deze functie, maak gebruik van de apa102_send_bytes functie
    
    # zend eerst 4 bytes met nullen
    # zend dan voor iedere pixel:
    #    eerste een byte met allemaal enen
    #    dan de 3 bytes met de kleurwaarden
    # zend nog 4 bytes, maar nu met allemaal enen

blue = [ 8, 0, 0 ]
green = [ 0, 255, 0 ]
red = [ 0, 0, 255 ]

def colors( x, n, on, off ):
   result = []
   for i in range( 0, n ):
      if i == x:
           result.append( on )
      else:
           result.append( off )
   return result           

def walk( clock_pin, data_pin, delay, n = 8 ):
   while True:
      for x in range( 0, n ):
         apa102( clock_pin, data_pin, colors( x, n, red, blue ) )
         time.sleep( delay )
      for x in range( n - 2, 0, -1 ):
         apa102( clock_pin, data_pin, colors( x, n, red, blue ) )
         time.sleep( delay )
         
walk( clock_pin, data_pin, 0.03 )         

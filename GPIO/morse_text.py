import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO morse text" )

def pulse( pin_nr, high_time, low_time ):
   """
   Geef een puls op de pin:
   Maak de pin pin_nr hoog, wacht high_time,
   maak de pin laag, en wacht nog low_time
   # copieer hier je pulse implementatie

def morse( pin_nr, dot_length, text ):
   """
   Laat de text horen als morse code.
   De pin_nr is de pin die gebruikt wordt.
   De text mag de volgende characters bevatten: spatie, streepje, punt.
   De dot_length is de lengte van een punt (dot).
   De lengte van de andere characters wordt daar van afgeleid.
   """
   # copieer hier je morse implementatie

def morse_text( pin_nr, dot_length, text ):
   """
   Laat de string s horen als morse code.
   De pin_nr is de pin die gebruikt wordt.
   De text mag de volgende characters bevatten: lowercase letters, spatie.
   De dot_length is de lengte van een punt (dot).
   De lengte van de andere characters wordt daar van afgeleid.
   """
   # implementeer deze functie

led = 18
GPIO.setup( led, GPIO.OUT )
morse_text( led, 0.2, "Hello world" )

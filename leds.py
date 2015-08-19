import pigpio
import urllib2
import json
import time
import sys

def set_leds(leds):
        pi = pigpio.pi()
        pi.set_PWM_dutycycle (17, leds["R"])
        pi.set_PWM_dutycycle (22, leds["G"])
        pi.set_PWM_dutycycle (24, leds["B"])
        pi.stop()
        return

leds = None

while True:
        try:
	        response = urllib2.urlopen("http://fnest.co.uk/api/rackledcolor")
       	 	new_leds = json.load(response)
        	if leds != new_leds:
			leds = new_leds
                	set_leds(leds)

        except:
                set_leds(json.loads('{"R":255,"G":0,"B":0}'))
        time.sleep(.25)

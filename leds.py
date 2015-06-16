import pigpio
import urllib2
import json
import time
import sys

def set_leds(r,g,b):
	pi = pigpio.pi()
	pi.set_PWM_dutycycle (17, r)
	pi.set_PWM_dutycycle (22, g)
	pi.set_PWM_dutycycle (24, b)
	pi.stop()
	return

def fade_on():
	for i in range (0,100):
		set_leds(0,0,i)
	return

while True:
	try:
		response = urllib2.urlopen("http://fnest.co.uk/api/rackledcolor")
		data =  json.load(response)
		set_leds(data["R"],data["G"],data["B"])
	except:
		set_leds(0,255,255)
	time.sleep(.25)

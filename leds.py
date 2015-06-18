import pigpio
import urllib2
import json
import time
import sys

def set_leds(rgb):
	pi = pigpio.pi()
	pi.set_PWM_dutycycle (17, rgb[0])
	pi.set_PWM_dutycycle (22, rgb[1])
	pi.set_PWM_dutycycle (24, rgb[2])
	pi.stop()
	return

led_color = [0,0,0]
new_led_color = [0,0,0]

while True:
	try:
		response = urllib2.urlopen("http://fnest.co.uk/api/rackledcolor")
		data =  json.load(response)
		new_led_color = [data["R"],data["G"],data["B"]]
	except:
		new_led_color = [255,127,0]

	if new_led_color != led_color:
		led_color = new_led_color
		set_leds(led_color)

	time.sleep(.1)
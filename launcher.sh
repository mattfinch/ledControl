#!/bin/sh

sudo ps -ef | grep "python [l]eds.py" | awk '{print $2}' | sudo xargs kill

sudo python leds.py > log 2>&1 & #

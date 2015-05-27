#!/bin/sh
sudo pigpiod
sudo python leds.py > log 2>&1 & #



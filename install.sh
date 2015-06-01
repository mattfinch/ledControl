#!/bin/sh

if [[ $EUID -ne 0 ]]; then
  echo "Uh oh! Are you root?" 1>&2
  exit 1
fi
{
  wget abyz.co.uk/rpi/pigpio/pigpio.zip
  unzip pigpio.zip
  rm pigpio.zip
  cd PIGPIO
  make
  make install
} > /dev/null

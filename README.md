# ledControl
Scripts for controlling RGB LED Strip in my home lab. This runs on a Raspberry Pi, controlling an RGL Led strip via GPIO and some MOSFETs.
##Installation
The install script should install the PIGPIO library, which must be started before the script can run.

##Usage
The script is looking for JSON in the format below. You need to set the URI for your web service to tell the script what color to be.
```
{
  "R":0,
  "G":0,
  "B":255
}
```

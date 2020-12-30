# PixelStick
PixelStick216 with RasPi and GUI on 3.2" SPI-LCD

# Overview

This is a remake of the PixelStick.  
[Original Pixel Stick](http://www.thepixelstick.com)
This is used for long exposure photos.

# Technical background 

It uses a RasPi 3 with a 3.2" Waveshare LCD to control the Stick.  
[Display](https://www.waveshare.com/wiki/3.2inch_RPi_LCD_(B))

It displays Images with a max heigh of 216 pixels in png format.
The Path of the images is configureable in the constructor of prgElements.

The GUI is created in Qt5.

The GUI provides a preview of the image.
The Brightness, the direction and the speed of the Image is configureable during runtime in the menu tab.  
The Button OK starts the screensaver so the Display is completely dark.

The LEDs are WS2811. they are controlled by the Adafruit neopixel library.
[rpi-ws281x Library](https://github.com/rpi-ws281x/rpi-ws281x-python)

If the "FIRE" button is pressed the image gets converted. Then the LED in the button begins to start blinking to show that the convert process is finished.
Then press the button again and the Image Starts. 
If the Button is Pressed during the displaying the image goes black and ends.

# Mechanics
In my version the Stick is 1500mm long and have 216 LEDs.  
The Case for the RasPi, battery and the Handle is 3D Printed.  
The Battery is a Li-Po normally used for Drones and other stuff.  
This creates a very sharp image.
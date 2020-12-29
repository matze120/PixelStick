# PixelStick
PixelStick216 with RasPi and GUI on 3.2" SPI-LCD

This is a remake of the PixelStick
This is used for long exposure photos.

It uses a RasPi 3 with a 3.2" Waveshare LCD to control the Stick.

It displays Images with a max heigh of 216 pixels in png format.
The Path of the images is configureable in the constructor of prgElements.

The GUI is created in Qt5.

The GUI provides a preview of the image.
The Brightness and the display speed of the Image is configureable during runtime.
The Button OK starts the screensaver so the Display is completely dark.

The LEDs are WS2811. they are controlled by the Adafruit neopixel library.

If the "FIRE" button is pressed the image convert process starts. then the LED in the button begins to start blinking to show that the convert process is finished.
Then press the button again and the Image Starts. 
If the Button is Pressed during the displaying the image goes black and ends.

In my version the Stick is 1500mm long and have 216 LEDs.
This creates a very sharp image.



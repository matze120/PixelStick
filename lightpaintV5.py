#!/usr/bin/python

# Light painting with LEDs
# Macrel Fornacon 01.2018
# uses LED stripes WS2812B


import RPi.GPIO as GPIO, Image, time
import spidev
import time
import os
import sys
import signal
from neopixel import *
from display import *

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def blackout():
	print("Blackout")
	for i in range(0, strip.numPixels()):
		strip.setPixelColor(i,Color(0,0,0))
	strip.show()


# LED strip configuration:
LED_COUNT      = 216      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



# Configurable values
filename  = "nofile.png"
dev       = "/dev/spidev0.0"
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 50000

#myFile = "/home/pi/lightpainting/"
myFile = "/home/pi/"
newList = []
listPos = 0

DisplaySpeed = 0.05
Brightness = 255

# GPIO Init
GPIO.setmode(GPIO.BCM)
# for use with a switch to start
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)		#GND Pin for Switch
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#input for Switch
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)		#LED from switch

POR()
LCD_Init()
LCD_Clr()
IO_Init()
IO_Out(0x80)
LCD_Print(0, 'PixelStick')
LCD_Print(1, 'by Marcel ')
time.sleep(5)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()


while True:
	LCD_Print(0, 'Choose File!    ')
	LCD_Print(1, 'Up or Down key  ')
	while GPIO.input(17):
		#print GPIO.input(17)			#Only for debugging
		time.sleep(0.2)
		GPIO.output(22, GPIO.LOW)		#Blink Switch LED used as LifeCycle LED
		time.sleep(0.2)
		GPIO.output(22, GPIO.HIGH)		#Blink Switch LED
		menu = IO_In()
		menu = menu & 0b00011111
		if(menu):
			IO_Out(0x80)
		if(menu == 8):
			LCD_Print(0, 'choose file     ')
			dirList = os.listdir(myFile)

			for sFile in dirList:
				if sFile.find('.png') == -1:
					continue
				newList.append(sFile)
			for sFile in newList:
				print(sFile)

			while True:
				dir = IO_In()
				dir = dir & 0b00011111
				LCD_Print(1, '                ')
				LCD_Print(1, newList[listPos])
				if((dir == 0x08) & ((listPos + 1) != len(newList))):
					listPos = listPos + 1
				if((dir == 0x01) & (listPos != 0)):
					listPos = listPos - 1
				if(dir == 0x10):
					filename = newList[listPos]
					break
				time.sleep(0.2)

		if(menu == 16):
			LCD_Print(0, "Menu             ")
			menu = 0
			while True:
				nav = IO_In()
				nav = nav & 0b00011111
				if(nav == 0x08):
					menu = menu + 1
				if((nav == 0x01) & (menu > 0)):
					menu = menu - 1
				time.sleep(0.2)		#"debouncing"
				#print menu
				if(menu == 0):
					LCD_Print(1, "Blackout        ")				# Blackout
					if(nav == 0x10):
						blackout()
					time.sleep(0.2)
				if(menu == 1):
					LCD_Print(1, "Shutdown        ")
					if(nav == 0x10):
						LCD_Print(0, "Shudown now     ")
						os.system("sudo shutdown -h now")
						sys.exit()
                        
				if(menu == 2):
					LCD_Print(1, "Restart         ")
					if(nav == 0x10):
						LCD_Print(0, "Restart now     ")
						os.system("sudo shutdown -r now")
						sys.exit()
                        
				if(menu == 3):
					LCD_Print(1, "Close Programm  ")
					if(nav == 0x10):
						LCD_Print(0, "Programm ended  ")
						LCD_Print(1, "by User         ")
						sys.exit("Programm ended by user")
                        
				if(menu == 4):
					LCD_Print(1, "Adjust Speed    ")
					if(nav == 0x10):
						LCD_Print(0, " <- -      + -> ")
						LCD_Print(1, "                ")
						while True:
							set = IO_In()
							set = set & 0b00011111
							time.sleep(0.1)
							LCD_Print(1, str(round(DisplaySpeed,4)))
							if(set == 0x02):
								DisplaySpeed = DisplaySpeed - 0.001
							if(set == 0x04):
								DisplaySpeed = DisplaySpeed + 0.001
							if(set == 0x10):
								break
						time.sleep(0.2)

				if(menu == 5):
					LCD_Print(1, "Adjust Brightnes")
					if(nav == 0x10):
                                        	LCD_Print(0, " <- -      + -> ")
                                        	LCD_Print(1, "                ")
						while True:
							set = IO_In()
							set = set & 0b00011111
							time.sleep(0.1)
							LCD_Print(1, str(Brightness))
							if(set == 0x02):
								Brightness = Brightness - 1
							if(set == 0x04):
								Brightness = Brightness + 1
							if(set == 0x10):
								strip.setBrightness(Brightness)
                                        			break
					time.sleep(0.2)

				if(menu == 6):		# Should be the last number of menu items
					LCD_Print(1, "EXIT            ")
					if(nav == 0x10):
						break

	LCD_Clr()
	# Open SPI device, load image in RGB format and get dimensions:
	spidev    = file(dev, "wb")
	print("Loading...")
	LCD_Print(0, 'Loading...')
	img       = Image.open((myFile + filename)).convert("RGB")
	pixels    = img.load()
	width     = img.size[0]
	height    = img.size[1]
	print("%dx%d pixels" % img.size)
	# TODO: add resize here if image is not desired height

	# Calculate gamma correction table.
	gamma = bytearray(256)
	for i in range(256):
		gamma[i] = int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)

	# Create list of bytearrays, one for each column of image.
	# R, G, B byte per pixel, plus extra '0' byte at end for latch.
	print("Allocating...")
	LCD_Print(0, 'Allocating...')
	column = [0 for x in range(width)]
	for x in range(width):
		column[x] = bytearray(height * 3 + 1)

	# Convert 8-bit RGB image into column-wise GBR bytearray list.
	print("Converting...")
	LCD_Print(0, 'Converting...')
	for x in range(width):
		for y in range(height):
			value = pixels[x, y]
			y3 = y * 3
			column[x][y3]     = gamma[value[0]]	#Red 2
			column[x][y3 + 1] = gamma[value[1]]	#Green 0
			column[x][y3 + 2] = gamma[value[2]]	#Blue 1


	LCD_Print(0, "Ready...        ")
        print('Ready...')
	while GPIO.input(17):
		time.sleep(0.1)
		GPIO.output(22, GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(22, GPIO.HIGH)

	while(GPIO.input(17) == 0):
		pass

	# Then it's a trivial matter of writing each column to the strip.
	print("Displaying...")
	LCD_Print(0, 'Displaying...')
	IO_Out(0x00)
	GPIO.output(22, GPIO.LOW)		#Turn Off LED for Displaying
	for x in range(0, width):
		z = 0
		if(GPIO.input(17) == 0):
			blackout()
			break
#			time.sleep(1)

		for y in range(0, height):
			RED = column[x][z]
			GREEN = column[x][z + 1]
			BLUE = column[x][z + 2]
			strip.setPixelColor(y,Color(RED,GREEN,BLUE))
			z = z + 3

		strip.show()
		time.sleep(DisplaySpeed)
	blackout()
        time.sleep(0.1)

spi.close()

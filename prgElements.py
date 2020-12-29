import sys
import os
from PyQt5.QtGui import QIcon, QPixmap
import RPi.GPIO as GPIO, time
from PIL import Image
#import spidev
import time
import signal
from neopixel import *

class prgElement(object):
    def __init__(self, object):
    #constructor
        # LED strip configuration:
        LED_COUNT      = 216      # Number of LED pixels.
        LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
        #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10       # DMA channel to use for generating signal (try 5)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering
        
        self.myFile = "/home/pi/"
        self.newList = []
        self.listPos = 0
        self.Brightness = 255
        self.Speed = 0.05
        self.Controller = object
        '''
        constructor
        '''
        self.updateBrightness(self.Brightness)
        self.updateSpeed(self.Speed)
        self.readImageList()
        self.displayImage()
        self.initGPIO()
        self.setLED()
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()
        
    def readImageList(self):
        dirList = os.listdir(self.myFile)
        for sFile in dirList:
            if sFile.find('.png') == -1:
                continue
            self.newList.append(sFile)
        for sFile in self.newList:
            print(sFile)
            
    def incrListPos(self):
        if(self.listPos < (len(self.newList)-1)):
            self.listPos += 1
        self.displayImage()
        
        
    def decrListPos(self):
        if(self.listPos > 0):
            self.listPos -= 1
        self.displayImage()
    
    def displayImage(self):
        pixmap = QPixmap(self.myFile + self.newList[self.listPos])
        #label.setPixmap(pixmap)
        self.Controller.updatePixmap(pixmap)
        
    def incrBrightness(self, val):
        if(self.Brightness < 255):
            self.Brightness += val
        self.updateBrightness(self.Brightness)
        self.strip.setBrightness(self.Brightness)
        
    def decrBrightness(self, val):
        if(self.Brightness > 0):
            self.Brightness -= val
        self.updateBrightness(self.Brightness)
        self.strip.setBrightness(self.Brightness)
        
    def updateBrightness(self, val):
        self.Controller.updateBrightness(val)
               
    def incrSpeed(self):
        self.Speed += 0.001
        self.updateSpeed(self.Speed)
        
    def decrSpeed(self):
        self.Speed -= 0.001
        self.updateSpeed(self.Speed)
        
    def updateSpeed(self, val):
        self.Controller.updateSpeed(val)
        
    def initGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #input for Switch K1
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #input for Switch K2
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #input for Switch FIRE
        GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)           #LED from switch
        
    def checkGPIO(self):
        if(GPIO.input(18) == 0):
            self.Controller.updateTab(0)
        if(GPIO.input(23) == 0):
            self.Controller.updateTab(1)
        if(GPIO.input(16) == 0):
            #self.loadImage()
            #self.gammaCorrection()
            #self.allocateImage()
            #self.convertImage()
            #self.displayImageStrip()
            self.prepareForDisplaying()
            
    def prepareForDisplaying(self):
        self.loadImage()
        self.gammaCorrection()
        self.allocateImage()
        self.convertImage()
        self.Controller.updateDuration((self.width * self.Speed))
        while(GPIO.input(16) == 1):
            self.setLED()
            time.sleep(0.1)
            self.clearLED()
            time.sleep(0.1)
        while(GPIO.input(16) == 0):
            time.sleep(0.2)
        self.displayImageStrip()
        self.setLED()
            
    def setLED(self):
        GPIO.output(20, GPIO.HIGH)
        
    def clearLED(self):
        GPIO.output(20, GPIO.LOW)
            
    def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

    def blackout(self):
        print("Blackout")
        for i in range(0, self.strip.numPixels()):
            self.strip.setPixelColor(i,Color(0,0,0))
        self.strip.show()
            
    def loadImage(self):
        img       = Image.open((self.myFile + self.newList[self.listPos])).convert("RGB")
        self.pixels    = img.load()
        self.width     = img.size[0]
        self.height    = img.size[1]
        print("%dx%d pixels" % img.size)
        
        # TODO: add resize here if image is not desired height
    
    # Calculate gamma correction table.
    def gammaCorrection(self):
        self.gamma = bytearray(256)
        for i in range(256):
            self.gamma[i] = int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)
    
    # Create list of bytearrays, one for each column of image.
    # R, G, B byte per pixel, plus extra '0' byte at end for latch.
    def allocateImage(self):
        self.column = [0 for x in range(self.width)]
        for x in range(self.width):
            self.column[x] = bytearray(self.height * 3 + 1)
    
    # Convert 8-bit RGB image into column-wise GBR bytearray list.
    def convertImage(self):
        for x in range(self.width):
            for y in range(self.height):
                value = self.pixels[x, y]
                y3 = y * 3
                self.column[x][y3]     = self.gamma[value[0]]    #Red 2
                self.column[x][y3 + 1] = self.gamma[value[1]]    #Green 0
                self.column[x][y3 + 2] = self.gamma[value[2]]    #Blue 1
    
    def displayImageStrip(self):
        for x in range(0, self.width):
            z = 0
            if(GPIO.input(16) == 0):
                self.blackout()
                break

            for y in range(0, self.height):
                RED = self.column[x][z]
                GREEN = self.column[x][z + 1]
                BLUE = self.column[x][z + 2]
                self.strip.setPixelColor(y,Color(RED,GREEN,BLUE))
                z = z + 3

            self.strip.show()
            time.sleep(self.Speed)
        self.blackout()
        time.sleep(0.5)
    
    def startScreensaver(self):
        os.system("xscreensaver-command -activate")
    
        
    def exitSoftware(self):
        sys.exit("Programm ended by user")
        
    def sysShutdown(self):
        os.system("sudo shutdown -h now")
        sys.exit()
        
    def focus(self):
        self.strip.setPixelColor(108, Color(255,0,0))
        self.strip.setPixelColor(88, Color(255,0,0))
        self.strip.setPixelColor(128, Color(255,0,0))
        self.strip.show()
        

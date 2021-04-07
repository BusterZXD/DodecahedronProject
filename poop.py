import board
import neopixel
import time
import argparse
import random

from rpi_ws281x import *

pixels = neopixel.NeoPixel(board.D18, 30)

# 7 per side (35 per panel)(12 panels)
#Destiny color corey(196,35,210)

# LED strip configuration:
LED_COUNT      = 59      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN       = 10    	 # GPIO pin connecwted to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#Standard Colors
# ALL LED OFF
def all_Off():
	for i in range(LED_COUNT):
		pixels[i] = (0, 0, 0)
	
# RED
def red_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (255, 0, 0)
		time.sleep(1)
	all_Off()

# GREEN
def green_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (0, 255, 0)
		time.sleep(1)
	all_Off()
	
# BLUE
def blue_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (0, 0, 255)
		time.sleep(1)
	all_Off()
# WHITE
def white_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (255, 255, 255)
		time.sleep(1)
	all_Off()

#EVEN
def even_CountUp():
	for i in range(LED_COUNT):
		if LED_COUNT % 2==0:
			pixels[i] = (0, 0, 255)
			time.sleep(1)
			pixels[i] = (0, 255, 0)
			time.sleep(1)
			pixels[i] = (255, 0, 0)
			time.sleep(1)
	all_Off()

#ODD
def odd_CountUp():
	for i in range(LED_COUNT):
		if LED_COUNT % 2==1:
			pixels[i] = (0, 0, 255)
			time.sleep(1)
			pixels[i] = (0, 255, 0)
			time.sleep(1)
			pixels[i] = (255, 0, 0)
			time.sleep(1)
	all_Off()

#ALL RANDOM
def all_Random():
	num=random.randint(0,LED_BRIGHTNESS)
	for i in range(LED_COUNT):
		pixels[i] = (num, num, num)
		time.sleep(1)
	all_Off()

#Snake Random color
def snake():
	num=random.randint(0,LED_BRIGHTNESS)
	for i in range(LED_COUNT):
		pixels[i] = (num, num, num)
			if (i +4)<LED_COUNT
				pixels[i +1] = (num, num, num)
				pixels[i +2] = (num, num, num)
				pixels[i +3] = (num, num, num)
				pixels[i +4] = (num, num, num)
	all_Off()

#Flicker (corey color)
def flick():
	for i in range(LED_COUNT):
		for i in range(LED_COUNT):
			pixels[i] = (196, 35, 210):
			if i=LED_COUNT - 1:
				time.sleep(2)
	all_Off()
		
#Flicker (random)
def flickRand():
	for i in range(LED_COUNT):
		for i in range(LED_COUNT):
			num=random.randint(0,LED_BRIGHTNESS)
			pixels[i] = (num, num, num):
			if i=LED_COUNT - 1:
				time.sleep(2)
	all_Off()
	

#Main run area to call functions
running = True;
while running:
	flick()


	
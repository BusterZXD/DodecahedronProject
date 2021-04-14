import board
import neopixel
import time
import argparse
import random

from rpi_ws281x import *

# 7 per side (35 per panel)(12 panels)
#Destiny color corey(196,35,210)

# LED strip configuration:
LED_COUNT	   = 59		 # Number of LED pixels
LED_PIN		   = 18		 # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN	   = 10		 # GPIO pin connecwted to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ	   = 800000	 # LED signal frequency in hertz (usually 800khz)
LED_DMA		   = 10		 # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255	 # Set to 0 for darkest and 255 for brightest
LED_INVERT	   = False	 # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	   = 0		 # set to '1' for GPIOs 13, 19, 41, 45 or 53
Color		   = 255
Faces		   = 6

pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

#Standard Colors
# ALL LED OFF
def all_Off():
	for i in range(LED_COUNT):
		pixels[i] = (0, 0, 0)
	
# RED
def red_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (255, 0, 0)
		time.sleep(0.1)
	all_Off()

# GREEN
def green_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (0, 255, 0)
		time.sleep(0.1)
	all_Off()
	
# BLUE
def blue_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (0, 0, 255)
		time.sleep(0.1)
	all_Off()
# WHITE
def white_CountUp():
	for i in range(LED_COUNT):
		pixels[i] = (255, 255, 255)
		time.sleep(0.1)
	all_Off()

#EVEN
def even_CountUp():
	for i in range(LED_COUNT):
		if LED_COUNT % 2==0:
			pixels[i] = (0, 0, 255)
			time.sleep(0.1)
			pixels[i] = (0, 255, 0)
			time.sleep(0.1)
			pixels[i] = (255, 0, 0)
			time.sleep(0.1)
	all_Off()

#ODD
def odd_CountUp():
	for i in range(LED_COUNT):
		if LED_COUNT % 2==1:
			pixels[i] = (0, 0, 255)
			time.sleep(0.1)
			pixels[i] = (0, 255, 0)
			time.sleep(0.1)
			pixels[i] = (255, 0, 0)
			time.sleep(0.1)
	all_Off()

#ALL RANDOM
def all_Random():
	num1=0
	num2=0
	num3=0
	for i in range(LED_COUNT):
		num1=random.randint(0,Color)
		num2=random.randint(0,Color)
		num3=random.randint(0,Color)
		pixels[i] = (num1, num2, num3)
		time.sleep(1)
	all_Off()

#Snake (pink)
def snake():
	for i in range(LED_COUNT):
		pixels[i] = (255, 0, 240)
		if i<4:
			pixels[i -4] = (0, 0, 0)
			pixels[i -3] = (0, 0, 0)
			pixels[i -2] = (0, 0, 0)
			pixels[i -1] = (0, 0, 0)
	all_Off()

#Flicker (corey color)
def flick():
	for i in range(LED_COUNT):
		for i in range(LED_COUNT):
			pixels[i] = (196, 35, 210)
			if i==LED_COUNT - 1:
				time.sleep(0.1)
	all_Off()
		
#Flicker (random)
def flickRand():
	num1=0
	num2=0
	num3=0
	for i in range(LED_COUNT):
		for i in range(LED_COUNT):
			num1=random.randint(0,Color)
			num2=random.randint(0,Color)
			num3=random.randint(0,Color)
			pixels[i] = (num1, num2, num3)
				if i=LED_COUNT - 1:
					time.sleep(2)
	all_Off()

def wheel(pos):
   # Input a value 0 to 255 to get a color value.
   # The colours are a transition r - g - b - back to r.
	if pos < 0 or pos > 255:
		r = g = b = 0
	elif pos < 85:
		r = int(pos * 3)
		g = int(255 - pos * 3)
		b = 0
	elif pos < 170:
		pos -= 85
		r = int(255 - pos * 3)
		g = 0
		b = int(pos * 3)
	else:
		pos -= 170
		r = 0
		g = int(pos * 3)
		b = int(255 - pos * 3)
	return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def color_chase(wait):
	for i in range(LED_COUNT):
		pixels[i] = (255, 255, 0)
		time.sleep(wait)
		pixels.show()
	time.sleep(0.5)
	all_Off()

def cycleRainbow(wait)
for j in range(255):
	for i in range(LED_COUNT):
		pixel_index = (i * 256 // num_pixels) + j
		pixels[i] = wheel(pixel_index & 255)
		pixels.show()
		time.sleep(wait)
	all_Off()

#Main run area to call functions
all_Off()
running = True;
while running:
	flick()
	color_chase(0.1)
	cycleRainbow(0.1)
	flickRand()
	all_Random()


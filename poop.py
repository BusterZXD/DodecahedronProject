import board
import neopixel
import time
import argparse
import random

from rpi_ws281x import *

pixels = neopixel.NeoPixel(board.D18, 209)

###########################LED strip configuration###########################################
LED_COUNT      = 209     # Number of LED pixels(210leds).
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN       = 10    	 # GPIO pin connecwted to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 2000000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#####################LED List########################################################
####Bottom leds , with middle ring###################################################
ValA           =34 #strip 1-5 (a)
ValB           =62 #strip 6-9 (b)
ValC           =83 #strip 10-12 (c)
ValD           =104 #strip 13-15 (d)
ValE           =125 #strip 16-18 (e)
ValF           =139 #strip 19-20 (f)
####Top leds excluding middle ring###################################################
ValG           =160 #strip 21-23 (g)
ValH           =174 #strip 24-25 (h)
ValI           =188 #strip 26-27 (i)
ValJ           =202 #strip 28-29 (j)
ValK           =209 #strip 30 (k)

############################FUNCTIONS FOR FACES##########################################
####################Subfunctions for each bottom face####################################
def faceA(red,green,blue,delay):
	for i in range(ValA+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceB(red,green,blue,delay):
	for i in range(ValA,ValB+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceC(red,green,blue,delay):
	for i in range(ValB,ValC+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceD(red,green,blue,delay):
	for i in range(ValC,ValD+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceE(red,green,blue,delay):
	for i in range(ValD,ValE+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceF(red,green,blue,delay):
	for i in range(ValE,ValF+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

#########################Subfunctions for each top face#####################################
def faceG(red,green,blue,delay):
	for i in range(ValF,ValG+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceH(red,green,blue,delay):
	for i in range(ValG,ValH+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceI(red,green,blue,delay):
	for i in range(ValH,ValI+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceJ(red,green,blue,delay):
	for i in range(ValI,ValJ+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def faceK(red,green,blue,delay):
	for i in range(ValJ,ValK):
		pixels[i] = (red,green,blue)
		time.sleep(delay)


###############################EDGES#####################################################
##############################Bottom#####################################################
def edge1(red,green,blue,delay): #6
	for i in range(35,41+1): 
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge2(red,green,blue,delay): #9
	for i in range(56,62+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge3(red,green,blue,delay): #12
	for i in range(77,83+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge4(red,green,blue,delay): #15
	for i in range(98,104+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge5(red,green,blue,delay): #18
	for i in range(119,125+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge6(red,green,blue,delay): #20
	for i in range(133,139+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)
###########################TOP##############################################################
def edge7(red,green,blue,delay): #21
	for i in range(140,146+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge8(red,green,blue,delay): #23
	for i in range(154,160+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge9(red,green,blue,delay): #25
	for i in range(168,174+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge10(red,green,blue,delay): #27
	for i in range(182,188+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

def edge11(red,green,blue,delay): #29
	for i in range(196,202+1):
		pixels[i] = (red,green,blue)
		time.sleep(delay)

#########################################RINGS##########################################
##########################################TOP###########################################
def topRing(red,green,blue,delay):
	for i in range(147,153+1): #22
		pixels[i] = (red,green,blue)
	for i in range(161,167+1): #24
		pixels[i] = (red,green,blue)
	for i in range(175,181+1): #26
		pixels[i] = (red,green,blue)
	for i in range(189,195+1): #28
		pixels[i] = (red,green,blue)
	for i in range(203,209): #30
		pixels[i] = (red,green,blue)
	time.sleep(delay)
##########################################MIDDLE#########################################
def middleRing(red,green,blue,delay):
	for i in range(42,48+1): #7
		pixels[i] = (red,green,blue)
	for i in range(49,55+1): #8
		pixels[i] = (red,green,blue)
	for i in range(63,69+1): #10
		pixels[i] = (red,green,blue)
	for i in range(70,76+1): #11
		pixels[i] = (red,green,blue)
	for i in range(84,90+1): #13
		pixels[i] = (red,green,blue)
	for i in range(91,97+1): #14
		pixels[i] = (red,green,blue)
	for i in range(105,111+1): #16
		pixels[i] = (red,green,blue)
	for i in range(112,118+1): #17
		pixels[i] = (red,green,blue)
	for i in range(126,132+1): #19
		pixels[i] = (red,green,blue)
	for i in range(133,139+1): #20
		pixels[i] = (red,green,blue)
	time.sleep(delay)
######################################Bottom##############################################
def bottomRing(red,green,blue,delay):
	for i in range(0,6+1): #1
		pixels[i] = (red,green,blue)
	for i in range(7,13+1): #2
		pixels[i] = (red,green,blue)
	for i in range(14,20+1): #3
		pixels[i] = (red,green,blue)
	for i in range(21,27+1): #4
		pixels[i] = (red,green,blue)
	for i in range(28,34+1): #5
		pixels[i] = (red,green,blue)
	time.sleep(delay)
###############################ALL LED OFF/RESET#########################################
def all_Off():
	pixels.fill((0,0,0))
	#for i in range(LED_COUNT):
		#print("Resetting led", i, "\n")
		
		#pixels[i] = (0, 0, 0)
###########################Main Functions################################################
def solidColor(red,green,blue,delay):
	pixels.fill((red,green,blue))
	#faceA(red,green,blue,delay)
	#faceB(red,green,blue,delay)
	#faceC(red,green,blue,delay)
	#faceD(red,green,blue,delay)
	#faceE(red,green,blue,delay)
	#faceF(red,green,blue,delay)
	#faceG(red,green,blue,delay)
	#faceH(red,green,blue,delay)
	#faceI(red,green,blue,delay)
	#faceJ(red,green,blue,delay)
	#faceK(red,green,blue,delay)
	all_Off()

def solidColorNoOFF(red,green,blue,delay):
	pixels.fill((red,green,blue))
	#faceA(red,green,blue,delay)
	#faceB(red,green,blue,delay)
	#faceC(red,green,blue,delay)
	#faceD(red,green,blue,delay)
	#faceE(red,green,blue,delay)
	#faceF(red,green,blue,delay)
	#faceG(red,green,blue,delay)
	#faceH(red,green,blue,delay)
	#faceI(red,green,blue,delay)
	#faceJ(red,green,blue,delay)
	#faceK(red,green,blue,delay)

	
def rainbow():
	delay=0.001
	faceA(247,16,55,delay)
	faceB(247,16,194,delay)
	faceC(155,16,247,delay)
	faceD(70,16,247,delay)
	faceE(16,194,247,delay)
	faceF(16,247,232,delay)
	faceG(16,247,155,delay)
	faceH(16,247,24,delay)
	faceI(186,247,16,delay)
	faceJ(247,240,16,delay)
	faceK(247,163,16,delay)
	all_Off()

def blinkRanbow():
	for i in range(3):
		delay=0.001
		faceA(247,163,16,delay)
		faceB(247,240,16,delay)
		faceC(186,247,16,delay)
		faceD(16,247,24,delay)
		faceE(16,247,155,delay)
		faceF(16,247,232,delay)
		faceG(16,194,247,delay)
		faceH(70,16,247,delay)
		faceI(155,16,247,delay)
		faceJ(247,16,194,delay)
		faceK(247,16,55,delay)
		all_Off()
	all_Off()

def flashBangRainbow():
	for i in range(20):
		delay=0
		pixels.fill((247,16,55))
		pixels.fill((247,16,194))
		pixels.fill((155,16,247))
		pixels.fill((70,16,247))
		pixels.fill((16,194,247))
		pixels.fill((16,247,232))
		pixels.fill((16,247,155))
		pixels.fill((16,247,24))
		pixels.fill((186,247,16))
		pixels.fill((247,240,16))
		pixels.fill((247,163,16))
		all_Off()
	all_Off()

def flashBang():
	for i in range(20):
		delay=0
		pixels.fill((255,255,255))
		#faceA(255,255,255,delay)
		#faceB(255,255,255,delay)
		#faceC(255,255,255,delay)
		#faceD(255,255,255,delay)
		#faceE(255,255,255,delay)
		#faceF(255,255,255,delay)
		#faceG(255,255,255,delay)
		#faceH(255,255,255,delay)
		#faceI(255,255,255,delay)
		#faceJ(255,255,255,delay)
		#faceK(255,255,255,delay)
		all_Off()
	all_Off()
def pacman(): #fix speed and color
	delay=0
	pixels.fill((255,240,0))
	for i in range(LED_COUNT):
		pixels[i]=(255,255,0)
		if i >=1:
			pixels[i-1]=(0,0,0)
		elif i==0:
			pixels[i]=(0,0,0)
	all_Off()

def doubleRainbow():
	delay=0.1
	for i in range(3):
		time.sleep(0.5)
		if i % 2==0:
			faceA(247,16,55,delay)
			faceB(247,16,194,delay)
			faceC(155,16,247,delay)
			faceD(70,16,247,delay)
			faceE(16,194,247,delay)
			faceF(16,247,232,delay)
			faceG(16,247,155,delay)
			faceH(16,247,24,delay)
			faceI(186,247,16,delay)
			faceJ(247,240,16,delay)
			faceK(247,163,16,delay)
		elif i % 2==1:
			faceA(247,163,16,delay)
			faceB(247,240,16,delay)
			faceC(186,247,16,delay)
			faceD(16,247,24,delay)
			faceE(16,247,155,delay)
			faceF(16,247,232,delay)
			faceG(16,194,247,delay)
			faceH(70,16,247,delay)
			faceI(155,16,247,delay)
			faceJ(247,16,194,delay)
			faceK(247,16,55,delay)
		all_Off()
	all_Off()

def christmasTree():
	for i in range(LED_COUNT):
		if i % 2==0:
			pixels[i]=(255,0,0)
		elif i % 2==1:
			pixels[i]=(0,255,0)
	all_Off()

def thunder():
	pixels.fill((255,255,255))
	time.sleep(1)
	edge7(64,57,255,0)
	edge8(64,57,255,0)
	edge9(64,57,255,0)
	edge10(64,57,255,0)
	edge11(64,57,255,0)
	edge1(64,57,255,0)
	edge2(64,57,255,0)
	edge3(64,57,255,0)
	edge4(64,57,255,0)
	edge5(64,57,255,0)
	edge6(64,57,255,0)
	all_Off()

def dying(): ##issue 
	for i in range(3):
		solidColor(0,255,145,0.01)
		LED_BRIGHTNESS -= 50 #isssue
	for i in range(2):
		solidColor(255,0,9,0.01)
		LED_BRIGHTNESS -= 50 #iisue
	LED_BRIGHTNESS = 255
	all_Off()

def ringsRanbowFlicker():
	topRing(255,0,0,0)
	middleRing(255,162,0,0)
	bottomRing(255,247,0,0)
	all_Off()
	#time.sleep(0.25)
	topRing(128,255,0,0)
	middleRing(0,255,154,0)
	bottomRing(0,255,239,0)
	all_Off()
	#time.sleep(0.25)
	topRing(0,145,255,0)
	middleRing(0,9,255,0)
	bottomRing(145,0,255,0)
	all_Off()
	#time.sleep(0.25)
	topRing(247,0,255,0)
	middleRing(255,0,171,0)
	bottomRing(255,0,77,0)
	all_Off()

def allRandom():
	num1=0
	num2=0
	num3=0
	for i in range(LED_COUNT):
		num1=random.randint(0,255)
		num2=random.randint(0,255)
		num3=random.randint(0,255)
		pixels[i] = (num1,num2,num3)
		#time.sleep(0)
	all_Off()

####################################Gradients####################################################
def fire():
	for i in range(2):
		solidColorNoOFF(236,29,56,0)
		solidColorNoOFF(255,145,18,0)
		solidColorNoOFF(243,157,58,0)
		solidColorNoOFF(239,222,112,0)
		solidColorNoOFF(243,229,100,0)
	all_Off()

def megaTron():
	for i in range(2):
		solidColorNoOFF(198,255,221,0)
		solidColorNoOFF(183,250,132,0)
		solidColorNoOFF(223,250,132,0)
		solidColorNoOFF(251,215,134,0)
		solidColorNoOFF(249,194,122,0)
		solidColorNoOFF(247,121,125,0)
	all_Off()

def jShine():
	for i in range(2):
		solidColorNoOFF(18,194,233,0)
		solidColorNoOFF(123,98,249,0)
		solidColorNoOFF(169,98,249,0)
		solidColorNoOFF(194,98,249,0)
		solidColorNoOFF(229,98,249,0)
		solidColorNoOFF(249,98,239,0)
	all_Off()

def neon():
	for i in range(2):
		solidColorNoOFF(63,8,135,0)
		solidColorNoOFF(106,54,174,0)
		solidColorNoOFF(130,80,196,0)
		solidColorNoOFF(189,68,208,0)
		solidColorNoOFF(215,62,215,0)
		solidColorNoOFF(252,29,215,0)
	all_Off()
#Main run area to call functions
running = True;
while running:
	print("RESETTING LIGHTS")
	all_Off()
	#print("Running: Rainbow")
	#rainbow()
	#print("Running: Blink Rainbow")
	#blinkRanbow()
	#print("Running: FlashBang")
	#flashBang()
	print("Running: Pacman")
	pacman()
	#print("Running: Double Rainbow")
	#doubleRainbow()
	print("Running: Christmas Tree")
	christmasTree()
	flashBangRainbow()
	print("Running: Thunder")
	thunder()
	flashBang()
	#print("Running: Dying")
	#dying()
	print("Running: Rings Rainbow Flicker")
	ringsRanbowFlicker()
	flashBangRainbow()
	print("Running: All Random")
	allRandom()
	flashBang()
	print("--Excicuting Gradients--")
	print("Running: Fire")
	fire()
	flashBangRainbow()
	print("Running: Megatron")
	megaTron()
	flashBang()
	print("Running: JShine")
	jShine()
	flashBangRainbow()
	print("Running: Neon")
	neon()
	flashBang()
	allRandom()
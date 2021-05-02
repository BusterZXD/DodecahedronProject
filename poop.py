import board
import neopixel
import time
import argparse
import random
import numpy as np
import colorsys
import random
import colorsys
import operator
import math

from rpi_ws281x import *
pixelOutput = neopixel.NeoPixel(board.D18, 209, auto_write=False)


# maps
BackwardEdgeMaps  = [0,7,14,21,28,35,42,49,56,63,70,77,84,91,98,105,112,119,126,133,140,147,154,161,168,175,182,189,196,203]
ForwardEdgeMaps   = [6,13,20,27,34,41,48,55,62,69,76,83,90,97,104,111,118,125,132,139,146,153,160,167,174,181,188,195,202,209]
pixelBuffer = [ (0,0,0) ] * 7 * 30
objectList = []

Junction = {
    #source, RIGHT, LEFT, -> direction switch (True / False)

    6:   [[7, False],  [125, True]],
    7:   [[125, False],  [6, False]],
    125: [[6, True],  [7, False]],

    13:  [[ 14, False], [104, True]],
    14:  [[104, False], [ 13, False]],
    104: [[ 13,  True], [ 14, False]],

    20: [[21, False], [83, True]],
    21: [[83, False], [20, False]],
    83: [[20,  True], [21, False]],

    27: [[28, False], [62, True]],
    28: [[62, False], [27, False]],
    62: [[27,  True], [28, False]],

    34: [ [0, False], [35, False]],
     0: [[35,  True], [34, False]],
    35: [[34, False], [ 0,  True]],

    41:  [[139, True], [42, False]],
    42:  [[41, False], [139, False]],
    139: [[42, False], [41, True]],

    48: [[160, True], [49, False]],
    49: [[48, False], [160, False]],
   160: [[49, False], [48, True]],

    55: [[63, False], [56, False]],
    56: [[55, False], [63,  True]],
    63: [[56,  True], [55, False]],

    69: [[174, True], [70, False]],
    70: [[69, False], [174, False]],
    174: [[70, False], [69, True]],

    76: [[84, False], [77, False]],
    77: [[76, False], [84,  True]],
    84: [[77,  True], [76, False]],

    90: [[188, True], [91, False]],
    91: [[90, False], [188, False]],
   188: [[91, False], [90, True]],

    97:  [[105, False], [ 98, False]],
    98:  [[ 97, False], [105,  True]],
    105: [[ 98,  True], [ 97, False]],

    111: [[202, True], [112, False]],
    112: [[111, False], [202, False]],
	202: [[112, False], [111, True]],

    118: [[126, False], [119, False]],
    119: [[118, False], [126,  True]],
    126: [[119, True], [118, False]],

    132: [[140, False], [133, False]],
    133: [[132, False], [140, True]],
	140: [[133, True], [132, False]],

    146: [[147, False], [209, True]],
    147: [[209, False], [146, False]],
	209: [[146, False], [147, False]],

    153: [[154, False], [161, False]],
    154: [[161, True], [153, False]],
	161: [[153, False], [154, True]],

    167: [[168, False], [175, False]],
    168: [[175, True], [167, False]],
	175: [[167, False], [168, True]],

	181: [[189, False], [182, False]],
    182: [[189, True], [181, False]],
	189: [[181, False], [182, True]],

	195: [[196, False], [203, False]],
    196: [[203, True], [195, False]],
	203: [[195, False], [196, True]],

	209: [[146, True], [147, False]],
    147: [[209, False], [146, False]],
	146: [[147, False], [209, True]]

}
 
head = 0

class Firefly:
    
    body = []
    color = (128,128,128)
    direction = 0
    speed = 1
    
    def __init__(self, index, speed):
        self.speed = speed
        if (self.speed == int(self.speed)):
            self.speed += 0.1
            
        self.length = 2 + int(self.speed*30)
        self.body = [index*1.0] * self.length
        self.color = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(random.uniform(0,1), 1, 0.5))
        self.direction = random.randint(0,1)
        
    def Suicide(self):
        del self
        
    def Undraw(self):
        for i in range(self.length):
            pixelOutput[int(round(self.body[i]))] = (0,0,0)
            pixelBuffer[int(round(self.body[i]))] = (0,0,0)

    def moveTrail(self):
        self.body.pop( len(self.body) - 1)
        self.body.insert(0, self.body[0]*1.0)
  
    def Draw(self):
        # update tuples
        for i in range(self.length):
            pixelBuffer[int(round(self.body[i]))] = (
                pixelBuffer[int(round(self.body[i]))][0] + self.color[0]/((i+1)*1.0),
                pixelBuffer[int(round(self.body[i]))][1] + self.color[1]/((i+1)*1.0),
                pixelBuffer[int(round(self.body[i]))][2] + self.color[2]/((i+1)*1.0)
            )
    
    def Update(self):
        
        #  check if we need to turn
        if self.direction == 1:
            if int(round(self.body[head])) in ForwardEdgeMaps:
                if int(round(self.body[head])) in Junction.keys():
                    #left/right choices
                    choices = Junction[int(round(self.body[head]))]
                    thechoice = random.choice(choices)

                    self.moveTrail()
                    self.body[head] += self.speed
                    
                    # jump to next chain
                    fraction = self.body[head] - math.floor(self.body[head])
                    if fraction >= 0.5:
                        self.body[head] = thechoice[0] - (1.0 - fraction)
                        if (thechoice[1] == True):
                            self.direction = not self.direction

            else:
                self.moveTrail()
                self.body[head] += self.speed
                
                
        elif self.direction == 0:
            if int(round(self.body[head])) in BackwardEdgeMaps:
                if int(round(self.body[head])) in Junction.keys():
                    #left/right choices
                    choices = Junction[int(round(self.body[head]))]
                    thechoice = random.choice(choices)
                    self.moveTrail()
                    self.body[head] -= self.speed
                                
                    # jump to next chain
                    fraction = 1.0 - ((self.body[head]-1) % 1)
                    if fraction >= 0.5:
                        self.body[head] = thechoice[0] + (1.0 - fraction)
                        if (thechoice[1] == True):
                            self.direction = not self.direction
                  
                    
            else:
                self.moveTrail()
                self.body[head] -= self.speed
                

def Clear():
    pixelBuffer = [ (0,0,0) ] * 7 * 30
        


    
Clear()
for i in range(0, 7):

    f1 = Firefly((3 + 7*i)%35, random.uniform(0.04, 0.48) )
    objectList.append(f1)

# add speed multiplier here
speedMultiplier = 10

while True:
    
    for ff in objectList:
        ff.Undraw()
    
    for ff in objectList:
        for i in range(0,speedMultiplier):
            ff.Update()
        
    for ff in objectList:
        ff.Draw()
        
    # smart draw
    for i in range(len(pixelBuffer)):
        if (  pixelBuffer[i] != (0,0,0) ):
            pixelOutput[i] = (
                min(255, max(0, int(round(pixelBuffer[i][0])))), 
                min(255, max(0, int(round(pixelBuffer[i][1])))), 
                min(255, max(0, int(round(pixelBuffer[i][2]))))
            )
    
    pixelOutput.show()
    time.sleep(0.001)
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

from rpi_ws281x import *
pixelOutput = neopixel.NeoPixel(board.D18, 209)


# maps
BackwardEdgeMaps  = [1,8,15,22,29]
ForwardEdgeMaps = [7,14,21,28,35]
pixelBuffer = [ (0,0,0) ] * 7 * 30
objectList = []

Junction = {
    7: [8, 99],
    8: [99, 7],
    14: [15, 99],
    15: [99, 14],
    21: [22,99],
    22: [99, 21],
    28: [29, 99],
    29: [99, 28],
    35: [1, 99],
    1: [99, 35]
}

class Firefly:
    
    body = [1,2,3]
    color = (128,128,128)
    direction = 0
    
    def __init__(self, index1,index2,index3):
        self.body = [index1, index2, index3]
        self.color = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(random.uniform(0,1), 0.5, 0.5))
        self.direction = random.randint(0,1)
        
    def Suicide(self):
        del self
        
    def Undraw(self):
        pixelOutput[self.body[1]] = (0,0,0)

    def Draw(self):
        tuple(map(operator.add, pixelBuffer[self.body[1]], self.color))
        
    
    def Update(self):
        
        #  check if we need to turn
        if self.direction == 1:
            if self.body[1] in ForwardEdgeMaps:
                if self.body[1] in Junction.keys():
                    #left/right choices
                    choices = Junction[self.body[1]]
                    print("Firefly A choices", choices)
                    self.body[1] = min(choices)
                    print("Firefly A moved to", self.body[1])
            else:
                self.body[1] += 1
        elif self.direction == 0:
            if self.body[1] in BackwardEdgeMaps:
                if self.body[1] in Junction.keys():
                    #left/right choices
                    choices = Junction[self.body[1]]
                    print("Firefly B choices", choices)
                    self.body[1] = min(choices)
                    print("Firefly B moved to", self.body[1])
            else:
                self.body[1] -= 1
                
        print("Moved to ", self.body[1])
    

def Clear():
    pixelBuffer = [ (0,0,0) ] * 7 * 30
        


# makeabunchof fireflies

#for i in range(1, 1+random.randrange(10)):
#    print(i)
#    
#    index = (4 + i*7)
#    tempFirefly = Firefly(index-1, index, index+1)
#    
#    objectList.append(tempFirefly)
    
Clear()
f1 = Firefly(4,5,6)
objectList.append(f1)

while True:
    
    for ff in objectList:
        ff.Undraw()
    
    for ff in objectList:
        ff.Update()
        
    for ff in objectList:
        ff.Draw()
        
    # smart draw
    for i in range(len(pixelBuffer)):
        if (  pixelBuffer[i] != (0,0,0) ):
            pixelOutput[i] = pixelBuffer[i]
            
    time.sleep(1)
        
        
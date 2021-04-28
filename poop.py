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
pixelOutput = neopixel.NeoPixel(board.D18, 209, auto_write=False)


# maps
BackwardEdgeMaps  = [0,7,14,21,28]
ForwardEdgeMaps   = [6,13,20,27,34]
pixelBuffer = [ (0,0,0) ] * 7 * 30
objectList = []

Junction = {
     6: [7,  99],
     7: [99,  6],
    13: [14, 99],
    14: [99, 13],
    20: [21, 99],
    21: [99, 20],
    27: [28, 99],
    28: [99, 27],
    34: [ 0, 99],
     0: [99, 34]
}

class Firefly:
    
    body = [1,2,3]
    color = (128,128,128)
    direction = 0
    
    def __init__(self, index1,index2,index3):
        self.body = [index1, index2, index3]
        self.color = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(random.uniform(0,1), 1, 0.5))
        self.direction = random.randint(0,1)
        
    def Suicide(self):
        del self
        
    def Undraw(self):
        pixelOutput[self.body[1]] = (0,0,0)
        pixelBuffer[self.body[1]] = (0,0,0)

    def Draw(self):
        # update tuples
        pixelBuffer[self.body[1]] = (
            pixelBuffer[self.body[1]][0] + self.color[0],
            pixelBuffer[self.body[1]][1] + self.color[1],
            pixelBuffer[self.body[1]][2] + self.color[2]
        )
    
    def Update(self):
        
        #  check if we need to turn
        if self.direction == 1:
            if self.body[1] in ForwardEdgeMaps:
                if self.body[1] in Junction.keys():
                    #left/right choices
                    choices = Junction[self.body[1]]
                    #print("Firefly A choices", choices)
                    self.body[1] = min(choices)
                    #print("Firefly A moved to", self.body[1])
            else:
                self.body[1] += 1
        elif self.direction == 0:
            if self.body[1] in BackwardEdgeMaps:
                if self.body[1] in Junction.keys():
                    #left/right choices
                    choices = Junction[self.body[1]]
                    #print("Firefly B choices", choices)
                    self.body[1] = min(choices)
                    #print("Firefly B moved to", self.body[1])
            else:
                self.body[1] -= 1
                
        #print("Moved to ", self.body[1])
    

def Clear():
    pixelBuffer = [ (0,0,0) ] * 7 * 30
        

#2
# makeabunchof fireflies

#for i in range(1, 1+random.randrange(10)):
#    print(i)
#    
#    index = (4 + i*7)
#    tempFirefly = Firefly(index-1, index, index+1)
#    
#    objectList.append(tempFirefly)
    
Clear()
for i in range(0, 12)

    f1 = Firefly(0, (3 + 7*i)%35, 0)
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
            pixelOutput[i] = (
                min(255, pixelBuffer[i][0]), 
                min(255, pixelBuffer[i][1]), 
                min(255, pixelBuffer[i][2])
            )
            
    pixelOutput.show()
    time.sleep(0.001)
        
        
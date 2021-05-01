#import board
#import neopixel
import time
import argparse
import random
import numpy as np
import colorsys
import random
import colorsys
import operator
import math

#from rpi_ws281x import *
pixelOutput = [ (0,0,0) ] * (7 * 30)
#neopixel.NeoPixel(board.D18, 209, auto_write=False)


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
        #for i in range(0, self.length-1):
        #    self.body[self.length-i] = self.body[self.length-(i-1)]
            
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
                    thechoice = min(choices)
                    self.moveTrail()
                    self.body[head] += self.speed
                    
                    # jump to next chain
                    fraction = self.body[head] - math.floor(self.body[head])
                    if fraction >= 0.5:
                        self.body[head] = thechoice - (1.0 - fraction)

            else:
                self.moveTrail()
                self.body[head] += self.speed
                
                
        elif self.direction == 0:
            if int(round(self.body[head])) in BackwardEdgeMaps:
                if int(round(self.body[head])) in Junction.keys():
                    #left/right choices
                    choices = Junction[int(round(self.body[head]))]
                    thechoice = min(choices)
                    self.moveTrail()
                    self.body[head] -= self.speed
                                
                    # jump to next chain
                    fraction = 1.0 - ((self.body[head]-1) % 1)
                    if fraction >= 0.5:
                        self.body[head] = thechoice + (1.0 - fraction)
                  
                    
            else:
                self.moveTrail()
                self.body[head] -= self.speed
                
                
        #print("Moved to ", self.body[1])
    

def Clear():
    pixelBuffer = [ (0,0,0) ] * 7 * 30
        


    
Clear()
for i in range(0, 7):

    f1 = Firefly((3 + 7*i)%35, random.uniform(0.025, 0.48) )
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
            print("i = ", i)
            pixelOutput[i] = (
                min(255, max(0, int(round(pixelBuffer[i][0])))), 
                min(255, max(0, int(round(pixelBuffer[i][1])))), 
                min(255, max(0, int(round(pixelBuffer[i][2]))))
            )
    
    #pixelOutput.show()
    time.sleep(0.005)
        
        
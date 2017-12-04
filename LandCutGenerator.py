import numpy as np
from math import sqrt, cos, pi, ceil
from PIL import Image, ImageColor, ImageDraw

class LandCutGenerator():
    def __init__(self, size):
        self.arr = np.zeros(size)
        self.size = size

    def makeLandCut(self):
        raise NotImplementedError()

    def isInRange(self, index):
        if index < 0 or index >= self.size: return False

        return True

    def getMaxHeight(self):
        __max = self.arr[0]

        for i in range(len(self.arr)):
            if self.arr[i] > __max:
                __max = self.arr[i]

        return int(ceil(__max))

    def generateImage(self):    
        max_height = self.getMaxHeight()
    
        img = Image.new('RGB', (self.size, max_height))
        draw = ImageDraw.Draw(img)

        for index in range(self.size):
            _height = self.arr[index]
            draw.line((index, max_height, index, max_height -_height), fill=(0, 255, 10))   
            
        return img

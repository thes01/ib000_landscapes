import numpy as np
from math import sqrt, cos, pi
from PIL import Image, ImageColor, ImageDraw

class LandCutGenerator():
    def __init__(self, size):
        self.arr = np.zeros(size)
        self.size = size
        self.max_height = 0

    def makeLandCut(self):
        raise NotImplementedError()

    def isInRange(self, index):
        if index < 0 or index >= self.size: return False

        return True

    def generateImage(self):    
        img = Image.new('RGB', (self.size, self.max_height))
        draw = ImageDraw.Draw(img)

        for index in range(self.size):
            _height = self.arr[index]

            draw.line((index, self.max_height, index, self.max_height -_height), fill=(0,255,10))
        
        return img
from random import randint
from PIL import Image, ImageColor, ImageDraw
from LandGenerator import LandGenerator
from Peaks import Peaks

class NewLandGenerator(LandGenerator):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.max_height = 0

    def makeLand(self):
        assert self.height == 1

        current_height = 100
        self.max_height = current_height
        peaks = Peaks()
        peaks.state = 1

        for index in range(self.width):
            current_height += peaks.getRandInt()
            self.arr[index, 0] = current_height

            if current_height > self.max_height:
                self.max_height = current_height

    def previewOneDimensional(self):    
        img = Image.new('RGB', (self.width, self.max_height))
        draw = ImageDraw.Draw(img)

        for index in range(self.width):
            _height = self.arr[index,0]

            draw.line((index, self.max_height, index, self.max_height -_height), fill=(0,255,10))
        
        return img

    def normalizeLand(self):
        assert self.height == 1

        # bad

        for index in range(self.width):
            for _delta in range(-2,2):
                if self.isInRange((index + _delta,0)) and _delta != 0:
                    self.arr[index, 0] += self.arr[index + _delta, 0] // (10)
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
        max_height = current_height
        peaks = Peaks()

        for index in range(self.width):
            current_height += peaks.getRandInt()
            self.arr[index, 0] = current_height

            if index % 100 == 0:
                peaks.state = randint(0,5)

            if current_height > max_height:
                max_height = current_height

    def previewOneDimensional(self):    
        img = Image.new('RGB', (self.width, self.max_height))
        draw = ImageDraw.Draw(img)

        for index in range(self.width):
            _height = self.arr[index,0]

            draw.line((index, self.max_height, index, self.max_height -_height), fill=(0,255,10))
        
        return img
from random import randint
from math import sqrt
from PIL import Image, ImageColor, ImageDraw
from LandGenerator import LandGenerator
from Peaks import Peaks

class NewLandGenerator(LandGenerator):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.max_height = 0

    def makeOneDimensional(self, size: int):
        current_height = 50
        self.max_height = current_height
        peaks = Peaks()
        peaks.state = 1

        result_arr = []

        for index in range(size):
            current_height += peaks.getRandInt()
            result_arr.append(current_height)

            if current_height > self.max_height:
                self.max_height = current_height

        return result_arr

    def normalizeOneDimLand(self, old_arr: list, window_radius = 2):
        new_arr = []

        for index in range(len(old_arr)):
            # if index + 1 < self.width:
            #     self.arr[index,0] = (self.arr[index, 0] + self.arr[index + 1, 0]) / 2
            _new_val = 0
            _count = 0

            for _delta in range(-window_radius, window_radius):
                src_index = index + _delta

                if src_index >= 0 and src_index < len(old_arr):
                    __weight = abs(_delta) ** 1.5

                    _new_val += old_arr[src_index] * __weight
                    _count += __weight

            new_arr.append(_new_val // _count)

        return new_arr

    def makeLand(self):

        horizontal = self.makeOneDimensional(self.width)
        horizontal = self.normalizeOneDimLand(horizontal, 3)

        vertical = self.makeOneDimensional(self.height)
        vertical = self.normalizeOneDimLand(vertical, 3)

        for _x in range(self.width):
            for _y in range(self.height):
                self.arr[_x,_y] = sqrt(horizontal[_x] * vertical[_y])


        # assert self.height == 1

        # current_height = 100
        # self.max_height = current_height
        # peaks = Peaks()
        # peaks.state = 1

        # for index in range(self.width):
        #     current_height += peaks.getRandInt()
        #     self.arr[index, 0] = current_height

        #     if current_height > self.max_height:
        #         self.max_height = current_height

    def previewOneDimensional(self):    
        img = Image.new('RGB', (self.width, self.max_height))
        draw = ImageDraw.Draw(img)

        for index in range(self.width):
            _height = self.arr[index]

            draw.line((index, self.max_height, index, self.max_height -_height), fill=(0,255,10))
        
        return img

    
from random import randint
from math import sqrt
from PIL import Image, ImageColor, ImageDraw
from LandCutGenerator import LandCutGenerator
from Peaks import Peaks

class RandomLandCutGenerator(LandCutGenerator):
    def makeLandCut(self, initial_height = 50):
        current_height = initial_height
        peaks = Peaks()
        peaks.state = 1

        self.arr = []

        for index in range(self.size):
            current_height += peaks.getRandInt()
            self.arr.append(current_height)

    def applySmoothing(self, window_radius = 2):
        new_arr = []

        for index in range(len(self.arr)):
            # if index + 1 < self.width:
            #     self.arr[index,0] = (self.arr[index, 0] + self.arr[index + 1, 0]) / 2
            _new_val = 0
            _count = 0

            for _delta in range(-window_radius, window_radius):
                src_index = index + _delta

                if self.isInRange(src_index):
                    __weight = abs(_delta) ** 1.5

                    _new_val += self.arr[src_index] * __weight
                    _count += __weight

            new_arr.append(_new_val // _count)

        self.arr = new_arr

    # def makeLand(self):

    #     horizontal = self.makeOneDimensional(self.width)
    #     horizontal = self.applySmoothing(horizontal, 3)

    #     vertical = self.makeOneDimensional(self.height)
    #     vertical = self.applySmoothing(vertical, 3)

    #     for _x in range(self.width):
    #         for _y in range(self.height):
    #             self.arr[_x,_y] = sqrt(horizontal[_x] * vertical[_y])

    
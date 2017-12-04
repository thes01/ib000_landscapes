from random import randint
from LandCutGenerator import *
from LandGenerator import *

class CombineLandGenerator(LandGenerator):
    def __init__(self, lcg_horizontal: LandCutGenerator, lcg_vertical: LandCutGenerator):
        self.lcg_horizontal = lcg_horizontal
        self.lcg_vertical = lcg_vertical
        # self.lcg_weights = lcg_weights

        super().__init__(lcg_horizontal.size, lcg_vertical.size)

    # def makeLand(self):
    #     for _x in range(self.width):
    #         for _y in range(self.height):
    #             self.arr[_x,_y] = sqrt(self.lcg_horizontal.arr[_x] + self.lcg_vertical.arr[_y])

    def makeLand(self):
        for _x in range(self.width):
            for _y in range(self.height):
                val_hor = self.lcg_horizontal.arr[int(sqrt(_x * _y))]
                val_ver = self.lcg_vertical.arr[_y]


                # val_third = abs(self.lcg_weights.arr[_x]) // 2

                # weight_hor = self.lcg_weights.arr[_x] + 1
                # weight_ver = self.lcg_weights.arr[self.height - _y - 1] + 1

                self.arr[_x,_y] = sqrt((val_hor - val_ver) ** 2)
                
                # self.arr[_x,_y] = (self.lcg_horizontal.arr[_x] * weight_x + self.lcg_vertical.arr[_y] * weight_y) / (weight_x + weight_y)
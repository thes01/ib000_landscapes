from random import randint
from LandCutGenerator import *
from LandGenerator import *


class CombineLandGenerator(LandGenerator):
    def __init__(self, lcg_horizontal: LandCutGenerator, lcg_vertical: LandCutGenerator):
        self.lcg_horizontal = lcg_horizontal
        self.lcg_vertical = lcg_vertical

        super().__init__(lcg_horizontal.size, lcg_vertical.size)

    def makeLand(self):
        for _x in range(self.width):
            for _y in range(self.height):
                val_hor = self.lcg_horizontal.arr[int(sqrt(_x * _y))]  # non-linear combination
                val_ver = self.lcg_vertical.arr[_y]
                self.arr[_x, _y] = sqrt((val_hor - val_ver) ** 2)  # non-linear combination 

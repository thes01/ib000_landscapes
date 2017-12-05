from random import randint
from math import sqrt, cos, pi
from LandGenerator import LandGenerator


class CircleLandGenerator(LandGenerator):
    def makeLand(self):
        """ add some hills to an empty field """
        for n in range(200):
            _x = randint(0, 299)
            _y = randint(0, 299)
            _size = randint(10, 16) * 8
            _height = randint(1, 15)
            self.addHill((_x, _y), _size, _height)

    def addHill(self, position, size, height, easing="cos"):
        if position[0] < 0 or position[0] >= self.width or position[1] < 0 or position[1] >= self.height:
            raise IndexError("Position out of canvas")

        radius = size // 2
        left_top_corner = (position[0] - radius, position[1] - radius)

        for hill_x in range(size):
            for hill_y in range(size):
                _x = left_top_corner[0] + hill_x
                _y = left_top_corner[1] + hill_y

                if _x >= 0 and _y >= 0 and _x < self.width and _y < self.height:
                    dist = self.distance((_x, _y), position)
                    if dist <= radius:
                        val = self.mapDistance(dist, radius, height, easing)
                        self.arr[_x, _y] += val

    def distance(self, point1, point2):
        delta_x = point1[0] - point2[0]
        delta_y = point1[1] - point2[1]

        return sqrt(delta_x**2 + delta_y**2)

    def mapDistance(self, distance, max_distance, max_value, easing="cos"):
        """ map the distance to 0-max_value """
        if easing == "cos":
            cos_val = (distance / max_distance) * (pi / 2)
            return cos(cos_val) * max_value

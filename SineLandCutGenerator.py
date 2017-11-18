from random import randint
from math import pi, sin, ceil
from LandCutGenerator import *

class SineLandCutGenerator(LandCutGenerator):
    discrete_sines = {} # a dictionary (cache) of key(number of steps) -> list(sine values)

    def __init__(self, size, n_peaks: int, max_height: int):
        self.n_peaks = n_peaks
        self.max_height = max_height

        super().__init__(size)

    def makeLandCut(self):
        peaks = self.generatePeaks()

        step = ceil(self.size / self.n_peaks)

        for peak_index in range(len(peaks) - 1):
            start_val = peaks[peak_index]
            end_val = peaks[peak_index + 1]

            start_index = step * peak_index

            sine_values = self.getDiscreteSineValues(step, start_val, end_val)

            for i in range(step):
                if self.isInRange(start_index + i):
                    self.arr[start_index + i] = int(round(sine_values[i]))

        print(self.arr)

    def generatePeaks(self):
        assert self.n_peaks < self.size

        step = ceil(self.size / self.n_peaks) # ceiling provides that the last point can be outside the area, must handle it in another function

        peaks = []

        for i in range(self.n_peaks + 1):
            peaks.append(randint(0, self.max_height))

        return peaks

    def removeRedundantPeaks(self):
        print("undefined")

    # override max height function because we already know that from the settings
    def getMaxHeight(self):
        return self.max_height

    def getDiscreteSineValues(self, n: int, start_y: int, end_y: int):
        # compute the sine function from pi/2 to 3pi/2 and normalize 
        if n not in self.discrete_sines:
            start_angle = pi / 2
            step = pi / n

            discrete_sine = []

            for i in range(n):
                discrete_sine.append(sin(start_angle + step * i))

            self.discrete_sines[n] = discrete_sine

        middle_y = (start_y + end_y) // 2
        multiplier = abs(start_y - end_y) / 2

        if end_y > start_y:
            multiplier = -multiplier

        result = []

        for i in range(n):
            result.append(self.discrete_sines[n][i] * multiplier + middle_y)

        return result
        
from random import *

class Peaks:
    # STATE_FLAT = 0
    # STATE_DOWNHILL = 1
    # STATE_UPHILL = 2

    def __init__(self):
        self.state = 0

        self.state_parameters = [
            (-1,1),
            (-2,2),
            (-1,3),
            (-2,5),
            (-3,1),
            (-5,2),
        ]

        # seed(10001)

    def getRandInt(self):
        assert self.state < len(self.state_parameters)

        minmax = self.state_parameters[self.state]
        return randint(*minmax)

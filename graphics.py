from SineLandCutGenerator import *
from CombineLandGenerator import *

from random import randint

for index in range(1, 11):

    max1 = randint(100, 300)
    max2 = randint(100, 300)

    n_peaks1 = randint(3, 8)
    n_peaks2 = randint(3, 8)

    landcut_horizontal = SineLandCutGenerator(300, n_peaks1, max1)
    landcut_vertical = SineLandCutGenerator(300, n_peaks2, max2)

    landcut_horizontal.makeLandCut()
    landcut_vertical.makeLandCut()

    final = CombineLandGenerator(landcut_horizontal, landcut_vertical)
    final.makeLand()

    final.generateImage().save('lands/land-{}-{}-{}-{}.bmp'.format(max1, max2, n_peaks1, n_peaks2))
    print(index)


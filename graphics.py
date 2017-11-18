from SineLandCutGenerator import *
from CombineLandGenerator import *

# gen = RandomLandCutGenerator(200)
# gen.applySmoothing(5)

# gen.makeLandCut()

# gen.generateImage().show()

landcut_horizontal = SineLandCutGenerator(300, 5, 100)
landcut_vertical = SineLandCutGenerator(300, 10, 100)
landcut_weights = SineLandCutGenerator(200, 5, 200)

landcut_horizontal.makeLandCut()
landcut_vertical.makeLandCut()
landcut_weights.makeLandCut()

# # landcut_vertical.generateImage().show()

final = CombineLandGenerator(landcut_horizontal, landcut_vertical, landcut_weights)
final.makeLand()

final.generateImage().show()
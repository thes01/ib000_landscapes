from RandomLandCutGenerator import *

gen = RandomLandCutGenerator(200)
gen.applySmoothing(5)

gen.makeLandCut()

gen.generateImage().show()
from SineLandCutGenerator import *

landcut_horizontal = SineLandCutGenerator(300, 7, 300)

landcut_horizontal.makeLandCut()
img = landcut_horizontal.generateImage()

img.show()

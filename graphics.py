from NewLandGenerator import NewLandGenerator
from random import randint

gen = NewLandGenerator(200,200)
gen.makeLand()
# gen.normalizeLand(3)

gen.generateImage().show()

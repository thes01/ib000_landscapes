from NewLandGenerator import NewLandGenerator
from random import randint

gen = NewLandGenerator(1000,1)
gen.makeLand()
gen.normalizeLand()

gen.previewOneDimensional().show()

from NewLandGenerator import NewLandGenerator
from random import randint

gen = NewLandGenerator(3000,1)
gen.makeLand()

gen.previewOneDimensional().show()

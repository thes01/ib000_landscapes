from CircleLandGenerator import CircleLandGenerator
from random import randint

gen = CircleLandGenerator(200,200)
gen.makeLand()

gen.generateImage().show()

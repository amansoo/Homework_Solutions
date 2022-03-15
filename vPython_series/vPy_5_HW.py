import numpy
from vpython import *

my_orb = sphere(radius=1, color=vector(0, 0, 0))

red_value = 0
blue_value = 0
green_value = 0
# Sequence database:

sequence = 1
while True:
    rate(50)
    if sequence == 1:
        for i in numpy.linspace(0, 1, 100):
            rate(40)
            my_orb.color = vector(i, 1, blue_value)
        sequence = 2
        continue
    if sequence == 2:
        for i in numpy.linspace(1, 0, 100):
            rate(40)
            my_orb.color = vector(1, i, blue_value)
        sequence = 3
        continue
    if sequence == 3:
        for i in numpy.linspace(0, 1, 100):
            rate(40)
            my_orb.color = vector(red_value, i, 1)
        sequence = 4
        continue
    if sequence == 4:
        for i in numpy.linspace(1, 0, 100):
            rate(40)
            my_orb.color = vector(red_value, 1, i)
        sequence = 5
        continue
    if sequence == 5:
        for i in numpy.linspace(0, 1, 100):
            rate(40)
            my_orb.color = vector(1, green_value, i)
        sequence = 6
        continue
    if sequence == 6:
        for i in numpy.linspace(1, 0, 100):
            rate(40)
            my_orb.color = vector(i, green_value, 1)
        sequence = 1
        continue

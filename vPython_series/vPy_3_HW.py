import numpy
from vpython import *

line = cylinder(color=color.black, radius=0.5, length=1)
outer_case = cylinder(radius=0.75, length=10, opacity=0.3)
mercury_bath = sphere(pos=vector(-0.25, 0, 0), radius=0.75, opacity=0.3)
while True:
    for line_length in numpy.linspace(1, 10, 500):
        rate(100)
        line.length = line_length
    for line_length in numpy.linspace(10, 1, 500):
        rate(100)
        line.length = line_length
    pass

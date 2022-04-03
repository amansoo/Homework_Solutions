from vpython import *
import numpy as np

arrow_length = 1
shaft_width = 0.04
# The default position is pointing in the xDirection.
# arrow_object = arrow(length=arrow_length, shaftwidth=shaft_width, axis=vector(0, 0, 1), color=color.blue)
# arrow_object_2 = arrow(length=arrow_length, shaftwidth=shaft_width, axis=vector(0, 1, 0), color=color.green)
arrow_object = arrow(length=arrow_length, shaftwidth=shaft_width, 
axis=vector(0, 0, 0), color=color.red)

# I want to change the rotating axis from x-y to y-z and finally to z-x
while True:
    for theta in np.linspace(0, 2 * np.pi, 1000):
        rate(100)
        arrow_object.color = color.red
        arrow_object.axis = vector(arrow_length * cos(theta), arrow_length * sin(theta), 0)
        arrow_object.length = arrow_length
    for theta in np.linspace(0, 2 * np.pi, 1000):
        rate(100)
        arrow_object.color = color.blue
        arrow_object.axis = vector(arrow_length * cos(theta), 0, arrow_length * sin(theta))
        arrow_object.length = arrow_length
    for theta in np.linspace(0, 2 * np.pi, 1000):
        rate(50)
        arrow_object.color = color.green
        arrow_object.axis = vector(0, arrow_length * cos(theta), arrow_length * sin(theta))
        arrow_object.length = arrow_length

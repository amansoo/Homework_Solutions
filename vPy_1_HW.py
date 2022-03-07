from turtle import width
from vpython import *

floor = box(length=10, height=0.1, width=10, pos=vector(0, -5, 0))
ceiling = box(length=10, height=0.1, width=10, pos=vector(0, 5, 0))
wall_left = box(length=1, height = 10, width = 10, pos=vector(-5, 0, 0))
wall_back = box(length=10, height = 10, width = 1, pos=vector(0, 0, -5))
wall_right = box(length=1, height=10, width=10, pos=vector(5, 0, 0))
red_marble = sphere(color=color.red, width=0.5, radius=0.5)
while True:
    pass

from vpython import *

floor = box(size=vector(10, 0.1, 10), pos=vector(0, -5, 0))
ceiling = box(size=vector(10, 0.1, 10), pos=vector(0, 5, 0))
wall_left = box(size=vector(0.1, 10, 10), pos=vector(-5, 0, 0))
wall_back = box(size=vector(10, 10, .1), pos=vector(0, 0, -5))
wall_right = box(size=vector(.1, 10, 10), pos=vector(5, 0, 0))
red_marble = sphere(color=color.red, radius=0.5)

delta_x = .1
delta_y = .1
delta_z = .1
x_pos = 0
y_pos = 0
z_pos = 0
while True:
    rate(10)
    x_pos += delta_x
    y_pos += delta_y
    z_pos += delta_z

    if x_pos + 0.5 >= 5 or x_pos - 0.5 <= -5:
        delta_x *= -1
    if y_pos + 0.5 >= 5 or y_pos - 0.5 <= -5:
        delta_y *= -1
    if z_pos + 0.5 >= 5 or z_pos - 0.5 <= -5:
        delta_z *= -1
    red_marble.pos = vector(x_pos, y_pos, z_pos)

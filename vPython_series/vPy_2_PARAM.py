from vpython import *
wall_thickness = 0.1
wall_length = 7
wall_depth = 2
wall_height = 5
marble_radius = 0.5
# Size deals in (x, y, z)
floor = box(size=vector(wall_length, wall_thickness, wall_depth), pos=vector(0, -wall_height / 2, 0))
ceiling = box(size=vector(wall_length, wall_thickness, wall_depth), pos=vector(0, wall_height / 2, 0))
wall_left = box(size=vector(wall_thickness, wall_height, wall_depth), pos=vector(-wall_length / 2, 0, 0))
wall_back = box(size=vector(wall_length, wall_height, wall_thickness), pos=vector(0, 0, -wall_depth / 2))
wall_right = box(size=vector(wall_thickness, wall_height, wall_depth), pos=vector(wall_length / 2, 0, 0))
red_marble = sphere(color=color.red, radius=marble_radius)

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

    if x_pos + marble_radius >= wall_length / 2 or x_pos - marble_radius <= -wall_length / 2:
        delta_x *= -1
    if y_pos + marble_radius >= wall_height / 2 or y_pos - marble_radius <= -wall_height / 2:
        delta_y *= -1
    if z_pos + marble_radius >= wall_depth / 2 or z_pos - marble_radius <= -wall_depth / 2:
        delta_z *= -1
    red_marble.pos = vector(x_pos, y_pos, z_pos)

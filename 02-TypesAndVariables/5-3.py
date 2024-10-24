###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
import math
a = input('a=')
b = input('b=')
c = input('c=')

cuboid_volume = a * b * c
cuboid_surf_area = 2 * a * b + 2 * b * c + 2 * a * c
print(f'The volume of a cuboid is {cuboid_volume}')
print(f'The surface area of a cuboid is {cuboid_surf_area}')
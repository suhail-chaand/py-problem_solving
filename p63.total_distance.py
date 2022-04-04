#A robot can move toward UP, DOWN, LEFT and RIGHT with a given step. 
#The trace of robot movement is shown as the following: 
#(Note : Take input from console)
#    UP 5
#    DOWN 3
#    LEFT 3
#    RIGHT 2
#Please write a program to compute the distance from the current position 
#after a sequence of movement and original point. 
#If the distance is a float, then just print the nearest integer.

import math

print('Enter number of steps towards,')
up = int(input('UP: '))
down = int(input('DOWN: '))
left = int(input('LEFT: '))
right = int(input('RIGHT: '))

distance_vertical = abs(up - down)
distance_horizontal = abs(left - right)

total_distance = round(math.sqrt(distance_vertical**2 + distance_horizontal**2))

print('Total distance = {} steps'.format(total_distance))
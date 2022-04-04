#Write a program to print the sum of angles of a polygon in degree. 
#Take number of sides input from console. 

def sum_of_angles(n_sides):
    if n_sides<2:
        return 0
    else:
        return (n_sides-2)*180

while True:
    try:
        num_sides = int(input('Enter number of sides of the polygon: '))
        break
    except ValueError:
        print('Invalid input! Try again.')

print('Sum of angles of a polygon of {} sides is {} degrees'.format(num_sides,sum_of_angles(num_sides)))
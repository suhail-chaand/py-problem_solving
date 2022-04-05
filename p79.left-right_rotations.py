#Create a left rotation and a right rotation function that 
#returns all the left rotations and right rotations of a string.
#    leftRotations("abc") ➞ ["abc", "bca", "cab"]
#    rightRotations("abc") ➞ ["abc", "cab", "bca"]

def rotateLeft(string):
    return string[1:len(string)] + string[0]

def rotateRight(string):
    return string[-1] + string[0:len(string)-1]

def leftRotations(string):
    left_rotations = [string]
    for i in range(len(string)-1):
        left_rotations.append(rotateLeft(string))
        string = rotateLeft(string)
    return left_rotations

def rightRotations(string):
    right_rotations = [string]
    for i in range(len(string)-1):
        right_rotations.append(rotateRight(string))
        string = rotateRight(string)
    return right_rotations

my_str = input('Enter a string: ')

print('Left rotations:',leftRotations(my_str))
print('Right rotations:',rightRotations(my_str))
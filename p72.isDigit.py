#Check if a char is digit without using isdigit(); take input from console.

def isDigit(c):
    try:
        int(c)
        return '{} is a digit'.format(c)
    except:
        return '{} is not a digit'.format(c)

char = input('Enter a charachter: ')
print(isDigit(char))
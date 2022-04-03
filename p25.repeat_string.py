#Recursion to repeat a string n number of times
#Create a recursive function that takes two parameters and 
#repeats the string n number of times. 
#The first parameter text is the string to be repeated and 
#the second parameter is the number of times the string is to be repeated.

def repeat_string(string,num):
    if num > 1:
        print(string,end='; ')
        repeat_string(string,num-1)
    else:
        print(string)

my_str = input('Enter a string: ')
n = int(input('n = '))

repeat_string(my_str,n)
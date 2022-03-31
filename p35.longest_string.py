#Define a function that can accept two strings as input and print the string 
#with maximum length in the console.
#If two strings have the same length, then the function should print all strings 
#line by line.

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

#Function
print('Function method--------------------')
def longest(string1,string2):
    if len(string1)>len(string2):
        return string1
    elif len(string2)>len(string1):
        return string2
    else:
        return string1 + '\n' + string2

print(longest(str1,str2))
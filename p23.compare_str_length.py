#Compare strings by count of characters
#Create a function that takes two strings as arguments and 
#returns either True or False depending on whether the total number of characters 
#in the first string is equal to the total number of characters in the second string.

def compare_str_length(string1,string2):
    if len(string1) == len(string2):
        return True
    else:
        return False

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

if compare_str_length(str1,str2):
    print('The strings are of equal length')
else:
    print('The strings are not of equal length')
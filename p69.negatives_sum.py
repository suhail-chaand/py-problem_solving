#Create a function that takes a string containing integers as well as 
#other characters and return the sum of the negative integers only. 
#    Ex: negatives_sum("22 13%14&-11-22 13 12") => -11 + -22 = -33

import re

def negatives_sum(string):
    negatives = re.findall(r'-[0-9]+',string)
    return sum([int(num) for num in negatives])

in_str = input('Enter a string: ')
print('Sum of negatives =',negatives_sum(in_str))
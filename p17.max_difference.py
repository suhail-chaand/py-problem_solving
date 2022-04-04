#Difference of max and min numbers in a list
#Create a function that takes a list and 
#returns the difference between the biggest and smallest numbers.

def largest(li):
    largest = li[0]
    for num in li:
        if largest<num:
            largest=num
    return largest

def smallest(li):
    smallest = li[0]
    for num in li:
        if smallest>num:
            smallest=num
    return smallest

def max_difference(li):
    return largest(li)-smallest(li)

my_list = list(map(int, input('Enter a list of integers: ').split()))

print('Maximum difference =',max_difference(my_list))
#Difference of max and min numbers in a list
#Create a function that takes a list and 
#returns the difference between the biggest and smallest numbers.

def max_difference(li):
    return max(li)-min(li)

my_list = list(map(int, input('Enter a list of integers: ').split()))

print('Maximum difference =',max_difference(my_list))
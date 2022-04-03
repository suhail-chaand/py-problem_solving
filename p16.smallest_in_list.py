#Find the smallest number in a list
#Create a function that takes a list of numbers and 
#returns the smallest number in the list.

def smallest(li):
    return min(li)

my_list = list(map(int,input('Enter a list of integers: ').split()))

print('Smallest number =',smallest(my_list))
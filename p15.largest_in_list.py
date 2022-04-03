#Find the largest number in a list
#Create a function that takes a list of numbers. 
#Return the largest number in the list.

def largest(li):
    return max(li)

my_list = list(map(int,input('Enter a list of integers: ').split()))

print('Largest number =',largest(my_list))
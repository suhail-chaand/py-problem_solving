#Find the largest number in a list
#Create a function that takes a list of numbers. 
#Return the largest number in the list.

def largest(li):
    largest = li[0]
    for num in li:
        if largest<num:
            largest=num
    return largest

my_list = list(map(int,input('Enter a list of integers: ').split()))

print('Largest number =',largest(my_list))
#Get the sum of all list elements
#Create a function that takes a list and returns the sum of all numbers in the list.

def list_sum(li):
    sum = 0
    for num in li:
        sum += num
    return sum

my_list = list(map(int,input('Enter a list of numbers: ').split()))

print('Sum =',list_sum(my_list))

print('Using in-built function-------------------')
print('Sum =',sum(my_list))
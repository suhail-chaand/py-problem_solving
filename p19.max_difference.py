#Maximum Difference
#Given a list of integers, 
#return the difference between the largest and the smallest integers in the list.

def max_difference(li):
    return max(li)-min(li)

my_list = list(map(int, input('Enter a list of integers: ').split()))

print('Maximum difference =',max_difference(my_list))
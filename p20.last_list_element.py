#Return the last element in a list
#Create a function that accepts a list and returns the last item in the list. 
#The list can be either homogeneous or heterogeneous.

def last_element(li):
    return li[-1]

my_list = input('Enter a list: ').split()

print('Last element =',last_element(my_list))
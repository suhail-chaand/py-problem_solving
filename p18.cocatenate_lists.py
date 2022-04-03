#Concatenating two integer lists
#Create a function to concatenate two integer lists.

def concatenate_lists(li1,li2):
    return li1+li2

list1 = list(map(int,input('Enter list 1: ').split()))
list2 = list(map(int,input('Enter list 2: ').split()))

print('=>',concatenate_lists(list1,list2))
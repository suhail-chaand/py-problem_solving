#Modify a tuple

my_tuple = tuple(input('Enter a tuple: ').split())

element, modified = input('Enter the element and the modified version: ').split()

def modify_tuple(t,e,m):
    l = list(t)
    l[l.index(e)] = m
    return tuple(l)

print(modify_tuple(my_tuple,element,modified))
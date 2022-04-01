#Take two list and iterate both lists simultaneously and print output

l1 = input('Enter list 1: ').split()
l2 = input('Enter list 2: ').split()

for e1,e2 in zip(l1,l2):
    print(e1,e2)
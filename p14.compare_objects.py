#Check if obj1 Is Equal to obj2

obj1 = input('Object 1: ')
obj2 = input('Object 2: ')

def compareObjects(o1,o2):
    if o1 == o2:
        if o1 is o2:
            return 'Objects 1 and 2 are the same'
        else:
            return 'Objects 1 and 2 are equal but are not the same'
    else:
        return 'Objects are not equal'

print(compareObjects(obj1,obj2))
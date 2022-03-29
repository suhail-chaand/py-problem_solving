#Return the first element from a list

my_list = list(input('Enter list items: ').split())

#Raw
print('Raw method')
try:
    print('First element = ',my_list[0])
except:
    print('Empty list!')

#Function
print('Function method')

def first_ele(l):
    try:
        return 'First element = {}'.format(l[0])
    except:
        return 'Empty list!'

print(first_ele(my_list))

#OOP
print('OOP method')

class FirstElement:
    def __init__(self,l) -> None:
        self.l=l
    def first_ele(self):
        try:
            return 'First element = {}'.format(self.l[0])
        except:
            return 'Empty list!'

fe = FirstElement(my_list)

print(fe.first_ele())
#Return a string as an integer

in_str = input('Enter a string: ')
print('Type of "{}" is: {}'.format(in_str,type(in_str)))

#Raw
print('Raw method--------------------')
try:
    int_form=int(in_str)
    print('Integer form: {} of type {}'.format(int_form,type(int_form)))
except:
    print('Invalid input!')

#Function
print('Function method--------------------')

def str_int(string):
    try:
        return 'Integer form: {} of type {}'.format(int_form,type(int_form))
    except:
        return 'Invalid input!'

print(str_int(in_str))

#OOP
print('OOP method--------------------')

class StringToInt:
    def __init__(self,string) -> None:
        self.string=string
    def str_int(self):
        try:
            return 'Integer form: {} of type {}'.format(int_form,type(int_form))
        except:
            return 'Invalid input!'

sti = StringToInt(in_str)

print(sti.str_int())
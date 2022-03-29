#Boolean to String
#bool(str) - empty strings evaluate to False, but everything else evaluates to True
bool_val = bool(input('Enter a boolean value: '))
print('"{}" is of type {}'.format(bool_val,type(bool_val)))

#Raw
print('Raw method')
str_val = str(bool_val)
print('String form: {} of type {}'.format(str_val,type(str_val)))

#Function
print('Function method')

def string(boolean):
    sv = str(boolean)
    return 'String form: {} of type {}'.format(sv,type(sv))

print(string(bool_val))

#OOP
print('OOP method')

class StringToBool:
    def __init__(self,boolean) -> None:
        self.boolean=boolean
    def string(self):
        sv = str(self.boolean)
        return 'String form: {} of type {}'.format(sv,type(sv))

stb = StringToBool(bool_val)

print(stb.string())
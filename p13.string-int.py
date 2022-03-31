#Convert string to Integer and vice-versa

str_val = input('String input: ')
try:
    int_val = int(input('Integer input: '))
except:
    print('Invalid integer input!')

#Raw
print('Raw method--------------------')
try:
    str_int = int(str_val)
    print('String to Integer => {} of type {}'.format(str_int,type(str_int)))
except:
    print('Invalid string input!')
try:
    int_str = str(int_val)
    print('Integer to String => {} of type {}'.format(int_str,type(int_str)))
except:
    pass

#Function
print('Function method--------------------')

def integer(string):
    try:
        integer = int(string)
        return 'String to Integer => {} of type {}'.format(integer,type(integer))
    except:
        return 'Invalid string input!'

def string(integer):
    string = str(integer)
    return 'Integer to String => {} of type {}'.format(string,type(string))

print(integer(str_val))
try:
    print(string(int_val))
except:
    pass

#OOP
print('OOP method--------------------')
class StringInteger:
    def integer(self,string):
        try:
            integer = int(string)
            return 'String to Integer => {} of type {}'.format(integer,type(integer))
        except:
            return 'Invalid string input!'

    def string(self,integer):
        string = str(integer)
        return 'Integer to String => {} of type {}'.format(string,type(string))


si = StringInteger()

print(si.integer(str_val))
try:
    print(si.string(int_val))
except:
    pass
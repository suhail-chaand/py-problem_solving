#Divides evenly
#Given two integers, a and b;
#return True if a can be divided evenly by b. Return False otherwise.

def divides_evenly(num1,num2):
    if num1%num2==0:
        return True
    else:
        return False

a = int(input('a = '))
b = int(input('b = '))

if divides_evenly(a,b):
    print('{} evenly divides {}'.format(b,a))
else:
    print('{} does not divide {}'.format(b,a))
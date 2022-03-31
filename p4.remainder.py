#Return the remainder from two numbers

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

#Raw
print('Raw method--------------------')
print('Remainder of {}/{} = {}'.format(num1,num2,num1%num2))

#Function
print('Function method--------------------')

def find_remainder(n1,n2):
    return n1%n2

print('Remainder of {}/{} = {}'.format(num1,num2,find_remainder(num1,num2)))

#OOP
print('OOP method--------------------')

class RemainderOfTwoNumbers:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def find_remainder(self):
        return self.n1%self.n2

rotn = RemainderOfTwoNumbers(num1,num2)

print('Remainder of {}/{} = {}'.format(num1,num2,rotn.find_remainder()))
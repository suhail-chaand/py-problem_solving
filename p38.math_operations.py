#Write a program to perform all basic mathematical operations

num1, num2 = map(float,input('Enter two numbers: ').split())

#Raw
print('Raw method-----------------------')
print('Addition: {} + {} = {}'.format(num1,num2,num1+num2))
print('Subtraction: {} - {} = {}'.format(num1,num2,num1-num2))
print('Multiplication: {} x {} = {}'.format(num1,num2,num1*num2))
try:
    print('Division: {} / {} = {}'.format(num1,num2,num1/num2))
except:
    print('Division: {} / {} = Invalid divisor!'.format(num1,num2))

#Function
print('Function method--------------------')

def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    try:
        return n1/n2
    except:
        return 'Invalid divisor!'

print('Addition: {} + {} = {}'.format(num1,num2,addition(num1,num2)))
print('Subtraction: {} - {} = {}'.format(num1,num2,subtraction(num1,num2)))
print('Multiplication: {} x {} = {}'.format(num1,num2,multiply(num1,num2)))
print('Division: {} / {} = {}'.format(num1,num2,divide(num1,num2)))

#OOP
print('OOP method--------------------')

class MathOperations:
    def addition(self,n1,n2):
        return n1+n2
    def subtraction(self,n1,n2):
        return n1-n2
    def multiply(self,n1,n2):
        return n1*n2
    def divide(self,n1,n2):
        try:
            return n1/n2
        except:
            return 'Invalid divisor!' 

mo = MathOperations()

print('Addition: {} + {} = {}'.format(num1,num2,mo.addition(num1,num2)))
print('Subtraction: {} - {} = {}'.format(num1,num2,mo.subtraction(num1,num2)))
print('Multiplication: {} x {} = {}'.format(num1,num2,mo.multiply(num1,num2)))
print('Division: {} / {} = {}'.format(num1,num2,mo.divide(num1,num2)))
#Write a function to compute 5/0 and use try/except to catch the exceptions

def divide(n1,n2):
    try:
        return 'Quotient = {}'.format(n1/n2)
    except:
        return 'Divisor cannot be ZERO!'

num1 = float(input('Enter dividend: '))
num2 = float(input('Enter divisor: '))

print(divide(num1,num2))
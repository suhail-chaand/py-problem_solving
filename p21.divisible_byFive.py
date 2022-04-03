#Check if an Integer is divisible by five
#Create a function that returns True if an integer is evenly divisible by 5, 
#and False otherwise.

def divisible_byFive(num):
    if num%5==0:
        return True
    else:
        return False

n = int(input('Enter an number: '))

if divisible_byFive(n):
    print('{} is divisible by 5'.format(n))
else:
    print('{} is not divisible by 5'.format(n))
#Return the next number from the integer passed

num = int(input('Enter an Integer: '))

#Raw
print('Raw method--------------------')
if num>=0:
    print('Next integer is',(num+1))
elif num<0:
    print('Next integer is',(num-1))

#Function
print('Function method--------------------')

def find_next_int(n):
    if n>=0:
        return n+1
    elif n<0:
        return n-1

print('Next integer is',find_next_int(num))

#OOP
print('OOP method--------------------')

class NextInt:
    def __init__(self,n) -> None:
        self.n=n
    def find_next_int(self):
        if self.n>=0:
            return self.n+1
        elif self.n<0:
            return self.n-1

ni = NextInt(num)

print('Next integer is',ni.find_next_int())
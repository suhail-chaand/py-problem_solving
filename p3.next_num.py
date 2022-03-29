#Return the Next Number from the Integer Passed

num = int(input('Enter an Integer: '))

#Raw
print('Raw method')
print('Next integer is',(num+1))

#Function
print('Function method')

def find_next_int(n):
    return n+1

print('Next integer is',find_next_int(num))

#OOP
print('OOP method')

class NextInt:
    def __init__(self,n) -> None:
        self.n=n
    def find_next_int(self):
        return self.n+1

ni = NextInt(num)

print('Next integer is',ni.find_next_int())
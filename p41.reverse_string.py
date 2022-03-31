#Write a program which accepts a string from the console and 
#print it in reverse order.

str_in = input('Enter a string: ')

#Raw
print('Raw method--------------------')
rev_str = str_in[::-1]
print('Reversed string:',rev_str)

#Function
print('Function method--------------------')

def reverse(string):
    return string[::-1]

print('Reversed string:',reverse(str_in))

#OOP
print('OOP method--------------------')

class StringReverese:
    def reverse(self,string):
        return string[::-1]

sr = StringReverese()

print('Reversed string:',sr.reverse(str_in))
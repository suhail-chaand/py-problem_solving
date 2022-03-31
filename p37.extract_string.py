#Write a program which accepts a sequence of words separated by whitespace as input 
#and print the words composed of digits only.
#Example 
#Input: 2 cats and 3 dogs
#Output: ['2', '3'] [‘cats’, ‘dogs’]

in_str = input('Enter a string: ')

#Raw
print('Raw method--------------------')
digits = [word for word in in_str.split() if word.isdigit()]
words = [in_str.split()[i] for i in range(len(in_str.split())) 
    if in_str.split()[i-1].isdigit() and i!=0]

print(digits)
print(words)

#Function
print('Function method--------------------')

def extract_digits(string):
    return [word for word in string.split() if word.isdigit()]

def extract_words(string):
    return [string.split()[i] for i in range(len(string.split())) 
        if string.split()[i-1].isdigit() and i!=0]

print(extract_digits(in_str))
print(extract_words(in_str))

#OOP
print('OOP method--------------------')

class ExtractString:
    def __init__(self,string) -> None:
        self.string=string

    def extract_digits(self):
        return [word for word in self.string.split() if word.isdigit()]

    def extract_words(self):
        return [self.string.split()[i] for i in range(len(self.string.split())) 
            if self.string.split()[i-1].isdigit() and i!=0]

es = ExtractString(in_str)

print(es.extract_digits())
print(es.extract_words())
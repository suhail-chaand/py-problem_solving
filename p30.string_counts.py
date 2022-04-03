#Write a program that accepts a sentence 
#and calculate the number of letters and digits
#and also calculates the upper and lower case letters.

sentence = input('Enter a sentence: ')

letters = 0
digits = 0
upper = 0
lower = 0

for l in sentence:
    if l.isalpha():
        letters += 1
    elif l.isdigit():
        digits += 1
    
    if l.isupper():
        upper += 1
    elif l.islower():
        lower += 1

print('Number of letters =',letters)
print('Number of digits =',digits)
print('Number of upper case letters =',upper)
print('Number of lower case letters =',lower)
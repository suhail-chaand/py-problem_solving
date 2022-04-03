#Write a program, which will find all such numbers between 0 and n (both included) 
#such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.
#n: take input from console.

n = int(input('Enter n value: '))

num_list = [str(num) for num in range(0,n+1)]

even_digits = []
for num in num_list:
    even = True
    for d in num:
        if int(d)%2 != 0:
            even = False
    if even:
        even_digits.append(int(num))

print('Numbers from 0 to {} with even digits:\n{}'.format(n,even_digits))
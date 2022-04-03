#Write a program to square each odd number in a list. 
#Take a list that contains at least 20 elements.

my_list = [10, 40, 31, 43, 45, 46, 1, 3, 7, 9, 34, 0, 21, 32, 87, 90, 13, 23, 12, 57, 15, 24]
print('my_list:\n',my_list)

print('Squares of all odd numbers:\n',[num**2 for num in my_list if num%2 != 0])
#Write a program which will find all such numbers which are divisible by 7 
#but are not a multiple of 5. 
#The numbers obtained should be printed in a comma-separated sequence
#on a single line. You can take any range like 2000-4700 or 3800-4900 etc.
#Check if both range numbers are also included in the output.

start, end = map(int,input('Enter a range: ').split('-'))

print('Numbers in the range of {}-{} that are divisible by 7 but are not a multiple of 5\n{}'
.format(start,end,[num for num in range(start,end+1) if num%7==0 and num%5!=0]))
#Create a function that returns the sum of missing numbers.
#sumMissingNumbers([1, 3, 5, 7, 10]) ➞ 29 // 2 + 4 + 6 + 8 + 9

def sumOfMissingNumbers(l):
    missing_numbers = [num for num in range(l[0],l[-1]+1) if num not in l]
    return sum(missing_numbers)

num_list = list(map(int,input('Enter list of numbers: ').split()))

print('Sum of missing numbers is {}'.format(sumOfMissingNumbers(num_list)))    
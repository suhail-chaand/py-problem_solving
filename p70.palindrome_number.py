#70. Write a program to identify if number is palindrome or not.

def isPalindrome(n):
    n_temp = n
    n_reversed = 0
    while n_temp%10 != 0:
        n_reversed = n_reversed*10 + n_temp%10
        n_temp //= 10
    if n_reversed == n:
        return '{} is a Palindrome'.format(n)
    else:
        return '{} is not a Palindrome'.format(n)
        
print(isPalindrome(int(input('Enter a number: '))))
#Write a function that returns the least common multiple (LCM) of two integers.

#LCM of num1 and num2 is the smallest positive integer divisible by both num1 and num2

num1, num2 = map(int,input('Enter two numbers: ').split())

def lcm(n1,n2):
    largest_num = max(n1,n2)
    while True:
        if largest_num%n1==0 and largest_num%n2==0:
            return largest_num
        else:
            largest_num += 1

print('LCM of {} and {} is {}'.format(num1,num2,lcm(num1,num2)))

#Using Recursive Function
print('Using Recursive function--------------------')
#HCF(Highest Common Factor) or GCD(Greatest Common Divisor) using
#Euclidian algorithm: first divide the greater by smaller and take the remainder
#and then divide the smaller by this remainder; Repeat until the remainder is 0.
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)

#LCM = n1*n2 / GCD

def lcm_using_gcd(n1,n2):
    return n1*n2//gcd(n1,n2)

print('LCM of {} and {} is {}'.format(num1,num2,lcm_using_gcd(num1,num2)))
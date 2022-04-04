#Create a function that takes a number and returns its length 
#(use of the len() function is prohibited)

def length(string):
    count = 0
    for c in string:
        count += 1
    return count

num = input('Enter a number: ')
print('Length =',length(num))
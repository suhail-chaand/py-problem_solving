#Given a string, reverse all the words which have odd length. 
#The even length words are not changed.

def reverse_str(string):
    reversed_str = ''
    for i in range(len(string)-1,-1,-1):
        reversed_str += string[i]
    return reversed_str

def reverse_odd_words(string):
    out_string = ''
    words = string.split()
    for word in words:
        if len(word)%2==0:
            out_string += word + ' '
        elif len(word)%2!=0:
            out_string += reverse_str(word) + ' '
    return out_string

my_str = input('Enter a string: ')
print('Resulting string:',reverse_odd_words(my_str))
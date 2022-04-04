#Create a function that takes a list and string. 
#The function should remove the letters in the string from the list, 
#and return the string.

def remove_letters(l_list,string):
    out_string = ''
    for c in string:
        if c in l_list:
            pass
        else:
            out_string += c
    return out_string

in_str = input('Enter a string: ')
letters_list = input('Enter the letters to be removed: ').split()

print('Resulting string:',remove_letters(letters_list,in_str))
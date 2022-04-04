#Create a function that takes a string's characters as ASCII and 
#returns each character's hexadecimal value as a string.

def string_hex(string):
    hex_dict = {}
    for c in string:
        hex_dict.update({c:hex(ord(c))})
    return hex_dict

my_str = input('Input a string: ')

print(string_hex(my_str))
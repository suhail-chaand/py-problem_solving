#Create a function that takes an array of strings and 
#returns an array with only the strings that have numbers in them. 
#If there are no strings containing numbers, return an empty array.

def strings_containing_numbers(str_li):
    strings_of_numbers = []
    for string in str_li:
        for c in string:
            if c.isdigit():
                strings_of_numbers.append(string)
                break
    return strings_of_numbers

string_list = input('Enter a list of strings: ').split()
print('Strings containing numbers:',strings_containing_numbers(string_list))
#Create a function that takes a string and returns it back in camelCase.
#    camelCasing("Hello World") ➞ "helloWorld"

def camelCasing(string):
    words = string.split()
    camel_case_string = words[0].lower()
    for word in words[1:len(words)]:
        camel_case_string += word.capitalize()
    return camel_case_string

my_str = input('Enter the words: ')

print('Camel case form:',camelCasing(my_str))
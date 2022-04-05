#Given a string of letters in the English alphabet, 
#return the letter that's missing from the string. 
#The missing letter will make the string be in alphabetical order (from A to Z).
#If there are no missing letters in the string, return "No Missing Letter".
#missingLetter("abdefg") ➞ "c"

def missingLetters(string):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    missing_letters = [letter for letter in alphabets[alphabets.index(string[0]):alphabets.index(string[-1])] if letter not in string]
    if missing_letters != []:
        return missing_letters
    else:
        return 'No missing letters'

my_str = input('Enter a string: ')

print('Missing letters:',missingLetters(my_str))
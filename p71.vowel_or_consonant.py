#Check if a given char is a vowel or a consonant.

def vowel_or_consonant(c):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if c in vowels:
        return '{} is a Vowel'.format(c)
    else:
        return '{} is a Consonant'.format(c)

print(vowel_or_consonant(input('Enter an alphabet: ')))
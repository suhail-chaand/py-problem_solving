#Write a program that accepts a comma separated sequence of words as input and 
#prints the words in a comma-separated sequence after sorting them alphabetically.

words = input('Enter comma seperated words: ').split(', ')

sorted_words = sorted(words)

print('Sorted =>')
for i in range(len(sorted_words)):
    if i != len(sorted_words)-1:
        print(sorted_words[i]+', ',end='')
    else:
        print(sorted_words[i])
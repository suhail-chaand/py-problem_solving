#Write a function to replace word with another word and 
#another function to replace only an alphabet

sentence = input('Enter a sentence: ')

#Function
print('Function method--------------------')

word, replacement_word = input('Enter the word and its replacement: ').split()
def replace_word(sentence, word, replacement):
    words = [w for w in sentence.split()]
    for i in range(len(words)):
        if words[i]==word:
            words[i]=replacement
    out_sentence = ''
    for w in words:
        out_sentence += w+' '
    return out_sentence
print(replace_word(sentence,word,replacement_word))

alphabet, replacement_alphabet = input('Enter the alphabet and its replacement: ').split()
def replace_alphabet(sentence, alphabet, replacement):
    alphabets = [sentence[i] for i in range(len(sentence))]
    for i in range(len(sentence)):
        if alphabets[i]==alphabet:
            alphabets[i]=replacement
    out_sentence = ''
    for a in alphabets:
        out_sentence += a
    return out_sentence
print(replace_alphabet(sentence,alphabet,replacement_alphabet))

#Inbuilt function
print('Inbuilt function method--------------------')

print(sentence.replace(word,replacement_word))
print(sentence.replace(alphabet,replacement_alphabet))

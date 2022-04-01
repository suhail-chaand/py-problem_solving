#Write a program to check the validity of password input by users. 
#Following are the criteria for checking the password:
#    At least 1 letter between [a-z]
#    At least 1 number between [0-9]
#    At least 1 letter between [A-Z]
#    At least 1 character from [$#@]
#    Minimum length of transaction password: 7
#    No space accepted
#    Maximum length of transaction password: 12 
#Your program should accept a sequence of comma separated passwords and 
#will check them according to the above criteria. 
#Passwords that match the criteria are to be printed, each separated by a comma. 
#    Input: ABd1234@1 
#    Output: ABd1234@1

import re

print(re.findall(r'[a-zA-Z0-9$#@]{7,12}',input('Enter passwords: ')))
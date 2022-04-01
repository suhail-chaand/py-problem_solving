#Calculate no of days between two dates; take input from console

from datetime import datetime

try:
    d1 = datetime.strptime(input('Enter start date dd-mm-yyyy: '),'%d-%m-%Y')
    d2 = datetime.strptime(input('Enter end date dd-mm-yyyy: '),'%d-%m-%Y')
except:
    print('Invalid input!')

print('Number of days =',(d2-d1).days)
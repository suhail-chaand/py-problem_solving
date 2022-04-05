#Create a function that takes two dates and 
#returns the number of days between the first and second date.

from datetime import datetime

def days_bw_dates(d1,d2):
    return abs((d2-d1).days)

date1 = datetime.strptime(input('Enter date1 dd-mm-yyyy: '),'%d-%m-%Y')
date2 = datetime.strptime(input('Enter date2 dd-mm-yyyy: '),'%d-%m-%Y')

print('Number of days between {} and {} are: {} days'.format(datetime.strftime(date1,'%d-%m-%Y'),datetime.strftime(date2,'%d-%m-%Y'),days_bw_dates(date1,date2)))
#Given the month and year as numbers, 
#return whether that month contains a Friday 13th.

from datetime import datetime
import calendar

def isFriday_theThirteenth(d):
    if d.weekday() == 4:
        return 'The 13th of {} {} is a Friday'.format(calendar.month_name[d.month],d.year)
    else:
        return 'The 13th of {} {} is not a Friday'.format(calendar.month_name[d.month],d.year)

while True:
    try:
        in_date = datetime.strptime('13-'+input('Enter the month and the year mm-yyyy: '),'%d-%m-%Y')
        break
    except:
        print('Invalid input! Try again.')

print(isFriday_theThirteenth(in_date))
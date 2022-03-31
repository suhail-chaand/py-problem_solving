#Find the day of the week from given date

from datetime import datetime
import calendar

try:
    in_date = datetime.strptime(input('Enter a date dd-mm-yyyy: '),'%d-%m-%Y')
except:
    print('Invalid input!')
    quit()

#Raw
print('Raw method--------------------')
print(calendar.day_name[in_date.weekday()])

#Function
print('Function method--------------------')

def find_weekday(d):
    return calendar.day_name[d.weekday()]

print(find_weekday(in_date))

#OOP
print('OOP method--------------------')

class DateWeekday:
    def __init__(self,d) -> None:
        self.d=d
    def find_weekday(self):
        return calendar.day_name[self.d.weekday()]

dw = DateWeekday(in_date)

print(dw.find_weekday())
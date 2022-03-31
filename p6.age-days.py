#Convert age to days

age = float(input('Enter age: '))

#Raw
print('Raw method--------------------')
print('Number of days old = {}'.format(age*365))

#Function
print('Function method--------------------')

def years_days(yr):
    return 'Number of days old = {}'.format(yr*365)

print(years_days(age))

#OOP
print('OOP method--------------------')

class AgeToDays:
    def __init__(self,yr):
        self.yr=yr
    def years_days(self):
        return 'Number of days old = {}'.format(self.yr*365)

atd = AgeToDays(age)

print(atd.years_days())
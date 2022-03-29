#Convert Hours and Minutes into Seconds

hr, min = map(int,input('hh:mm = ').split(':'))

#Raw
print('Raw method')
print('Number of seconds = {} seconds'.format(hr*60*60+min*60))

#Function
print('Function method')

def secs(hours, minutes):
    return 'Number of seconds = {} seconds'.format(hours*60*60+minutes*60)

print(secs(hr,min))

#OOP
print('OOP method')

class HourMinutesToSeconds:
    def __init__(self,hours,minutes) -> None:
        self.hours=hours
        self.minutes=minutes
    def secs(self):
        return 'Number of seconds = {} seconds'.format(self.hours*60*60+self.minutes*60)

hmts = HourMinutesToSeconds(hr,min)

print(hmts.secs())
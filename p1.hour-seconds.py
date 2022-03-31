#Convert hours into seconds

hr = int(input('Enter the number of hours: '))

#Raw
print('Raw method---------------------')
print('{} hours in seconds: {} seconds'.format(hr,hr*60*60))

#Function
print('Function method--------------------')

def hr_to_sec(hour):
    return hour*60*60

print('{} hours in seconds: {} seconds'.format(hr,hr_to_sec(hr)))

#OOP
print('OOP method--------------------')

class HourToSeconds:
    def __init__(self,hour):
        self.hour=hour
    def hr_to_sec(self):
        return self.hour*60*60

hr_sec = HourToSeconds(hr)
print('{} hours in seconds: {} seconds'.format(hr,hr_sec.hr_to_sec()))
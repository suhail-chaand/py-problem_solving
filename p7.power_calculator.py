#Power Calculator

work = float(input('Work done in Joules = '))
time = int(input('Time in seconds = '))

#Raw
print('Raw method')
try:
    print('Power = {} Watt'.format(work//time))
except:
    print('Time taken cannot be ZERO')

#Function
print('Function method')

def power(w,t):
    try:
        return 'Power = {} Watt'.format(w//t)
    except:
        return 'Time taken cannot be ZERO'

print(power(work,time))

#OOP
print('OOP method')

class PowerCalulator:
    def __init__(self,w,t) -> None:
        self.w=w
        self.t=t
    def power(self):
        try:
            return 'Power = {} Watt'.format(work//time)
        except:
            return 'Time taken cannot be ZERO'

pc = PowerCalulator(work,time)

print(pc.power())
#The Farm Problem
#In this challenge, a farmer is asking you to tell him how many legs can be 
#counted among all his animals. The farmer breeds three species:
    #chickens = 2 legs
    #cows = 4 legs
    #pigs = 4 legs
#The farmer has counted his animals and he gives you a subtotal for each species. 
#You have to implement a function that returns the total number of legs of 
#all the animals.

chickens = int(input('Enter number of chickens: '))
cows = int(input('Enter number of cows: '))
pigs = int(input('Enter number of pigs: '))

#Function
print('Function method')
def count_legs(chicken,cow,pig):
    return 'Total leg count = {}'.format(chicken*2+cow*4+pig*4)

print(count_legs(chickens,cows,pigs))

#OOP
print('OOP method')

class LegCount:
    def __init__(self,chicken,cow,pig) -> None:
        self.chicken=chicken
        self.cow=cow
        self.pig=pig
    def count_legs(self):
        return 'Total leg count = {}'.format(self.chicken*2+self.cow*4+self.pig*4)

lc = LegCount(chickens,cows,pigs)

print(lc.count_legs())
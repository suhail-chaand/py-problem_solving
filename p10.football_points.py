#Football Points
#Create a function that takes the number of wins, draws and losses and 
#calculates the number of points a football team has obtained so far.
    #wins get 3 points
    #draws get 1 point
    #losses get 0 points

wins = int(input('Enter number of wins: '))
draws = int(input('Enter number of draws: '))
losses = int(input('Enter number of losses: '))

#Function
print('Function method')
def calc_points(win,draw):
    return 'Total points = {}'.format(win*3+draw*1)

print(calc_points(wins,draws))

#OOP
print('OOP method')
class FootballPoints:
    def __init__(self,win,draw):
        self.win=win
        self.draw=draw
    def calc_points(self):
        return 'Total points = {}'.format(self.win*3+self.draw*1)

fp = FootballPoints(wins,draws)

print(fp.calc_points())
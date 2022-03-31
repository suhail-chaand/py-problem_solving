#Write a program to print the list after removing the 0th,4th,5th numbers from list: 
#[12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1].

my_list = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]

#Raw
print('Raw method--------------------')
out_list = my_list.copy()
out_list.pop(0)
out_list.pop(3)
out_list.pop(3)
print(out_list)

#Function
print('Function method--------------------')

def rem_ele(li):
    oli = li.copy()
    oli.pop(0)
    oli.pop(3)
    oli.pop(3)
    return oli

print(rem_ele(my_list))

#OOP
print('OOP method')

class RemoveElements:
    def rem_ele(self,li):
        oli = li.copy()
        oli.pop(0)
        oli.pop(3)
        oli.pop(3)
        return oli

re = RemoveElements()

print(re.rem_ele(my_list))
#Write a program to sort the data by ascending and descending order. 
#Take a list of data: you can take input from console or define a list.

#Raw
print('Raw method-------------------')
my_list = input('Enter list of data: ').split()
print('Sorted ascending: ',sorted(my_list))
print('Sorted descending: ',sorted(my_list,reverse=True))

#Function
print('Function method--------------------')

def sort_asc(li):
    return sorted(li)
def sort_desc(li):
    return sorted(li,reverse=True)

print('Sorted ascending: ',sort_asc(my_list))
print('Sorted descending: ',sort_desc(my_list))

#OOP
print('OOP method-------------------')

class SortList:
    def __init__(self,li) -> None:
        self.li=li
    def sort_asc(self):
        return sorted(self.li)
    def sort_desc(self):
        return sorted(self.li,reverse=True)

sl = SortList(my_list)

print('Sorted ascending: ',sl.sort_asc())
print('Sorted descending: ',sl.sort_desc())
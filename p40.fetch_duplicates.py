#Write a program to print the duplicate numbers from the list: 
#[12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1,12,88,7,6,2].
#Print output in comma separated list.

my_list = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1,12,88,7,6,2]

#Raw
print('Raw method--------------------')
duplicates = set()
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] == my_list[j]:
            duplicates.add(my_list[i])

print('The duplicates are:',list(duplicates))

#Function
print('Function method--------------------')

def fetch_duplicates(my_list):
    duplicates = set()
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] == my_list[j]:
                duplicates.add(my_list[i])
    return list(duplicates)

print('The duplicates are:',fetch_duplicates(my_list))

#OOP
print('OOP method--------------------')

class DuplicatesInList:
    def fetch_duplicates(self,my_list):
        duplicates = set()
        for i in range(len(my_list)):
            for j in range(i+1,len(my_list)):
                if my_list[i] == my_list[j]:
                    duplicates.add(my_list[i])
        return list(duplicates)

dil = DuplicatesInList()

print('The duplicates are:',dil.fetch_duplicates(my_list))
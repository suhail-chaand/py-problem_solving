#Remove repetitive elements from the list; 
#list length should be 25 include number, char etc.

my_list = [12,True,65,45,'hi',True,'good morning',65,'morning',False,'good morning',
    11,12,13+14j,15,'bye',36,'hi',14+13j,14+13j,45,99,False,56+14j,12.99,12.98]

print('my_list of length {}:\n{}'.format(len(my_list),my_list))

print('my_list devoid of duplicates of length {}:\n{}'.format(len(set(my_list)),set(my_list)))
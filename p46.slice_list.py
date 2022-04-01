#Slice list into 3 chunks and reverse each chunk 
#list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

my_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

print([my_list[i*3:i*3+3][::-1] for i in range(len(my_list)) if i*3<len(my_list)])
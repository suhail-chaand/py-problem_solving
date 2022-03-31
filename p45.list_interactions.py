#Consider the list [54, 44, 27, 79, 91, 41, 36, 87, 10]
#Output:
#   my_list after removing an element at index 4: [54, 44, 27, 79, 41, 36, 87, 10]
#   my_list after adding an element at index 2: [54, 44, 11, 27, 79, 41, 36, 87, 10]
#   my_list after addding an element at the last [54, 44, 11, 27, 79, 41, 36, 87, 10, 99]

my_list = [54, 44, 27, 79, 91, 41, 36, 87, 10]

my_list.pop(4)
print('my_list after removing an element at index 4:',my_list)

my_list.insert(2,11)
print('my_list after adding an element at index 2:',my_list)

my_list.append(99)
print('my_list after addding an element at the last',my_list)
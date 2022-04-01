#Convert list into dictionary and add new item into dictionary

my_list = input('Enter a list: ').split()
my_dict = {}

for i in range(len(my_list)):
    my_dict.update({i:my_list[i]})

print('Dictionary:',my_dict)

k,v = input('Enter key and value: ').split()
my_dict.update({k:v})
print('Updated dictionary:',my_dict)
#Check if key exists in dictionary and delete that key value from dictionary

my_dict = {}

dict_len = int(input('Enter length of dictionary: '))
print('Enter dictionary elements:')
for _ in range(dict_len):
    k,v = input().split()
    my_dict.update({k:v})

key = input('Enter the key to be deleted: ')

if key in my_dict:
    del my_dict[key]
    print('Updated dictionary:',my_dict)
else:
    print('Key not found!')
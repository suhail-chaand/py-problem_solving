#Get only unique items from dictionary

my_dict = {}

dict_len = int(input('Enter length of dictionary: '))
print('Enter dictionary elements:')
for _ in range(dict_len):
    k,v = input().split()
    my_dict.update({k:v})

unique_values = set(my_dict.values())

unique_items = {}
for uv in unique_values:
    keys = []
    for k,v in my_dict.items():
        if v == uv:
            keys.append(k)
    unique_items.update({keys[0]:uv})

print('Items with unique values:',unique_items)

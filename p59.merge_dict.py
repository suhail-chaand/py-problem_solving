#Merge two dictionaries into one and rename dictionary key name

dict1 = {}
dict2 = {}

len1 = int(input('Enter length of dictionary 1: '))
print('Enter dictionary 1 elements:')
for i in range(len1):
    k,v = input().split()
    dict1.update({k:v})
len2 = int(input('Enter length of dictionary 2: '))
print('Enter dictionary 2 elements:')
for i in range(len2):
    k,v = input().split()
    dict2.update({k:v})

def merge_dict(d1,d2):
    return d1 | d2

merged_dict = merge_dict(dict1,dict2)
print('Dictionaries merged =>',merged_dict)

key, new_key = input('Enter key and its new name: ').split()
merged_dict[new_key] = merged_dict.pop(key)

print('Updated dictionary:',merged_dict)
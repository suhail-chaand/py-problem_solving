#Concant two lists index wise 
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]

l1 = ["M", "na", "i", "Ke"]
l2 = ["y", "me", "s", "lly"]
my_str = ''

for i in range(len(l1)):
    my_str += l1[i] + l2[i] + ' '

print(my_str)
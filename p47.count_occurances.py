#Count occurances of each element from a list
#list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

my_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
my_set = set(my_list)
count = {}

for e in my_set:
    count.update({e:my_list.count(e)})

print(count)
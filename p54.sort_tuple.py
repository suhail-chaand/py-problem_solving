#Sort tuple by 2nd item: (('a', 23),('b', 37),('c', 11), ('d',29))

my_tuple = (('a', 23),('b', 37),('c', 11), ('d',29))

print(sorted(my_tuple,key=lambda x:x[1]))
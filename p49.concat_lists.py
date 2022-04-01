#Concatenate two list as
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]  
#Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

l1 = ["Hello ", "take "]
l2 = ["Dear", "Sir"]
ol = []

for e1 in l1:
    for e2 in l2:
        ol.append(e1+e2)

print(ol)
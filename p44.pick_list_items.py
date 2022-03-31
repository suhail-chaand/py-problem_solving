#Create a list by picking an odd-index items from the first list and even index items from the second
#    l1 = [3, 6, 9, 12, 15, 18, 21]
#    l2 = [4, 8, 12, 16, 20, 24, 28] 
#    Output:
#	    Element at odd-index positions from list one: [6, 12, 18]
#	    Element at even-index positions from list two: [4, 12, 20, 28]
#	    Printing Final third list: [6, 12, 18, 4, 12, 20, 28]

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

#Raw
print('Raw method--------------------')

odd_list = [l1[i] for i in range(len(l1)) if i%2!=0]
even_list = [l2[i] for i in range(len(l2)) if i%2==0]
print(odd_list + even_list)
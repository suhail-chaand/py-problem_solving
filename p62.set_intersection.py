#Return a new set of identical items from two sets

set1 = set(input('Enter set 1 elements: ').split())
set2 = set(input('Enter set 2 elements: ').split())

print('Set of identical items from set 1 and set 2',set1.intersection(set2))
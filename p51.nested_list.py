#Extend nested list by adding sub list with specific index taken from console

my_list = ['nested','list']

tc = int(input('Enter number of test cases: '))

for _ in range(1,tc+1):
    print('Test case:',_)
    index = int(input('Enter index: '))
    sub_list = input('Enter sub-list: ').split()

    my_list.insert(index,sub_list)

    print(my_list)
    print('Index of sub-list =',my_list.index(sub_list))
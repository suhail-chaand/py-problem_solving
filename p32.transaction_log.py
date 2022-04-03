#Write a program that computes the net amount of a bank account based on a transaction log from console input. 
#    Log format is :  D 100 W 200; D means deposit while W means withdrawal. 
#    Input: D 300 D 300 W 200 D 100
#    Output: 500

transactions = input('Enter transactions: ').split()

deposits = [int(transactions[i+1]) for i in range(len(transactions)) if transactions[i]=='D' or transactions[i]=='d']
withdrawals = [int(transactions[i+1]) for i in range(len(transactions)) if transactions[i]=='W' or transactions[i]=='w']

print('Net amount =',sum(deposits) - sum(withdrawals))
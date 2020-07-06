#CTI-110
#P4HW1 Expenses
#Johnny Curry
#06 July 2020
#

#Declaring constants.
exp_count = 0
exp_amount = 0
total_exp = 0

#Get starting amount.
base_amount = int(input('Please enter starting amount: '))

#Enter expense amount.
exp_amount = float(input('Enter first expense: '))
exp_count = exp_count + 1
total_exp += exp_amount
cont = input('Do you ant to add another expense? (y/n):' )
while cont == 'y':
    exp_amount = float(input('Please enter next expense:' ))
    cont = input('Do you ant to add another expense? (y/n):' )
    exp_count = exp_count + 1
    total_exp += exp_amount
else:
#Show final information.
    print('Beginning amount before expenses: $',int(base_amount))
    print('Number of expenses: ',int(exp_count))
    print('Amount in account after expenses: $',int(base_amount - total_exp))

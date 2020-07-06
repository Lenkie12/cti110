#This program totals the number of bugs collected each day for 5 days.
#06 July 2020
#CTI-110 P4T2 - Bug Collector
#Johnny Curry
#

#Accumulator needed.
total_bugs = 0

#Get bugs per day.
for day in range(1, 6):
    #Ask to input collected bugs.
    print('Enter collected bugs on day', day)

    #Input number of bugs collected.
    bugs_col = int(input())
    total_bugs += bugs_col

#Show total bugs.
print('You got', total_bugs, 'total bugs.')

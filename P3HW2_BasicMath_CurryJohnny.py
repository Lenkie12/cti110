#CTI-110
#P3HW2 - BasicMath
#Johnny Curry
#26 June 2020
#

#Get the first number.
first_number = float(input('Enter the first number: '))

# Get the second number.
second_number = float(input('Enter the second number: '))

#Display math operations.
print('1) Add Numbers')
print('2) Multiply Numbers')
print('3) Subtract Numbers')
print('4) Exit')
math_op = input('Please enter math operation: ')


#Apply selected math operation.
if math_op == '1':
    total_add = first_number + second_number
    print('The sum is ', int(total_add))
else:
    if math_op == '2':
        total_multiply = first_number * second_number
        print('The product is ', int(total_multiply))
    else:
        if math_op == '3':
            total_subtract = first_number - second_number
            print('The difference is ', int(total_subtract))
        else:
            if math_op == '4':
                print('The program will now terminate.')
            else:
                print('You have made an invalid choice!!!')






#CTI-110
#P4HW2 - BasicMath
#Johnny Curry
#06 July 2020
#



#Get the two numbers.
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
print('\n')
#Constant range.
math_op = [1, 2, 3, 4]

#Display math operations.
while True:
    print('1) Add Numbers')
    print('2) Multiply Numbers')
    print('3) Subtract Numbers')
    print('4) Exit')
    print('\n')
    math_op = int(input('Please enter math operation: '))

#Apply selected math operation.
    if math_op == 1:
        total_add = first_number + second_number
        print('\n')
        print('The sum is ', int(total_add))
    else:
        if math_op == 2:
            total_multiply = first_number * second_number
            print('\n')
            print('The product is ', int(total_multiply))
            print('\n')
        else:
            if math_op == 3:
                total_subtract = first_number - second_number
                print('\n')
                print('The difference is ', int(total_subtract))
                print('\n')
            else:
                if math_op == 4:
                    print('\n')
                    print('The program will now terminate')
                    print('\n')
                    break
                else:
                    print('You have made an invalid choice!')
                    print('\n')

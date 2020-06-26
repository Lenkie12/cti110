#CTI-110
#P3LAB - Debugging
#Johnny Curry
#25 June 2020
#

#Input score.
score=(int(input('Please enter grade: ')))

#Dedicated grade value.
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 59

#Determine letter grade.
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

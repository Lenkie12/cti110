#To ask the length and width of two rectangles.
#To determine which rectangle has the greater area.
#24 July 2020
#CTI-110 P3T1 - Areas of Rectangles
#Johnny Curry
#

#Get the length and width of rectangle 1.
length_1 = int(input('Enter the length of rectangle 1: '))
width_1 = int(input('Enter the width of rectangle 1: '))

#Get the length and width of rectangle 2.
length_2 = int(input('Enter the length of rectangle 2: '))
width_2 = int(input('Enter the width of rectangle 2: '))

#Calculate area of rectangle 1.
rec_1 = length_1 * width_1

#Calculate area of rectangle 2.
rec_2 = length_2 * width_2

#Show results.
if rec_1 > rec_2:
    print('Rectangle 1 is greater.')
elif rec_2 > rec_1:
    print('Rectangle 2 is greater.')
else:
    print('Both rectangles have the same area.')   

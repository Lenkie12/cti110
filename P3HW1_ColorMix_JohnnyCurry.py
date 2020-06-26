#CTI-110
#P3HW1 - Color Mixer
#Johnny Curry
#25 June 2020
#

#Get the primary colors.
color_1=(input('Enter first primary color: '))
color_2=(input('Enter second primary color: '))

#Mix the colors.
if (color_1 == 'red' and color_2 == 'yellow') or (color_1 == 'yellow' and color_2 == 'red'):
    print('The color is ORANGE!')

elif (color_1 == 'red' and color_2 == 'blue') or (color_1 == 'blue' and color_2 == 'red'):
    print('The color is PURPLE!')

elif (color_1 == 'blue' and color_2 == 'yellow') or (color_1 == 'yellow' and color_2 == 'blue'):
    print('The color is GREEN!')

else:
    print('A primary color was not chosen!!!')

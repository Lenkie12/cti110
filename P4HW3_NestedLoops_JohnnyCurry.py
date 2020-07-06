#To draw pattern as per Chapter 3, Exercise 15, page 180
#06 July 2020
#CTI-110 - Nested Loops
#Johnny Curry
#

#Constant step.
steps = 6

#Create design with nested loop.
for s in range(steps):
    print('#', end='')
    for t in range(s):
        print(' ', end='',)
    print('#')

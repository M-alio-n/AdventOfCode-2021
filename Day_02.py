import numpy as np

### Part 1
file = open('Day_2_inpt.txt', 'r')
lines = file.readlines()

hor = 0
vert = 0
for line in lines:
    tup = (line.strip()).split(' ')
    if tup[0] == 'down':
        vert = vert + int(tup[1])
    elif tup[0] == 'up':
        vert = vert - int(tup[1])
    elif tup[0] == 'forward':
        hor = hor + int(tup[1])

print(hor*vert)

### Part 2
aim = 0
hor = 0
vert = 0
for line in lines:
    tup = (line.strip()).split(' ')
    if tup[0] == 'down':
        aim = aim + int(tup[1])
    elif tup[0] == 'up':
        aim = aim - int(tup[1])
    elif tup[0] == 'forward':
        hor = hor + int(tup[1])
        vert = vert + aim * int(tup[1])

print(hor*vert)
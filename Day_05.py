import numpy as np

#region: Additional functions
def extend_seafloor(current_map, new_max):
    np.pad(current_map, 0, 'constant')
    return
#endregion: Addtional functions
#region: Seafloor boards
file = open('Day_5_inpt.txt', 'r')
lines = file.readlines()
#endregion: Seafloor loaded
#region: Part 1
seafloor = np.empty([0,0])
for counter,line in enumerate(lines):
    points = line.strip().split(' -> ')
    x1,y1,x2,y2 = [int(x) for x in (points[0]+','+points[1]).split(',')]
    if max([x1,x2,y1,y2]) > np.shape(seafloor)[0]+1:          #If one of the new points is outside the square seafloor, we need to extend it
        seafloor = np.pad(seafloor,(0,max([x1,x2,y1,y2])-np.shape(seafloor)[0]+1), 'constant', constant_values=(0, 0))
    if y1 == y2:
        if x1 < x2:     # act on horizontal or vertical vent lines
            seafloor[y1,x1:x2+1] += 1
        else:
            seafloor[y1,x2:x1+1] += 1
    elif x1 == x2:      # act on horizontal or vertical vent lines
        if y1 < y2:
            seafloor[y1:y2+1,x1] += 1
        else:
            seafloor[y2:y1+1,x1] += 1

print('There are ' + str(len(np.where(seafloor > 1)[0])) + ' dangerous tiles in this part of the sea!')
#endregion: Part 1 complete!
#region: Part 2
seafloor = np.empty([0,0])
for counter,line in enumerate(lines):
    points = line.strip().split(' -> ')
    x1,y1,x2,y2 = [int(x) for x in (points[0]+','+points[1]).split(',')]
    if max([x1,x2,y1,y2]) >= np.shape(seafloor)[0]:          #If one of the new points is outside the square seafloor, we need to extend it
        seafloor = np.pad(seafloor,(0,max([x1,x2,y1,y2])-np.shape(seafloor)[0]+1), 'constant', constant_values=(0, 0))
    if y1 == y2:
        if x1 < x2:     # act on horizontal or vertical vent lines
            seafloor[y1,x1:x2+1] += 1
        else:
            seafloor[y1,x2:x1+1] += 1
    elif x1 == x2:      # act on horizontal or vertical vent lines
        if y1 < y2:
            seafloor[y1:y2+1,x1] += 1
        else:
            seafloor[y2:y1+1,x1] += 1
    else:
        if y1 < y2:
            for counter2, y_val in enumerate(range(y1,y2+1)):
                seafloor[y_val,x1+int(counter2*(x2-x1)/abs(x2-x1))] += 1
        else:
            for counter2, y_val in enumerate(range(y2,y1+1)):
                seafloor[y_val,x2+int(counter2*(x1-x2)/abs(x1-x2))] += 1

print('There are ' + str(len(np.where(seafloor > 1)[0])) + ' dangerous tiles in this part of the sea!')
#endregion: Part 2 complete!
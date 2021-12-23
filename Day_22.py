import numpy as np
import re

#region: Additional functions
def find_intersection(cuboid_1, cuboid_2):
    intersection_cuboid = []
    overlap = [0,0,0]
    for dim in range(3):
        if cuboid_1[dim*2] <= cuboid_2[dim*2] <= cuboid_1[dim*2+1]:
            overlap[dim] += 1
        if cuboid_1[dim*2] <= cuboid_2[dim*2+1] <= cuboid_1[dim*2+1]:
            overlap[dim] += 1
        if cuboid_2[dim*2] < cuboid_1[dim*2] < cuboid_2[dim*2+1] and cuboid_2[dim*2] < cuboid_1[dim*2+1] < cuboid_2[dim*2+1]:
            overlap[dim] = -2
    if all(overlap):    # every dimension has overlap
        for dim, overlap_val in enumerate(overlap):
            sorted_corners = sorted([cuboid_1[dim*2], cuboid_1[dim*2+1], cuboid_2[dim*2], cuboid_2[dim*2+1]])
            intersection_cuboid.extend(sorted_corners[1:3])
        intersection_cuboid = cuboid_volume(intersection_cuboid)
    return intersection_cuboid

def break_cuboid(cuboid_to_break, breaking_cuboid):
    broken_cuboids = []
    # There's got to be a more elegant way...
    # negative x
    broken_cuboids.append([cuboid_to_break[0], breaking_cuboid[0]-1, cuboid_to_break[2], cuboid_to_break[3], cuboid_to_break[4], cuboid_to_break[5]])
    # positive x
    broken_cuboids.append([breaking_cuboid[1]+1, cuboid_to_break[1], cuboid_to_break[2], cuboid_to_break[3], cuboid_to_break[4], cuboid_to_break[5]])
    # negative y
    broken_cuboids.append([breaking_cuboid[0], breaking_cuboid[1], cuboid_to_break[2], breaking_cuboid[2]-1, cuboid_to_break[4], cuboid_to_break[5]])
    # positive y
    broken_cuboids.append([breaking_cuboid[0], breaking_cuboid[1], breaking_cuboid[3]+1, cuboid_to_break[3], cuboid_to_break[4], cuboid_to_break[5]])
    # negtive z
    broken_cuboids.append([breaking_cuboid[0], breaking_cuboid[1], breaking_cuboid[2], breaking_cuboid[3], cuboid_to_break[4], breaking_cuboid[4]-1])
    # positive z
    broken_cuboids.append([breaking_cuboid[0], breaking_cuboid[1], breaking_cuboid[2], breaking_cuboid[3], breaking_cuboid[5]+1, cuboid_to_break[5]])
    for ind in range(5,-1,-1):
        if broken_cuboids[ind][1] < broken_cuboids[ind][0] or broken_cuboids[ind][3] < broken_cuboids[ind][2] or broken_cuboids[ind][5] < broken_cuboids[ind][4]:
            del broken_cuboids[ind]
        else:
            broken_cuboids[ind] = cuboid_volume(broken_cuboids[ind])
    return broken_cuboids

def fulfill_task(task_cuboid, list_of_cuboids, mode):
    breaking_cuboids = []   # these existing cuboids break into subcuboids
    new_cuboids = []    # these cuboids will be added 
    for cubeoid_idx, existing_cuboid in enumerate(list_of_cuboids):
        tmp = find_intersection(task_cuboid, existing_cuboid)
        if tmp:
            breaking_cuboids.append(cubeoid_idx)
            new_cuboids.extend(break_cuboid(existing_cuboid, tmp))  # break the existing cuboid into subcuboids
    if mode == 'on':
        new_cuboids.extend([cuboid_volume(task_cuboid)])
    for idx in reversed(breaking_cuboids):
        del list_of_cuboids[idx]    # remove the broken cubes
    list_of_cuboids.extend(new_cuboids) # add the new cuboids (subcuboids and only in mode 'on' also the task cuboid)
        
    return

def calc_on_vol(list_of_cuboids):
    sum = 0
    for cuboid in list_of_cuboids:
        sum += cuboid[6]
    return sum

def cuboid_volume(cuboid):
    cuboid.append((cuboid[1]-cuboid[0]+1)*(cuboid[3]-cuboid[2]+1)*(cuboid[5]-cuboid[4]+1))
    return cuboid

#endregion: Addtional functions
#region: Load boot sequence
cuboids = []
tasks = []
file = open('Day_22_inpt.txt', 'r')
for line in file.readlines():
    tasks.append(line.strip().split(' ')[0])
    cuboids.append([int(val) for val in re.findall('-?\d+', line)])
#endregion: Boot sequence loaded
#region: Part 1
reactor = np.zeros((101,101,101))
for step_no, cuboid in enumerate(cuboids):
    tmp_cuboid = [int(x)+50 for x in cuboid]    # shift the indices by 50 to positive values
    if not(any(y > 100 for y in tmp_cuboid) or any(y < 0 for y in tmp_cuboid)):
        if tasks[step_no] == 'on':
            reactor[tmp_cuboid[0]:tmp_cuboid[1]+1, tmp_cuboid[2]:tmp_cuboid[3]+1, tmp_cuboid[4]:tmp_cuboid[5]+1] = 1
        elif tasks[step_no] == 'off':
            reactor[tmp_cuboid[0]:tmp_cuboid[1]+1, tmp_cuboid[2]:tmp_cuboid[3]+1, tmp_cuboid[4]:tmp_cuboid[5]+1] = 0
print('Solution 1: ' + str(np.sum(reactor)))
#endregion: Part 1 complete!
#region: Part 2
on_cuboids = []
first_outside = 1
for step_no, cuboid in enumerate(cuboids):
    fulfill_task(cuboid, on_cuboids, tasks[step_no])
print('Solution 2: ' + str(calc_on_vol(on_cuboids)))
#endregion: Part 2 complete!
import numpy as np

#region: Additional functions
def get_adjacent(mat: np.array, row: int, col: int, mode: str = 'direct', dist: int = 1):
    adjacent_rows = [x for x in range(row-dist, row+dist+1)]
    adjacent_cols = [x for x in range(col-dist, col+dist+1)]
    values = []
    coordinates = []
    for rows in adjacent_rows:
        for cols in adjacent_cols:
            if rows >= 0 and cols >= 0 and rows < np.shape(mat)[0] and cols < np.shape(mat)[1]:   # handel edges and corners
                if not (rows == row and cols == col):
                    if mode == 'diag':   # All values, including diagonals
                        values.append(mat[rows, cols])
                        coordinates.append([rows, cols])
                    elif mode == 'direct': # No diagonal values
                        if rows == row or cols == col:
                            values.append(mat[rows, cols])
                            coordinates.append([rows, cols])
    return [values, coordinates]

def combine_clusters(mat):
    numbers = [set()] * (int(np.max(mat))+1)
    for rows in range(0, np.shape(mat)[0]):
        for cols in range(0, np.shape(mat)[1]):
            values, coords = get_adjacent(mat, rows, cols)
            numbers[mat[rows,cols]] = numbers[mat[rows,cols]].union(set([x for x in values if x < mat[rows,cols]]))
    
    for num, sets in enumerate(numbers):
        sets.discard(num)
        sets.discard(0)
    
    for number in range(np.max(mat), 0, -1):
        try:
            mat[mat == number] = max(numbers[number])
        except:
            continue

    return mat

def label_clusters(mat):
    labelled_mat = mat.copy()
    label = 1

    for rows in range(0, np.shape(mat)[0]):
        for cols in range(0, np.shape(mat)[1]):
            if mat[rows, cols] == 1:    # field is in a valley
                if rows > 0 and cols > 0:
                    if labelled_mat[rows-1, cols] >= 1:
                        labelled_mat[rows, cols] = labelled_mat[rows-1, cols]
                    elif labelled_mat[rows, cols-1] >= 1:
                        labelled_mat[rows, cols] = labelled_mat[rows, cols-1]
                    else:
                        label += 1
                        labelled_mat[rows, cols] = label
                elif rows > 0:            # check field above
                    if labelled_mat[rows-1, cols] >= 1:     # if it is labelled take its label
                        labelled_mat[rows, cols] = labelled_mat[rows-1, cols]
                    else:
                        label += 1
                        labelled_mat[rows, cols] = label
                elif cols > 0:            # check left field
                    if labelled_mat[rows, cols-1] >= 1:     # if it is labelled take its label
                        labelled_mat[rows, cols] = labelled_mat[rows, cols-1]
                    else:
                        label += 1
                        labelled_mat[rows, cols] = label

    labelled_mat = combine_clusters(labelled_mat)
    return labelled_mat
            
#endregion: Addtional functions
#region: Load seafloor
file = open('Day_9_inpt.txt', 'r')
seafloor = np.empty((0,0))
for count, line in enumerate(file.readlines()):
    if count == 0:
        seafloor = np.array([int(char) for char in line.strip()])
    else:
        seafloor = np.vstack([seafloor, np.array([int(char) for char in line.strip()])])
#endregion: Seafloor loaded
#region: Part 1
final_sum = 0
for rows in range(0, np.shape(seafloor)[0]):
    for cols in range(0, np.shape(seafloor)[1]):
        values, coords = get_adjacent(seafloor, rows,cols)
        if all(values > seafloor[rows,cols]):   # it is a local minimum
            final_sum += seafloor[rows,cols] + 1
print('The sum of all risk levels of the low points on the seafloor is: ' + str(final_sum))
#endregion: Part 1 complete!
#region: Part 2
coarse_seafloor = seafloor
coarse_seafloor[seafloor < 9 ] = 1
coarse_seafloor[seafloor == 9 ] = 0
labelled_floor = label_clusters(coarse_seafloor)
sums = []
for number in range(1, np.max(labelled_floor)+1):
    sums.append(np.sum(labelled_floor == number))

print('The product of the sizes of the largest vealleys is: ' + str(sorted(sums)[-3]*sorted(sums)[-2]*sorted(sums)[-1]))
#endregion: Part 2 complete!
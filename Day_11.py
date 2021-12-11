import numpy as np
from numpy.core.numeric import argwhere

#region: Additional functions
def set_adjacent(mat: np.array, row: int, col: int, mode: str = 'direct', value: float = 0, addition: str = 'set', dist: int = 1):
    adjacent_rows = [x for x in range(row-dist, row+dist+1)]
    adjacent_cols = [x for x in range(col-dist, col+dist+1)]
    for rows in adjacent_rows:
        for cols in adjacent_cols:
            if rows >= 0 and cols >= 0 and rows < np.shape(mat)[0] and cols < np.shape(mat)[1]:   # handel edges and corners
                if not (rows == row and cols == col):
                    if mode == 'diag':   # All values, including diagonals
                        if addition == 'add':   # Add the value
                            mat[rows, cols] += value
                        else:               # Directly set the value
                            mat[rows, cols] = value
                    elif mode == 'direct': # No diagonal values
                        if addition == 'add':   # Add the value
                            mat[rows, cols] += value
                        else:               # Directly set the value
                            mat[rows, cols] = value
    return

def simulate_step(octos):
    octos += 1
    new_flash = [tuple(x) for x in np.argwhere(octos == 10)]   # detect flashes
    octos[octos == 10] = 11     # after detecting a flash, it is increased, not to be detected again
    while len(new_flash) > 0:
        new_flashes = []
        for coords in new_flash:
            octos[coords[0], coords[1]] += 1
            set_adjacent(octos, coords[0], coords[1], 'diag', 1, 'add')
            new_flashes += [tuple(x) for x in np.argwhere(octos == 10)]  # detect flashes
            octos[octos == 10] = 11 # after detecting a flash, it is increased, not to be detected again
        new_flash = new_flashes
    flashes = np.sum(octos > 9)
    octos[octos > 9] = 0
    return flashes

#endregion: Addtional functions
#region: Load octopus energy levels
file = open('Day_11_inpt.txt', 'r')
octolight = np.empty((10,10))
for counter, line in enumerate(file.readlines()):
    octolight[counter] = np.array([int(x) for x in line.strip()])
octolight2 = np.copy(octolight)
#endregion: Octopus energy levels loaded
#region: Part 1
steps_to_sim = 100
flashes = 0
for ind in range(0,steps_to_sim):
    flashes += simulate_step(octolight)
print('In the first 100 steps there will be ' + str(flashes) + ' flashes')
#endregion: Part 1 complete!
#region: Part 2
steps_to_sim = 100
flashes = 1
counter = 0
while flashes < 100:
    flashes = simulate_step(octolight2)
    counter += 1
print('After ' + str(counter) + ' steps all octopuses will flash at once')
#endregion: Part 2 complete!
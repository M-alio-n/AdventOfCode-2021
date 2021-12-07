import numpy as np

#region: Additional functions
#endregion: Addtional functions
#region: Load crab positions
file = open('Day_7_inpt.txt', 'r')
for line in file.readlines():
    positions = np.array([int(x) for x in line.split(',')])

#endregion: Crab positions loaded
#region: Part 1
fuel_need = np.zeros(np.max(positions)+1)
for pos in range(0,np.max(positions)+1):
    fuel_need[pos] = np.sum(np.abs(pos-positions))
best_position = np.argwhere(fuel_need == np.min(fuel_need))[0,0]
fuel_needed = fuel_need[best_position]

print('The crabs should aling in position ' + str(best_position) + ' requiring a total of ' + str(fuel_needed) + ' units of fuel')
#endregion: Part 1 complete!
#region: Part 2
fuel_need = np.zeros(np.max(positions)+1)
for pos in range(0,np.max(positions)+1):
    fuel_need[pos] = np.sum((np.abs(pos-positions) * (np.abs(pos-positions)+1))/2)
best_position = np.argwhere(fuel_need == np.min(fuel_need))[0,0]
fuel_needed = fuel_need[best_position]

print('The crabs should aling in position ' + str(best_position) + ' requiring a total of ' + str(fuel_needed) + ' units of fuel')
#endregion: Part 2 complete!
import numpy as np
from numpy.core.defchararray import array

#region: Additional functions
def model_lanternfish(initial_timers, model_days):
    timers_7_8 = np.zeros(2)
    for days in range(0,model_days):
        initial_timers = np.roll(initial_timers, -1)    # Existing fish get their timer reduced by 1
        new_fish = initial_timers[-1]                   # Fish from a 0 timer create a new fish
        initial_timers[-1] += timers_7_8[0]             # Fish on a timer of 7 reduce their timer to 6 (changing from one array to the other)
        timers_7_8 = np.roll(timers_7_8, -1)            # Fish with a timer of 8 reduce their timer by 1
        timers_7_8[1] = new_fish                        # The new fish are assignet to the counter of 8 timers
    
    return np.sum(initial_timers) + np.sum(timers_7_8)
#endregion: Addtional functions
#region: Load fishtimers
file = open('Day_6_inpt.txt', 'r')
lines = file.readlines()
for counter,line in enumerate(lines):
    list = np.array([int(x) for x in line.strip().split(',')])
# Instead of working on the list of individual fishtimers, we count each occuring fish timer
timers = np.zeros(7)
for ind in range(0,7):
    timers[ind] = np.sum(list == ind)
#endregion: Fishtimers loaded
#region: Part 1
print('The sum of fish after ' + str(80) +  ' days is: ' + str(model_lanternfish(timers, 80)))
#endregion: Part 1 complete!
#region: Part 2
print('The sum of fish after ' + str(256) +  ' days is: ' + str(model_lanternfish(timers, 256)))
#endregion: Part 2 complete!
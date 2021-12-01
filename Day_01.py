import numpy as np

### Part 1
Data = np.loadtxt('Day_1_inpt.txt')
print(np.sum(np.diff(Data) > 0))

### Part 2
sums = [Data[x]+Data[x-1]+Data[x-2] for x in range(2, len(Data))]
print((np.sum(np.diff(sums) > 0)))
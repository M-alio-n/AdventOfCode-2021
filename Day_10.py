import numpy as np

#region: Additional functions
#endregion: Addtional functions
#region: Load Navigation systems
file = open('Day_10_inpt.txt', 'r')
subsys_lines = []
for line in file.readlines():
    subsys_lines.append(line.strip())
#endregion: Navigation systems loaded
#region: Part 1
values = {')': 3, ']': 57, '}': 1197, '>': 25137}
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_score, counter1 = [0, 0]
while counter1 < len(subsys_lines):
    flag, counter2 = [0, 0]
    while counter2 < len(subsys_lines[counter1]):
        if subsys_lines[counter1][counter2] in pairs:                       # opening new parenthesis
            counter2 += 1
        elif subsys_lines[counter1][counter2] == pairs[subsys_lines[counter1][counter2-1]]:    # closing last parenthesis
            subsys_lines[counter1] = subsys_lines[counter1][0:counter2-1] + subsys_lines[counter1][counter2+1::]    # Preparation for part 2
            counter2 -= 1
        else:                                   # erroneus line
            error_score += values[subsys_lines[counter1][counter2]]
            del subsys_lines[counter1]               # Preparation for part 2
            flag = 1
            break
    if flag == 0:
        counter1 += 1
        flag = 0
print('Error score for part 1: ' + str(error_score))
#endregion: Part 1 complete!
#region: Part 2
values = {'(': 1, '[': 2, '{': 3, '<': 4}
scores = []
for line in subsys_lines:
    score = 0
    for char in reversed(line):
        score = score * 5 + values[char]
    scores.append(score)
scores.sort()
print('Error score for part 2: ' + str(scores[int(np.floor(len(scores)/2))]))
#endregion: Part 2 complete!
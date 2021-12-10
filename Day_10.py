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
error_score = 0
for ind in range(len(subsys_lines)-1, -1, -1):
    line = subsys_lines[ind]
    open_chunks = ''
    for char in line:
        if char == '(':
            open_chunks += '0'
        elif char == ')' and open_chunks[-1] == '0':
            open_chunks = open_chunks[:-1]
        elif char == '[':
            open_chunks += '1'
        elif char == ']' and open_chunks[-1] == '1':
            open_chunks = open_chunks[:-1]
        elif char == '{':
            open_chunks += '2'
        elif char == '}' and open_chunks[-1] == '2':
            open_chunks = open_chunks[:-1]
        elif char == '<':
            open_chunks += '3'
        elif char == '>' and open_chunks[-1] == '3':
            open_chunks = open_chunks[:-1]
        else:
            error_score += values[char]
            del subsys_lines[ind]   # Preparation for part 2
            break

print('Error score for part 1: ' + str(error_score))
#endregion: Part 1 complete!
#region: Part 2
values = {'0': 1, '1': 2, '2': 3, '3': 4}
scores = []
for line in subsys_lines:
    open_chunks = ''
    for char in line:
        if char == '(':
            open_chunks += '0'
        elif char == ')' and open_chunks[-1] == '0':
            open_chunks = open_chunks[:-1]
        elif char == '[':
            open_chunks += '1'
        elif char == ']' and open_chunks[-1] == '1':
            open_chunks = open_chunks[:-1]
        elif char == '{':
            open_chunks += '2'
        elif char == '}' and open_chunks[-1] == '2':
            open_chunks = open_chunks[:-1]
        elif char == '<':
            open_chunks += '3'
        elif char == '>' and open_chunks[-1] == '3':
            open_chunks = open_chunks[:-1]
    score = 0
    for char in reversed(open_chunks):
        score = score * 5 + values[char]
    scores.append(score)
scores.sort()
print('Error score for part 2: ' + str(scores[int(np.floor(len(scores)/2))]))


#endregion: Part 2 complete!
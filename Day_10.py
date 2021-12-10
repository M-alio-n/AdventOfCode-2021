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
            if char == ')':
                error_score += 3
                del subsys_lines[ind]
                break
            elif char == ']':
                error_score += 57
                del subsys_lines[ind]
                break
            elif char == '}':
                error_score += 1197
                del subsys_lines[ind]
                break
            elif char == '>':
                error_score += 25137
                del subsys_lines[ind]
                break
print(str(error_score))
#endregion: Part 1 complete!
#region: Part 2
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
    for ind in range(len(open_chunks)-1, -1,-1):
        if open_chunks[ind] == '0':
            score = score * 5 + 1
        elif open_chunks[ind] == '1':
            score = score * 5 + 2
        elif open_chunks[ind] == '2':
            score = score * 5 + 3
        elif open_chunks[ind] == '3':
            score = score * 5 + 4
    scores.append(score)
scores.sort()
print(scores[int(np.floor(len(scores)/2))])


#endregion: Part 2 complete!
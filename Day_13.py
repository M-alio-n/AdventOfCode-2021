import numpy as np

#region: Additional functions    
def folding(given, dir, val):
    if dir == 1:
        outp = np.array(given[0:val, :])
        half_2 = np.array(given[val+1:, :])
        outp[val-np.shape(half_2)[0]:val, :] += np.flipud(half_2)
    else:
        outp = np.array(given[:, 0:val])
        half_2 = np.array(given[:, val+1:])
        outp[:, val-np.shape(half_2)[1]:val] += np.fliplr(half_2)
    
    outp[outp>0] = 1
    return outp
    
#endregion: Addtional functions
#region: Load paper
file = open('Day_13_inpt.txt', 'r')
coords = []
fold_dirs = []
fold_vals = []
for count, line in enumerate(file.readlines()):
    if line[0:3] == 'fol':
        line.strip().split('=')
        fold_vals.append(int(line.strip().split('=')[1]))
        if line.strip().split('=')[0][-1] == 'x':
            fold_dirs.append(0)
        else:
            fold_dirs.append(1)
    elif line == '\n':
        continue
    else:
        coords.append([int(x) for x in line.strip().split(',')])

paper = np.zeros((max([x[1] for x in coords])+1, max([y[0] for y in coords])+1))
for coord in coords:
    paper[coord[1],coord[0]] = 1
#endregion: Paper loaded
#region: Part 1
folding(paper, fold_dirs[0], fold_vals[0])
print('After the first fold, there are ' + str(np.sum(folding(paper, fold_dirs[0], fold_vals[0]))) + ' dots.')
#endregion: Part 1 complete!
#region: Part 2
for fold_idx, dir in enumerate(fold_dirs):
    paper = folding(paper, dir, fold_vals[fold_idx])
np.savetxt('result.txt', paper, fmt='%u')
print('Take a look in result.txt to see the activation code for the thermal cam.')
#endregion: Part 2 complete!
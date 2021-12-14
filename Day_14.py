#region: Additional functions    
#endregion: Addtional functions
#region: Load paper
file = open('Day_14_inpt.txt', 'r')
insertion = {}
pairings = {}
for count, line in enumerate(file.readlines()):
    if count == 0:
        template = line.strip()
        template2 = line.strip()
    elif line == '\n':
        continue
    else:
        pairings[line.strip().split(' -> ')[0]] = [line.strip().split(' -> ')[0][0]+line.strip().split(' -> ')[1], line.strip().split(' -> ')[1]+line.strip().split(' -> ')[0][1]]
#endregion: Paper loaded
#region: Part 1
cycles = 10 
pos = []
for i in range(0, cycles):
    pos = []
    for ind, lett in enumerate(template[:-1]):
        if template[ind]+template[ind+1] in pairings:
            pos.append(ind)
    for count, pos_idx in enumerate(pos):
        template = template[0:pos_idx+count+1] + pairings[template[pos_idx+count:pos_idx+count+2]][0][1] + template[pos_idx+count+1::]

counts = []
for char in set(template):
    counts.append(template.count(char))
print('Solution for part 1: ' + str(max(counts) - min(counts)))
#endregion: Part 1 complete!
#region: Part 2
counts = {}
for ind, lett in enumerate(template2[:-1]):
    if lett+template2[ind+1] in counts:
        counts[lett+template2[ind+1]] += 1
    else:
        counts[lett+template2[ind+1]] = 1

cycles = 40
new_counts = dict()
for i in range(0, cycles):
    new_counts = {}
    for pairs in counts:
        for n_pair in pairings[pairs]:
            if n_pair in new_counts:
                new_counts[n_pair] += counts[pairs]
            else:
                new_counts[n_pair] = counts[pairs]
    counts = new_counts.copy()

new_counts = {}
for pairs in counts:
    for char in pairs:
        if char in new_counts:
            new_counts[char] += counts[pairs]
        else:
            new_counts[char] = counts[pairs]
maxim = 0
minim = float('inf')
for char in new_counts:
    new_counts[char] = round(new_counts[char]/2)
    if new_counts[char] > maxim:
        maxim = new_counts[char]
    if new_counts[char] < minim:
        minim = new_counts[char]
print('Solution for part 2: ' + str(maxim-minim))
#endregion: Part 2 complete!
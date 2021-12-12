#region: Additional functions
def rec_ways(system, parent_way, key, ways):
    way = parent_way.copy()
    if key == 'end':    # the way ends succesfully
        way.append(key)
        return way
    elif key.islower() and key in way:  # the way ends because it revisits a small cave
        return []
    else:   # the way continues
        way.append(key)
        for cave in system[key]:
            tmp = rec_ways(system, way, cave, ways)
            if len(tmp) == 0:
                continue
            else:
                ways.append(tmp)
    return []

def rec_ways2(system, parent_way, key, ways):
    way = parent_way.copy()
    if key == 'end':    # the way ends succesfully
        way.append(key)
        return way
    elif key.islower() and key in way and key == 'start':  # the way ends because it revisits the start cave
        return []
    elif key.islower() and illegal_revisit(way,key):  # the way ends because it revisits a small cave
        return []
    else:   # the way continues
        way.append(key)
        for cave in system[key]:
            tmp = rec_ways2(system, way, cave, ways)
            if len(tmp) == 0:
                continue
            else:
                ways.append(tmp)
    return []

def illegal_revisit(way, key):
    if way.count(key) == 2:     # this cave has already been visited twice,it is not allowed to be revisited!
        return True
    elif way.count(key) == 1:   # this cave was only visited once lets make sure no other small cave was visited twice before
        for cave in way:
            if cave.islower() and way.count(cave) == 2:
                return True
        return False
    return False


#endregion: Addtional functions
#region: Load cave system
file = open('Day_12_inpt.txt', 'r')
cave_system = {}
for line in file:
    caves = line.strip().split('-')
    if caves[0] in cave_system:
        cave_system[caves[0]].add(caves[1])
    else:
        cave_system[caves[0]] = set([caves[1]])
    if caves[1] in cave_system:
        cave_system[caves[1]].add(caves[0])
    else:
        cave_system[caves[1]] = set([caves[0]])
#endregion: cave_system loaded
#region: Part 1
list_o_ways = []
rec_ways(cave_system,[],'start',list_o_ways)
print('There are ' + str(len(list_o_ways)) + ' ways out of the cave system without visiting small caves more than once.')
#endregion: Part 1 complete!
#region: Part 2
list_o_ways = []
rec_ways2(cave_system,[],'start',list_o_ways)
print('There are ' + str(len(list_o_ways)) + ' ways out of the cave system with a maximum of one small cave being visited twice.')
#endregion: Part 2 complete!
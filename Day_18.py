import numpy as np

def reduce_line(line):
    old_line = line
    outer_flag = 1
    while outer_flag:
        open_pairs = 0
        outer_flag = 0
        for idx, char in enumerate(old_line):
            if char == '[':
                open_pairs += 1
            elif char == ']':
                open_pairs -= 1
            
            if open_pairs == 5: # explode the pair
                partner_flag = 0
                left_line = old_line[0:idx]
                # right_line = old_line[idx+5::]
                # n1 = int(old_line[idx+1])
                # n2 = int(old_line[idx+3])

                first_flag = 0
                if old_line[idx+1:idx+3].isnumeric():   # first number has two digits
                    n1 = int(old_line[idx+1:idx+3])
                    first_flag += 1
                else:
                    n1 = int(old_line[idx+1])
                second_flag = 0
                if old_line[idx+first_flag+3:idx+first_flag+5].isnumeric(): #second number has two digits
                    n2 = int(old_line[idx+first_flag+3:idx+first_flag+5])
                    second_flag += 1
                else:
                    n2 = int(old_line[idx+first_flag+3])
                right_line = old_line[idx+5+first_flag+second_flag::]

                flag = 0
                for idx_l in range(len(left_line)-1, -1, -1):
                    if left_line[idx_l].isnumeric():
                        if left_line[idx_l-1:idx_l+1].isnumeric():
                            left_line = left_line[0:idx_l-1] + str(int(left_line[idx_l-1:idx_l+1]) + n1) + left_line[idx_l+1::]
                        else:
                            left_line = left_line[0:idx_l] + str(int(left_line[idx_l]) + n1) + left_line[idx_l+1::]
                        flag = 1
                        partner_flag += 1
                        break
                if flag == 0:
                    left_line = left_line + '0'
                
                flag = 0
                for idx_r in range(0, len(right_line)):
                    if right_line[idx_r].isnumeric():
                        if right_line[idx_r:idx_r+2].isnumeric():
                            right_line = right_line[0:idx_r] + str(int(right_line[idx_r:idx_r+2]) + n2) + right_line[idx_r+2::]
                        else:
                            right_line = right_line[0:idx_r] + str(int(right_line[idx_r]) + n2) + right_line[idx_r+1::]
                        flag = 1
                        partner_flag += 1
                        break
                if flag == 0:
                    right_line = '0' + right_line
                if partner_flag == 2:
                    old_line = left_line + '0' + right_line
                else:
                    old_line = left_line + right_line
                outer_flag = 1
                break
        if outer_flag == 0:
            for idx, char in enumerate(old_line):
                if old_line[idx:idx+2].isnumeric():   # split this pair
                    left_line = old_line[0:idx]
                    right_line = old_line[idx+2::]
                    old_line = left_line + '[' + str(int(np.floor(int(old_line[idx:idx+2])/2))) + ',' + str(int(np.ceil(int(old_line[idx:idx+2])/2))) + ']' + right_line
                    outer_flag = 1
                    break
    return old_line

def add_lines(line1, line2):
    return reduce_line('[' + line1 + ',' + line2 + ']')

def get_magnitude(line):
    open_pairs = 0
    for idx, char in enumerate(line):
        if char == '[':
            open_pairs += 1
        elif char == ']':
            open_pairs -= 1
        elif open_pairs == 1 and char == ',':
            first_term = line[1:idx]
            second_term = line[idx+1:-1]
            break
    if first_term.isnumeric():
        first_magnitude = 3*int(first_term)
    else:
        first_magnitude = 3*get_magnitude(first_term)
    if second_term.isnumeric():
        second_magnitude = 2*int(second_term)
    else:
        second_magnitude = 2*get_magnitude(second_term)
    return first_magnitude+second_magnitude

#region: Additional functions
#endregion: Addtional functions
#region: Load snailfish homework
file = open('Day_18_inpt.txt', 'r')
homework = []
for counter, line in enumerate(file.readlines()):
    homework.append(line.strip())
#endregion: Homework loaded
#region: Part 1
first_line = homework[0]
for ind in range(1, len(homework)):
    first_line = add_lines(first_line, homework[ind])
print(get_magnitude(first_line))
#endregion: Part 1 complete!
#region: Part 2
max_mag = 0
for ind_1 in range(0,len(homework)):
    for ind_2 in range(0,len(homework)):
        if ind_1 != ind_2:
            if get_magnitude(add_lines(homework[ind_1], homework[ind_2])) > max_mag:
                max_mag = get_magnitude(add_lines(homework[ind_1], homework[ind_2]))
        else:
            continue
print(max_mag)
#endregion: Part 2 complete!
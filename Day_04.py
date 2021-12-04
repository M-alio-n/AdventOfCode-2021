import numpy as np

#region: Additional functions
def check_for_win():
    winner = []
    for board_no in range(0,len(boards)):
        for row in range(0,5):
            if np.sum(drawn[board_no][row,:]) == 5:
                winner.append(board_no)
        for column in range(0,5):
            if np.sum(drawn[board_no][:,column]) == 5:
                winner.append(board_no)
    return list(dict.fromkeys(winner))

def bool_equal(array, value):
    tmp_array = np.zeros(np.shape(array), dtype=bool)
    tmp = np.where(array == value)
    for ind in range(0,len(tmp[0])):
        tmp_array[tmp[0][ind], tmp[1][ind]] = True
    return tmp_array


def winvalue(winner):
    return sum(boards[winner][bool_equal(np.array(drawn[winner], dtype=bool), False)])*number
    
#endregion: Addtional functions
#region: Load the bingo boards
file = open('Day_4_inpt.txt', 'r')
lines = file.readlines()

tmp_board = np.empty([5,5])
boards = []
board_no = 0
board_line = 0
for counter,line in enumerate(lines):
    if counter == 0:
        draw_numbers = [int(x) for x in line.split(',')]
    elif line == '\n':
        if counter != 1:
            boards.append(tmp_board.copy())
            board_no += 1
            board_line = 0
    else:
        numbers = [int(x) for x in line.split()]
        tmp_board[board_line, :] = numbers
        board_line += 1
boards.append(tmp_board.copy())
#endregion: Bingo boards loaded
#region: Part 1
drawn = []
for board_no in range(0,len(boards)):
    drawn.append(np.zeros(np.shape(boards[board_no])))

for number in draw_numbers:
    for board_no in range(0,len(boards)):
        drawn[board_no][bool_equal(boards[board_no], number)] = 1
    if len(check_for_win()) > 0:
        break

print('Winning value for part 1 is: ' + str(winvalue(check_for_win()[0])))
#endregion: Part 1 complete!
#region: Part 2
drawn = []
for board_no in range(0,len(boards)):
    drawn.append(np.zeros(np.shape(boards[board_no])))

prev_win = []
for number in draw_numbers:
    for board_no in range(0,len(boards)):
        drawn[board_no][bool_equal(boards[board_no], number)] = 1
    if len(check_for_win()) == len(boards):
        break
    prev_win = check_for_win()

print('Winning value for part 2 is: ' + str(winvalue(list(set(check_for_win()) - set(prev_win))[0])))

#endregion: Part 2 complete!
import numpy as np

#region: Additional functions
def check_for_win():
    winner = []
    for board_no in range(0,len(boards)):
        for row in range(0,5):
            if np.sum(drawn[board_no][row,:]) == 5: # If all five entries in one row of the drawn array are 1, the sum is 5 and that's a BINGO!
                winner.append(board_no)
        for column in range(0,5):
            if np.sum(drawn[board_no][:,column]) == 5: # If all five entries in one column of the drawn array are 1, the sum is 5 and that's a BINGO!
                winner.append(board_no)
    return list(dict.fromkeys(winner))

def winvalue(winner):
    return sum(boards[winner][np.array(drawn[winner], dtype=bool)== False])*number
    
#endregion: Addtional functions
#region: Load the bingo boards
file = open('Day_4_inpt.txt', 'r')
lines = file.readlines()

tmp_board = np.empty([5,5])
boards = [] # This list will contain the final bingo boards
board_no = 0
board_line = 0
for counter,line in enumerate(lines):
    if counter == 0:    # The first line contains the numbers in the order in which they are drawn
        draw_numbers = [int(x) for x in line.split(',')]
    elif line == '\n':  # A linebreak separates the boards
        if counter != 1:    # But the first only separates the numbers from the first board
            boards.append(tmp_board.copy()) # Append the current board to the collection of boards (!!!the copy function is needed, as arrays will otherwise be passed by reference!!!)
            board_no += 1
            board_line = 0
    else:   # Each other line contains one line of one board
        numbers = [int(x) for x in line.split()]
        tmp_board[board_line, :] = numbers
        board_line += 1
boards.append(tmp_board.copy()) # Append the final board to the collection of boards
#endregion: Bingo boards loaded
#region: Part 1
drawn = []
for board_no in range(0,len(boards)):
    drawn.append(np.zeros(np.shape(boards[board_no])))  # In this array the positions of drawn numbers will be tagged

for number in draw_numbers:
    for board_no in range(0,len(boards)):
        drawn[board_no][boards[board_no]== number] = 1   # In the drawn array all positions that contain the number in the boards array are tagged
    if len(check_for_win()) > 0:    # Once the first winning array was detected, the number-drawing loop breaks
        break

print('Winning value for part 1 is: ' + str(winvalue(check_for_win()[0])))
#endregion: Part 1 complete!
#region: Part 2
drawn = []
for board_no in range(0,len(boards)):
    drawn.append(np.zeros(np.shape(boards[board_no])))  # In this array the positions of drawn numbers will be tagged

prev_win = []   # Note here which boards have already won
for number in draw_numbers:
    for board_no in range(0,len(boards)):
        drawn[board_no][boards[board_no]== number] = 1   # In the drawn array all positions that contain the number in the boards array are tagged
    if len(check_for_win()) == len(boards): # Once the last winning array was detected, the number-drawing loop breaks
        break
    prev_win = check_for_win()  # Note which boards have already won

print('Winning value for part 2 is: ' + str(winvalue(list(set(check_for_win()) - set(prev_win))[0])))

#endregion: Part 2 complete!
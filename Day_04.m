function [] = Day_04()
%% Load the boards and the numbers
fid = fopen('Day_4_inpt.txt');
tline = fgetl(fid);
line_count = 1;

board_no = 0;
board_line = 0;
tmp_board = zeros(5,5);

while ischar(tline)
    if line_count == 1
        draw_numbers = str2double(split(tline,','));
    elseif isempty(tline)
        if line_count ~= 2
            board(board_no).board = tmp_board;
        end
        board_no = board_no + 1;
        board_line = 1;
    else
        numbers = str2double(split(tline));
        tmp_board(:,board_line) = numbers(~isnan(numbers));
        board_line = board_line +1;
    end
    
    
    tline = fgetl(fid);
    line_count = line_count + 1;
end
board(board_no).board = tmp_board;
fclose(fid);
% Boards loaded

%% Part 1
for board_no = 1:numel(board)
    drawn(board_no).board = zeros(5,5);
end

for number = draw_numbers'
    for board_no = 1:numel(board)
        drawn(board_no).board(board(board_no).board == number) = 1;
    end
    if ~isempty(check_for_win())
        break
    end
end

disp(['Winning value for part 1 is: ' num2str(winvalue(check_for_win()))])

clearvars drawn

%% Part 2
for board_no = 1:numel(board)
    drawn(board_no).board = zeros(5,5);
end

prev_win = [];
for number = draw_numbers'
    for board_no = 1:numel(board)
        drawn(board_no).board(board(board_no).board == number) = 1;
    end
    if numel(check_for_win()) == numel(board)
        break
    end
    prev_win = check_for_win();
end

disp(['Winning value for part 2 is: ' num2str(winvalue(setdiff([1:numel(board)], prev_win)))])

%% Additional functions
    function [winner] = check_for_win()
        winner = [];
        for board_no = 1:numel(board)
            for row = 1:5
                if sum(drawn(board_no).board(row,:)) == 5
                    winner = [winner, board_no];
                end
            end
            for column = 1:5
                if sum(drawn(board_no).board(:,column)) == 5
                    winner = [winner, board_no];
                end
            end
        end
        winner = unique(winner);
    end


    function [value] = winvalue(winner)
        value = sum(sum(board(winner).board(~drawn(winner).board)))*number;
    end

end
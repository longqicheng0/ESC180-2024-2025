import copy

def is_empty(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != " ":
                return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    prev_status = ""
    after_status = ""

    if (min(y_end, x_end) < 0) or (max(y_end, x_end) >= len(board)):
        return "CLOSED"
    
    #prev
    if (min(y_end - length * d_y, x_end - length * d_x) < 0) or (max(y_end - length * d_y, x_end - length * d_x) >= len(board)):
        prev_status = "CLOSED"
    elif board[y_end - length * d_y][x_end - length * d_x] == " ":
        prev_status = "OPEN"
    else:
        prev_status = "CLOSED"
    
    #after
    if (min(y_end + d_y, x_end + d_x) < 0) or (max(y_end + d_y, x_end + d_x) >= len(board)):
        after_status = "CLOSED"
    elif board[y_end + d_y][x_end + d_x] == " ":
        after_status = "OPEN" 
    else:
        after_status = "CLOSED"
        
    if prev_status == after_status:
        if prev_status == "CLOSED":
            return "CLOSED"
        else:
            return "OPEN"
    else: 
        return "SEMIOPEN" 

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_seq_count = 0
    current_length = 0
    cur_status = ""

    for i in range(len(board) + 1):
        if y_start + d_y > len(board) or x_start + d_x > len(board) or y_start + d_y < 0 or x_start + d_x < 0:
            return open_seq_count, semi_seq_count

        elif board[y_start][x_start] == col:
            current_length = get_length(board, col, y_start, x_start, d_y, d_x)

            if current_length == length:
                cur_status = is_bounded(board, (y_start + d_y * (length - 1)), (x_start + d_x * (length - 1)), length, d_y, d_x)
                
                y_start += (length - 1) * d_y
                x_start += (length - 1) * d_x

                if cur_status == "OPEN":
                    open_seq_count = open_seq_count + 1
                if cur_status == "SEMIOPEN":
                    semi_seq_count = semi_seq_count + 1

            else:
                y_start += (current_length - 1) * d_y
                x_start += (current_length - 1) * d_x

        y_start += d_y
        x_start += d_x

def get_length(board, col, y_start, x_start, d_y, d_x):
    length = 1 

    for i in range(len(board) + 1):
        if max(y_start + d_y, x_start + d_x) >= len(board) or min(y_start + d_y, x_start + d_x) < 0 or board[y_start + d_y][x_start + d_x] != col:
            return length

        y_start += d_y
        x_start += d_x
        length += 1

def detect_rows(board, col, length):
    open_seq_count, semi_seq_count = 0, 0
    
    #(0,1)
    for cl in range(len(board)):
        count = detect_row(board, col, cl, 0, length, 0, 1)
        open_seq_count += count[0]
        semi_seq_count += count[1]
      
    #(1,0)  
    for row in range(len(board)):
        count = detect_row(board, col, 0, row, length, 1, 0)
        open_seq_count += count[0]
        semi_seq_count += count[1]
    
    for cl in range(len(board)):
        count = detect_row(board, col, cl, 0, length, 1, 1)
        open_seq_count += count[0]
        semi_seq_count += count[1]

        count = detect_row(board, col, cl, 7, length, 1, -1)
        open_seq_count += count[0]
        semi_seq_count += count[1]

    for cl in range(1, len(board)-1):
        count = detect_row(board, col, 0, cl, length, 1, 1)
        open_seq_count += count[0]
        semi_seq_count += count[1]

        count = detect_row(board, col, 0, cl, length, 1, -1)
        open_seq_count += count[0]
        semi_seq_count += count[1]
        
    return open_seq_count, semi_seq_count

def search_max(board):
    copy_board = copy.deepcopy(board)
    cur_score = score(board)
    test_score = 0
    move_x = 0
    move_y = 0
    
    for r in range(len(board)):
        for c in range(len(board)):
            if copy_board[r][c] == " ":
                copy_board[r][c] = "b"
                test_score = score(copy_board)
                copy_board[r][c] = " "
                if test_score >= cur_score:
                    cur_score = test_score
                    move_y = r
                    move_x = c
                    
    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def check_full(board):      
    for i in range(len(board)):
        for n in range(len(board)):
            if board[i][n] == " ":
                return False
    return True    

def test_row_win(board, col, y_start, x_start, length, d_y, d_x):
    cur_length = 0,0
    status = False
    
    for i in range(len(board) + 1):
        if y_start + d_y > len(board) or x_start + d_x > len(board) or y_start + d_y < 0 or x_start + d_x < 0:
            return status

        elif board[y_start][x_start] == col:
            cur_length = get_length(board, col, y_start, x_start, d_y, d_x)

            if cur_length == length:
                status = True
            else:
                y_start += (cur_length - 1) * d_y
                x_start += (cur_length - 1) * d_x

        y_start += d_y
        x_start += d_x

def test_rows_win(board, col, length):

    for cl in range(len(board)):
        if test_row_win(board, col, cl, 0, length, 0, 1):
            return True
    
    for row in range(len(board)):
        if test_row_win(board, col, 0, row, length, 1, 0):
            return True
    
    for cl in range(len(board)):
        # top left to bottom right
        if test_row_win(board, col, cl, 0, length, 1, 1):
            return True

        if test_row_win(board, col, cl, 7, length, 1, -1):
            return True

    for cl in range(1, len(board)):
        if test_row_win(board, col, 0, cl, length, 1, 1):
            return True

        if test_row_win(board, col, 0, cl, length, 1, -1):
            return True

    return False


def is_win(board):
    # detects if there are any winning rows of each colour

    black_count = test_rows_win(board, "b", 5)
    white_count = test_rows_win(board, "w", 5)

    if black_count > 0:
        return "Black won"
    elif white_count > 0:
        return "White won"
    elif check_full(board):
        return "Draw"
    else:
        return "Continue playing"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
         
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
                    
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


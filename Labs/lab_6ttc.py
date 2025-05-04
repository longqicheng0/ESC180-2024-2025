import random

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")  
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def get_cord(square_num):
    if square_num <= 9 and 1 <= square_num:
        row = (square_num - 1) // 3
        col = (square_num - 1) % 3
        
        return [row,col]
    return
   
def put_in_board(board, mark, square_num):
    mark = mark.upper()
    row = (square_num - 1) // 3
    col = (square_num - 1) % 3
    if mark == "X" or mark == "O":
        board[row][col] = mark
        return board
    return
     
def game(board):
    game_end = False
    cnt = 0
    
    while game_end == False:
        if cnt % 2 == 0:
            print("its player 1's turn,please input which square you would like to put X in")
            user1 = int(input())
            row = (user1 - 1) // 3
            col = (user1 - 1) % 3
            filled = board[row][col] == "X" or board[row][col] == "O"
            while user1 < 1 or user1 > 9 or filled:
                print("!!please input a proper square index!!")
                user1 = int(input())
                row = (user1 - 1) // 3
                col = (user1 - 1) % 3
                filled = board[row][col] == "X" or board[row][col] == "O"
            
            put_in_board(board, "X", user1)
            print_board_and_legend(board)
            cnt += 1
                
        else:
            print("its player 2's turn,please input which square you would like to put O in")
            user2 = int(input())
            row = (user2 - 1) // 3
            col = (user2 - 1) % 3
            filled = board[row][col] == "X" or board[row][col] == "O"
            while user1 < 1 or user1 > 9 or filled:
                print("!!please input a proper square index!!")
                user2 = int(input())
                row = (user2 - 1) // 3
                col = (user2 - 1) % 3
                filled = board[row][col] == "X" or board[row][col] == "O"
            
            put_in_board(board, "O", user2)
            print_board_and_legend(board)
            cnt += 1
        
        #seperate from above since the board migt start unempty
        temp = 0
        for i in range (len(board)):
            for j in range (len(board[0])):
                if board[i][j] == "X" or board[i][j] == "O":
                    temp += 1
        
        if temp == 9:
            game_end = True

def get_free_squares(board):
    res = []
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] == " ":
                res.append([i,j])
    
    return res

def user_move(board):
    print("its your turn,please input which square you would like to put X in")
    user = int(input())
    row = (user - 1) // 3
    col = (user - 1) % 3
    filled = board[row][col] == "X" or board[row][col] == "O"
    while user < 1 or user > 9 or filled:
        print("!!please input a proper square index!!")
        user = int(input())
        row = (user - 1) // 3
        col = (user - 1) % 3
        filled = board[row][col] == "X" or board[row][col] == "O"
    put_in_board(board, "X", user)
              
def make_random_move(board, mark):
    free = get_free_squares(board)
    print (free)
    
    rand = int(len(free) * random.random())
    print(rand)
    
    square_num = (free[rand][0]*3) + (free[rand][1]+1)
    print(square_num)
    
    put_in_board(board, mark, square_num)
    #print("computer move shown")
    
def game_with_computer(board):
    game_end = False
    cnt = 0
    
    while game_end == False:
        if cnt % 2 == 0:
            user_move(board)
            print_board_and_legend(board)
            winner = check_winner(board)
            
            cnt += 1
                
        else:
            make_random_move(board, "O")
            print_board_and_legend(board)
            winner = check_winner(board)
            
            cnt+=1
        
        if winner == "X":
                print("you won!")
                break
        elif winner == "O":
                print("computer won,you SUCK :DDDDDDD")
                break
        
        #seperate from above since the board migt start unempty
        temp = 0
        for i in range (len(board)):
            for j in range (len(board[0])):
                if board[i][j] == "X" or board[i][j] == "O":
                    temp += 1
        
        if temp == 9:
            game_end = True
            winner = check_winner(board)
            if winner == "O":
                print("computer won,you SUCK :DDDDDDD")
            elif winner == "X":
                print("you won!")
            else:
                print("no on wins this round, play again!")
            
                
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range (3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None
        
    
    
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [["O", " ", "X"],
             [" ", "X", " "],
             ["O", " ", " "]]
    
    print_board_and_legend(board)  
    print(get_cord(9))
    print(get_free_squares(board))
    #print_board_and_legend(board)
    game_with_computer(board)
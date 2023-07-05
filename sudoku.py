board = [[0,0,0,0,1,0,0,0,4],
         [4,0,0,0,9,0,1,7,2],
         [2,1,0,0,8,0,9,0,0],
         [0,3,4,7,2,8,6,0,0],
         [0,0,0,1,0,0,3,4,7],
         [7,0,1,0,0,0,2,0,0],
         [1,2,0,0,0,0,4,0,0],
         [0,0,5,8,0,2,0,0,0],
         [8,7,0,9,0,1,0,2,0]]
def print_board():
    #print first line
    print('----' * len(board) + '-')
    #print details
    for row in range(len(board)):
        row_str = ''
        for col in range(len(board)):
            row_str += '| ' + str(board[row][col]) + ' '
        print(row_str + '|')
        print('----' * len(board) + '-')

#check if the number is valid in row, col, box condition
def is_valid(board, row, col, num):
    #row
    for i in range(9):
        if board[row][i] == num:
            return False

    #col
    for i in range(9):
        if board[i][col] == num:
            return False

    #box
    boxRow = row - row % 3
    boxCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + boxRow][j + boxCol] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        #recursion
                        if solve(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True                    

print('Before !')    
print_board()

if solve(board):
    print('After !')
    print_board()
else:
    print('Can not solve this. Sorry x.x !!!')

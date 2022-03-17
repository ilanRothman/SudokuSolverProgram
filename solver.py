board = [[0,0,3,7,0,1,6,0,0],
         [0,4,0,0,0,0,0,0,5],
         [0,0,0,0,8,0,0,0,0],
         [0,0,0,0,9,0,2,0,0],
         [0,3,0,2,0,8,0,4,0],
         [0,0,8,0,6,0,0,0,0],
         [0,0,0,9,0,0,0,0,0],
         [0,0,1,3,0,2,7,0,0],
         [7,0,0,0,0,0,0,6,0]]



def valid(board,num,pos):
        # check row first
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False
        #check col
        for j in range(len(board)):
            if board[j][pos[1]] == num and pos[0] != j:
                return False
        #check box
        box_X = pos[0] // 3
        box_Y = pos[1] // 3

        for i in range(box_X*3,box_X*3 +3):
            for j in range(box_Y*3,box_Y*3 +3):
                if board[i][j] == num and pos != (i,j):
                    return False
        return True

def pickEmptySquare(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row,col)
    return False

def Print_Board(board):
    for row in range(len(board)):
        if row % 3 == 0:
            print( "- - - - - - - - - - - - - - - - ")
        for sqr in range(len(board[row])):
            if sqr % 3 == 0 and sqr != 0:
                print("|", end=" ")
            print(board[row][sqr]," ",end="")
            if sqr == 8:
                print()


def solve(board):
    assignable = pickEmptySquare(board)
    if not assignable:
        print("solved!")
        return True

    for i in range(1,10):
        if valid(board,i,assignable):
            board[assignable[0]][assignable[1]] = i
            Print_Board(board)
            print("\n\n\nstill solving...\n\n\n\n\n")

            if solve(board):
                return True
            board[assignable[0]][assignable[1]] = 0

    return False
solve(board)


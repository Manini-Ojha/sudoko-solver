print("Welcome to Sudoku Solver")
board = [[0,0,0,1,0,4,9,0,0],
         [0,8,0,0,0,2,0,0,0],
         [0,0,0,0,0,0,0,3,8],
         [8,0,0,2,0,0,7,0,1],
         [0,2,9,0,0,0,8,5,0],
         [5,0,7,0,0,6,0,0,9],
         [4,9,0,0,0,0,0,0,0],
         [0,0,0,5,0,0,0,2,0],
         [0,0,5,7,0,8,0,0,0]]

fillValues = [1,2,3,4,5,6,7,8,9]

box1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
box2 = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
box3 = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
box4 = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
box5 = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
box6 = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
box7 = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
box8 = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
box9 = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]

box = [box1,box2,box3,box4,box5,box6,box7,box8,box9]

def printBoard (board):
    for row in board:
        print(row)


def validateBoardCompletion(myboard):
    for i in range(9):
        for j in range(9):
            if (myboard[i][j] == 0):
                return False
        return True


def nextPosition(x,y):
    next_y = y+1
    next_x = x
    if(next_y >= 9):
        next_x = x+1
        next_y = next_y %9
    return (next_x, next_y)


def isValidValue(x,y,value,myboard):
    #Check in row
    for i in range(9):
        if (i == y):
            continue
        elif (myboard[x][i] == value):
            return False

    #check in column
    for i in range(9):
        if (i == x):
            continue
        elif (myboard[i][y] == value):
            return False

    #check in box
    # Calculte box number

    valuex = x//3
    valuey = y//3
    
    boxNum = (valuex*3) + valuey
    #print(boxNum)

    boxCoord = box[boxNum]
    for cell in boxCoord:
        if (myboard[cell[0]][cell[1]] == value):
            return False

    return True


def SolveBoard(x,y,localBoard):

    print(str(x) +"," + str(y))
    if (localBoard[x][y] != 0):
        print("position is already filled. Skip " + str(x) + "," +str(y))
        (next_x,next_y) = nextPosition(x,y)
        if (next_x > 8):
            print("we have reached last position")
            return True
        x = next_x
        y = next_y
        return SolveBoard(x,y, localBoard)
    else:
       for i in fillValues:
           if (isValidValue(x,y,i,localBoard)):
               localBoard[x][y] = i
               print("Going with " + str(i))
               (next_x, next_y) = nextPosition(x,y)
               if (next_x > 8):
                   print("we have reached last position")
                   return True
               if (SolveBoard(next_x,next_y,localBoard)):
                   return True
               else:
                   print("blacktrack for " + str(x)+ " , " +str(y) + " value - " + str(localBoard[x][y]))
                   localBoard[x][y] = 0

    return False

if (SolveBoard(0,0,board)):
    printBoard(board)

else:
    print("Can't solve")
    printBoard(board)

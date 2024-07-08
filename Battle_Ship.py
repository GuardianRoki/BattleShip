

def createBoard():
    
    board = [["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","0","0"]]
    return board

def printBoard(board):
    grid = f"""
         1   2   3   4   5
       ---------------------
    A: | {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} |
       ---------------------
    B: | {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]} |
       ---------------------
    C: | {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} | 
       ---------------------
    D: | {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} | 
       ---------------------
    E: | {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} |
       ---------------------
    """

    print(grid)

def bombDropping(targetLoc, userBomb):
    targetLoc = userBomb.split(",")
    yPos = targetLoc[1]
    xPos = targetLoc[0]

    return targetLoc


userBomb = input("Please select a section to hit with your artilery: ")
targetLoc = None

def main():

    p1ShipList = []
    p2ShipList = []
    p1HitList = []
    p2HitList = []
    boardTransfer = createBoard()
    printBoard(boardTransfer)
    userBomb = input("Please select a section to hit with your artilery: ")
    targetLoc = None
    
    return userBomb


main()

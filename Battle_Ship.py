import random

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

def bombTarget(targetLoc, userBomb, board):
    if userBomb in p1HitList or userBomb in p2HitList:
        print("Please Input a valid coord pair! ")
        userBomb = input("Please select a section to hit with your artilery: ")
    else:
        print()
    targetLoc = userBomb.split(",")
    yPos = targetLoc[0]
    xPos = targetLoc[1]
    if int(xPos) > 5 or int(xPos) < 0:
        print("Please input a valid target! ")
        userBomb = input("Please select a section to hit with your artilery: ")
        bombTarget(targetLoc, userBomb, board)
    if yPos == "A" or yPos == "a":
        board[0][int(xPos) - 1] = "X"
        printBoard(boardTransfer)
    if yPos == "B" or yPos == "b":
        board[1][int(xPos)- 1] = "X"
        printBoard(boardTransfer)
    if yPos == "C" or yPos == "c":
        board[2][int(xPos)- 1] = "X"
        printBoard(boardTransfer)
    if yPos == "D" or yPos == "d":
        board[3][int(xPos)- 1] = "X"
        printBoard(boardTransfer)
    if yPos == "E" or yPos == "e":
        board[4][int(xPos)- 1] = "X"
        printBoard(boardTransfer)
    else:
        print("Please input a valid target!")
        userBomb = input("Please select a section to hit with your artilery: ")
        bombTarget(targetLoc, userBomb, board)
    p1HitList.append(userBomb)

    return targetLoc and board



playing = True
targetLoc = None
p1ShipList = []
p2ShipList = []
p1HitList = []
p2HitList = []
boardTransfer = createBoard()
printBoard(boardTransfer)
userBomb = input("Please select a section to hit with your artilery: ")
bombTarget(targetLoc, userBomb, boardTransfer)
    



    


while(playing):
    printBoard(boardTransfer)
    userBomb = input("Please select a section to hit with your artilery: ")
    bombTarget(targetLoc, userBomb, boardTransfer)




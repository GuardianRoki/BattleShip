import random
import os
import keyboard

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



def bombTarget(userBomb, board):
  
    if userBomb in p1HitList or userBomb in p2HitList:
        print("You've already hit this space! ")
        userBomb = input("Please select a section to hit with your artilery: ")

    targetLoc = userBomb.split(",")
    yPos = targetLoc[0]
    xPos = targetLoc[1]
    placehold = f"({yPos},{xPos})"
    print(placehold)

    if placehold not in p1Ship1:

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


    elif placehold in p1Ship1:

        if yPos == "A" or yPos == "a":

            board[0][int(xPos) - 1] = "~"
            printBoard(boardTransfer)
            print("You Hit!")

        if yPos == "B" or yPos == "b":

            board[1][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            print("You Hit!")

        if yPos == "C" or yPos == "c":

            board[2][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            print("You Hit!")

        if yPos == "D" or yPos == "d":

            board[3][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            print("You Hit!")

        if yPos == "E" or yPos == "e":

            board[4][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            print("You Hit!")

        p1HitList.append(userBomb)

        return targetLoc and board


def shipCreate(p1Ship1, p1Ship2, p2Ship1, p2Ship2, player):

    if player == "Player 1":

        # horVert = random.randint(0,1)
        # if horVert = 0:
        #   generate coordinates horizontally
        # elif horVert = 1:
        #   generate coordinates vertically 
        generateX = random.randint(0,4)
        xLetter = strConvert(generateX)
        generateY = random.randint(0,4)
        str_correlate = f"({xLetter},{generateY})"
        print(str_correlate)

        p1Ship1.append(str_correlate)

    if player == "Player 2":

        # horVert = random.randint(0,1)
        # if horVert = 0:
        #   generate coordinates horizontally
        # elif horVert = 1:
        #   generate coordinates vertically 
        generateX = random.randint(0,4)
        xLetter = strConvert(generateX)
        generateY = random.randint(0,4)
        str_correlate = f"({xLetter},{generateY})"
        print(str_correlate)

        p2Ship1.append(str_correlate)
    
    
def strConvert(col):
     
     newcol = ""
     if col == 0:
          newcol = "A"
     elif col == 1:
          newcol = "B"
     elif col == 2:
          newcol = "C"
     elif col == 3:
          newcol = "D"
     elif col == 4:
          newcol = "E"

     return newcol


playing = True

p1Ship1 = []
p1Ship2 = []

p2Ship1 = []
p2Ship2 = []

p1HitList = []
p2HitList = []

boardTransfer = createBoard()
printBoard(boardTransfer)

player = "Player 1"
shipCreate(p1Ship1, p1Ship2, p2Ship1, p2Ship2, player)

player = "Player 1"
    
# board1Transfer = createP1Board()
# board2Transfer = createP2Board()

print("\nWelcome to BattleShip!\n")
print("In BattleShip, two players engage in a turn-based battle, competing to sink all of the opponent's ships before they lose all of their own.\n")
print("Player 1 will start first. If an opposing ship is hit, your turn will continue. Otherwise, player 2's turn will begin.\n")

while(playing):

    
    player = "Player 1"
    print("\nIt is player 1's turn.\n")

    userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
    bombTarget(userBomb, boardTransfer)
    # bombTarget(userBomb, board1Transfer)


    
    # print("\nPress space when you are ready to end your turn\n")

    # player = "Player 2"
    # print("\nIt is player 2's turn.\n")

    # userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
    # bombTarget(userBomb, boardTransfer)
    # # bombTarget(userBomb, board2Transfer)


    # print("\nPress space when you are ready to end your turn\n")

    # continue



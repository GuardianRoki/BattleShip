import random
import os
import keyboard

def createP1Board():
    
    board = [["O","O","O","O","O"],
            ["O","O","O","O","O"],
            ["O","O","O","O","O"],
            ["O","O","O","O","O"],
            ["O","O","O","O","O"]]
    return board

def printP1Board(board):
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

def createP2Board():
    
    board = [["O","O","O","O","O"],
            ["O","O","O","O","O"],
            ["O","O","O","O","O"],
            ["O","O","O","O","O"],
            ["O","O","O","O","O"]]
    return board

def printP2Board(board):
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


def bombTarget(targetLoc, userBomb, board, player):

    if userBomb in p1HitList or userBomb in p2HitList:
        while userBomb in p1HitList or userBomb in p2HitList:
                
            print("Please Input a valid coord pair! ")
            userBomb = input("Please select a section to hit with your artilery: ")
            continue

    targetLoc = userBomb.split(",")
    yPos = targetLoc[0]
    xPos = targetLoc[1]
    if player == "Player 1":

        if yPos == "A" or yPos == "a":
            board[0][int(xPos) - 1] = "X"
            printP1Board(board)
        if yPos == "B" or yPos == "b":
            board[1][int(xPos)- 1] = "X"
            printP1Board(board)
        if yPos == "C" or yPos == "c":
            board[2][int(xPos)- 1] = "X"
            printP1Board(board)
        if yPos == "D" or yPos == "d":
            board[3][int(xPos)- 1] = "X"
            printP1Board(board)
        if yPos == "E" or yPos == "e":
            board[4][int(xPos)- 1] = "X"
            printP1Board(board)

    elif player == "Player 2":

        if yPos == "A" or yPos == "a":
            board[0][int(xPos) - 1] = "X"
            printP2Board(board)
        if yPos == "B" or yPos == "b":
            board[1][int(xPos)- 1] = "X"
            printP2Board(board)
        if yPos == "C" or yPos == "c":
            board[2][int(xPos)- 1] = "X"
            printP2Board(board)
        if yPos == "D" or yPos == "d":
            board[3][int(xPos)- 1] = "X"
            printP2Board(board)
        if yPos == "E" or yPos == "e":
            board[4][int(xPos)- 1] = "X"
            printP2Board(board)

    p1HitList.append(userBomb)

    return targetLoc and board



playing = True
targetLoc = None
p1ShipList = []
p2ShipList = []
p1HitList = []
p2HitList = []
board1Transfer = createP1Board()
board2Transfer = createP2Board()
printP2Board(board2Transfer)


while(playing):

    print("Welcome to BattleShip!\n")
    print("In BattleShip, two players engage in a turn-based battle, competing to sink all of the opponent's ships before they lose all of their own.\n")
    print("Player 1 will start first. If an opposing ship is hit, your turn will continue. Otherwise, player 2's turn will begin.\n")

    print("Press Space to begin\n")
    keyboard.wait(" ")
    os.system('cls')

    player = "Player 1"
    printP1Board(board1Transfer)
    userBomb = input("\nPlease select a section to hit with your artilery: ")
    bombTarget(targetLoc, userBomb, board1Transfer, player)




    playing = False

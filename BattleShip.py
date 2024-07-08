import random
import os

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

def placement(board,player, p1HitList, p2HitList):

    ""
    placehold = input("Enter coordinates (Row,Col): ")
    location = placehold.split(",")
    str_correlate = f"({location})"
    if str_correlate in p1HitList or str_correlate in p2HitList:
          while str_correlate in p1HitList or str_correlate in p2HitList:
               
               placehold = ("That space has already been hit. Please reselect: ")
               str_correlate = f"({location})"
        
    if player == "Player 1":
        p1HitList.append(str_correlate)
    elif player == "Player 2":
        p2HitList.append(str_correlate)

def strConvert(col):
     
     if col == "A":
          newcol = 0
     elif col == "B":
          newcol = 1
     elif col == "C":
          newcol = 2
     elif col == "D":
          newcol = 3
     elif col == "E":
          newcol = 4

     return newcol


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
    board1Transfer = createP1Board()
    board2Transfer = createP2Board()


    printP1Board(board1Transfer)
    userBomb = input("Please select a section to hit with your artilery: ")
    targetLoc = None

    return userBomb


main()

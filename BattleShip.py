import random
import os
import time
from colorama import Fore, Back, Style


def createP1Board(gridSize):
    

    board = [['O'] * int(gridSize) for col in range(int(gridSize))]
    # intercept = str(board).replace("],", '],\n')
    

    return board

def createP2Board(gridSize):
    

    board = [['O'] * int(gridSize) for col in range(int(gridSize))]
    # intercept = str(board).replace("],", '],\n')
    

    return board

# def printBoard(board):
#     grid = f"""
#          1   2   3   4   5
#        ---------------------
#     A: | {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} |
#        ---------------------
#     B: | {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]} |
#        ---------------------
#     C: | {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} | 
#        ---------------------
#     D: | {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} | 
#        ---------------------
#     E: | {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} |
#        ---------------------
#     """


    # print(grid)

def printBoard(board):
    
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for item in range(1, len(board) + 1):
        print("   " +  str(item), end = " ")
    print("")
    for it in range(len(board)):
        print(keys[it] + ":", end = " | ")
        for item in range(len(board)):
            print(board[it][item], end = " | ")
        print("")



def bombTarget(userBomb, board):
  
    if userBomb in p1HitList or userBomb in p2HitList:
        print("You've already hit this space! ")
        userBomb = input("Please select a section to hit with your artilery: ")

    targetLoc = userBomb.split(",")
    yPos = targetLoc[0]
    xPos = targetLoc[1]
    placehold = f"({yPos},{xPos})"
    print(placehold)


    if placehold not in p1Dest and placehold not in p1Sub and placehold not in p1Cruise and placehold not in p1Battle and placehold not in p1Air:

        if yPos == "A" or yPos == "a":

            board[0][int(xPos) - 1] = "X"
            printBoard(boardTransfer)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "B" or yPos == "b":

            board[1][int(xPos)- 1] = "X"
            printBoard(boardTransfer)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "C" or yPos == "c":

            board[2][int(xPos)- 1] = "X"
            printBoard(boardTransfer)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "D" or yPos == "d":

            board[3][int(xPos)- 1] = "X"
            printBoard(boardTransfer)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "E" or yPos == "e":

            board[4][int(xPos)- 1] = "X"
            printBoard(boardTransfer)
            p1HitList.append(userBomb)
            missileLaunchO()


    elif placehold in p1Dest or placehold in p1Sub or placehold in p1Cruise or placehold  in p1Battle or placehold  in p1Air:

        if yPos == "A" or yPos == "a":

            board[0][int(xPos) - 1] = Fore.RED + "~" + Fore.RESET
            printBoard(boardTransfer)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "B" or yPos == "b":

            board[1][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "C" or yPos == "c":

            board[2][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "D" or yPos == "d":

            board[3][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            p1HitsHit.append(userBomb) 
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "E" or yPos == "e":

            board[4][int(xPos)- 1] = "~"
            printBoard(boardTransfer)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            



        return targetLoc and board

def shipCreateS(numShips,  gridSize, player, ):

    if numShips == 1:

        createDest(player, gridSize, placementType)

    if numShips == 2:

        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)

    if numShips == 3:
        
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)

    if numShips == 4:
        
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        createBattle(player, gridSize , placementType)
    
    if numShips == 5:
    
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        createBattle(player, gridSize, placementType)
        createAirC(player, gridSize, placementType)
    
    # if player == "Player 1":

    #     # horVert = random.randint(0,1)
    #     # if horVert = 0:
    #     #   generate coordinates horizontally
    #     # elif horVert = 1:
    #     #   generate coordinates vertically 
    #     generateX = random.randint(0,4)
    #     xLetter = strConvert(generateX)
    #     generateY = random.randint(0,4)
    #     str_correlate = f"({xLetter},{generateY})"
    #     print(str_correlate)

    #     p1Ship1.append(str_correlate)

    # if player == "Player 2":

    #     # horVert = random.randint(0,1)
    #     # if horVert = 0:
    #     #   generate coordinates horizontally
    #     # elif horVert = 1:
    #     #   generate coordinates vertically 
    #     generateX = random.randint(0,4)
    #     xLetter = strConvert(generateX)
    #     generateY = random.randint(0,4)
    #     str_correlate = f"({xLetter},{generateY})"


    #     p2Ship1.append(str_correlate)
    print()

def createDest(playtype, gridSize, placementType):
        if placementType == 1:
        #horVert = random.randint(0,1)
        # if horVert = 0:
        #   generate coordinates horizontally
        # elif horVert = 1:
        #   generate coordinates vertically 
            generateX = random.randint(0,int(gridSize) - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(0,int(gridSize) - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p1Dest.append(str_correlate)
        elif placementType == 0:
            shipLoc = input("Please input a location to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]
            str_correlate = f"({xLetter},{yNumber})"
            print(str_correlate)
            p1Dest.append(str_correlate)

def createSub(playtype, ):
    if playtype == 1:
        #horVert = random.randint(0,1)
        # if horVert = 0:
        #   generate coordinates horizontally
        # elif horVert = 1:
        #   generate coordinates vertically 
        generateX = random.randint(0,4)
        xLetter = strConvert(generateX)
        generateY = random.randint(0,4)
        str_correlate = f"({xLetter},{generateY})"
        p1Dest.append(str_correlate)

    elif playtype == 2:
        shipLoc = input("Please input a location to sail your ship: ")
        parkedShip = shipLoc.split(",")
        xLetter = parkedShip[0]
        yNumber = parkedShip[1]
        str_correlate = f"({xLetter},{yNumber})"
        p1Sub.append(str_correlate)

def createCruise():
    print()

def createBattle():
    print()

def createAirC():
    print()

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

def gameEnding():
    if len(p1HitList) >= 5:
        playing = False
        print("Your enemy managed to escape! You gotta be quicker next time! ")
        return playing
    elif len(p1HitsHit) == numShips:
        playing = False
        print("You banished all your opponents! Your name will go down in history as a great seamen")
        return playing
    else:
        playing = True
        return playing

# def shipManual():
#     shipLoc = input("Please input a location to sail your ship: ")
#     parkedShip = shipLoc.split(",")
#     xLetter = parkedShip[0]
#     yNumber = parkedShip[1]
#     str_correlate = f"({xLetter},{yNumber})"
#     p1.append(str_correlate)

def aresenal():
    if len(p1HitList) == 0:
        print("""
_______
|<==={| 
|<==={| 
|<==={| 
|<==={|
|<==={|
|_____|
               """)
    elif len(p1HitList) == 1:
        print("""
_______
|<==={| 
|<==={| 
|<==={| 
|<==={|
|  .  |
|_____|""")
    elif len(p1HitList) == 2:
        print("""
_______
|<==={| 
|<==={| 
|<==={| 
| ,   |
|  .  |
|_____|""")
    elif len(p1HitList) == 3:
        print("""
_______
|<==={| 
|<==={| 
|     | 
| ,   |
|  .  |
|_____|""")
    elif len(p1HitList) == 4:
        print("""
_______
|<==={| 
|   . | 
|     | 
| ,   |
|  .  |
|_____|
""")
    else:
        print("Out of Ammo!")

def misslieLaunchS():
        print("""     
        -}===>
        """)
        time.sleep(.3)
        print("""     
           ---}===>
        """)
        time.sleep(.3)
        print("""     
             -----}===>
        """)
        time.sleep(.3)
        print("""
                                 ___|___
               -------}===>      |     |
                                 \_____/""")
        time.sleep(.3)
        print("""
                                 ___|___
                 ---------}===>  |     |
                                 \_____/""")
        time.sleep(.3)
        print("""
                                 ___|___
                 ---------BOOOMM )     |
                                 \_____/""")

def missileLaunchO():
    fiftychance = random.randint(0,1)
    if fiftychance == 1:
        print("""     
        -}===>
        """)
        time.sleep(.3)
        print("""     
        ---}===>
        """)
        time.sleep(.3)
        print("""     
        -----}===>
        """)
        time.sleep(.3)
        print("""      
                          /     |
        -------}===>   __/       |
                      /           |
        """)
        time.sleep(.3)
        print("""
                          /     |
        ---------}===> __/       |
                      /           |
        """)
        time.sleep(.3)
        print("""           
                        (        )
        --------------(   BOOM!   )
                        (        )
        """)
        print("You hit an innocent island...")
    else:
        print("""     
        -}===>
        """)
        time.sleep(.3)
        print("""     
        ---}===>
        """)
        time.sleep(.3)
        print("""     
        -----}===>
        """)
        time.sleep(.3)
        print("""      
                        
        -------}===>  
                
        """)
        time.sleep(.3)
        print("""           
                      (~~~~~~~~~)
    ------------}===>(~~~~~~~~~~~~)
                      (~~ >(^) ~~)
        """)
        print("THE POOR FISHIES")

def gmode():
    playType = int(input("Enter 1 for singleplayer, 2 for co-op: "))
    return playType

gridSize = input("\nEnter your grid size (#): ")
numShips = int(input("How many ships would you like to have? (Max 5): "))
gooping = True
playing = gooping
placehold = None
playType = None

p1Ship1 = []
p1Dest = []
p1Sub = []
p1Cruise = []
p1Battle = []
p1Air = []
p1Ship2 = []

p2Ship1 = []
p2Ship2 = []

p1HitList = []
p2HitList = []

p1HitsHit = []

player = "Player 1"
    
# board1Transfer = createP1Board()
# board2Transfer = createP2Board()

gmode()

print("\nWelcome to BattleShip!\n")
print("In BattleShip, two players engage in a turn-based battle, competing to sink all of the opponent's ships before they lose all of their own.\n")
print("Player 1 will start first. If an opposing ship is hit, your turn will continue. Otherwise, player 2's turn will begin.\n")
print("Ships that are sailing will be Green and Ships that are sunk will be Red!")                              
placementType = int(input("Type 1 to automatically place ships or 0 to manually place ships: "))
shipCreateS(numShips,  gridSize, player, )



boardTransfer = createP1Board(gridSize)
printBoard(boardTransfer)

while(gooping):

    if playType == 1:
        print("\nIt is player 1's turn.\n")
        
        userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
        bombTarget(userBomb, boardTransfer)
        time.sleep(.7)
        aresenal()
        gooping = gameEnding()
    


    
    # print("\nPress space when you are ready to end your turn\n")

    # player = "Player 2"
    # print("\nIt is player 2's turn.\n")

    # userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
    # bombTarget(userBomb, boardTransfer)
    # # bombTarget(userBomb, board2Transfer)


    # print("\nPress space when you are ready to end your turn\n")

    # continue



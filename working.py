import random
import os
import time
from colorama import Fore, Back, Style

# Creates a board for player 1's ships & what the enemy has hit

def createP1BoardDef(gridSize):
    

    board = [['O'] * int(gridSize) for col in range(int(gridSize))]
    # intercept = str(board).replace("],", '],\n')
    

    return board

# Creates a board for player 1's attack coordinates

def createP1BoardAtk(gridSize):
    

    grid = [['O'] * int(gridSize) for col in range(int(gridSize))]
    # intercept = str(board).replace("],", '],\n')
    

    return grid

# Creates a board for player 2 (or computer) ships & What the enemy has hit

def createP2BoardDef(gridSize):
    

    field = [['O'] * int(gridSize) for col in range(int(gridSize))]
    # intercept = str(board).replace("],", '],\n')
    

    return field

# Creates a board for player 2 (or computer) attack coordinates

def createP2BoardAtk(gridSize):
    

    domain = [['O'] * int(gridSize) for col in range(int(gridSize))]
    # intercept = str(board).replace("],", '],\n')
    

    return domain

def printBoard(board):
    
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    print("   ", end="") #adds extra space before the print statement
    for item in range(1, len(board) + 1):
        end_str = " "
        if item > 9: # if number is two digits it will remove the space between them
            end_str = ""
        print("  " +  str(item).strip(), end = end_str)
    print("   ")
    for it in range(len(board)):
        print(keys[it] + ":", end = " | ")
        for item in range(len(board)):
            print(board[it][item], end = " | ")
        print(" ")

        intercept = str(board).replace("],", '],\n')
    return intercept

def bombTarget(userBomb, board, ):
    if userBomb in p1HitList or userBomb in p2HitList:
        print("You've already hit this space! ")
        userBomb = input("Please select a section to hit with your artilery: ")

    targetLoc = userBomb.split(",")
    yPos = targetLoc[0]
    xPos = targetLoc[1]
    placehold = f"({yPos},{xPos})"
    print(placehold)

    if placehold not in p1Dest and placehold not in p1Sub and placehold not in p1Cruise and placehold not in p1Battle and placehold not in p1Air:

        boardpos = strConvert(yPos)
        board[boardpos][int(xPos) - 1] = "X"
        printBoard(board)
        p1HitList.append(userBomb)
        missileLaunchO()

    elif placehold in p1Dest or placehold in p1Sub or placehold in p1Cruise or placehold  in p1Battle or placehold  in p1Air:

        boardpos = strConvert(yPos)
        board[boardpos][int(xPos) - 1] = "~"
        printBoard(board)
        p1HitList.append(userBomb)
        misslieLaunchS()
        print("You Hit!")

        return targetLoc and board

def shipCreateS(numShips, gridSize, player, board, newCol, ):

    if numShips == 1:

        createDest(player, gridSize, placementType, newCol, board)
        

    if numShips == 2:

        printBoard(board)
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        printBoard(board)

    if numShips == 3:
        
        print(board)
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        print(board)

    if numShips == 4:
        print(board)
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        createBattle(player, gridSize , placementType)
        print(board)
    
    if numShips == 5:
        
        print(board)
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        createBattle(player, gridSize, placementType)
        createAirC(player, gridSize, placementType)
        print(board)

def createDest(playType, gridSize, placementType, newCol, board):
    if player == "Player 1":
        if placementType == 1:
            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvertc(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            if orientation == 1:
                #vertical
                if generateX == 0:
                    board[generateX][generateY] = "#"
                    board[generateX + 1][generateY] = "#"
                elif generateX == (gridSize - 1):
                    board[generateX][generateY] = "#"
                    board[generateX - 1][generateY] = "#"
                else:
                    toporbottom = random.randint(0,1)
                    if toporbottom == 0:
                        #top
                        board[generateX][generateY] = "#"
                        board[generateX - 1][generateY] = "#"
                    elif toporbottom == 1:
                        #bottom
                        board[generateX][generateY] = "#"
                        board[generateX + 1][generateY] = "#"
            elif orientation == 0:
                #horiz
                if generateY == 1:
                    board[generateX][generateY] = "#"
                    board[generateX][generateY + 1] = "#"
                elif generateY == (gridSize - 1):
                    board[generateX][generateY] = "#"
                    board[generateX][generateY - 1] = "#"
                else:
                    toporbottom = random.randint(0,1)
                    if toporbottom == 0:
                        #right
                        board[generateX][generateY] = "#"
                        board[generateX][generateY + 1] = "#"
                    elif toporbottom == 1:
                        #left
                        board[generateX][generateY] = "#"
                        board[generateX][generateY - 1] = "#"
            printBoard(board)
            p2Dest.append(str_correlate)
        elif placementType == 0:
            printBoard(board)
            shipLoc = input("Please input a location to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]
            str_correlate = f"({xLetter},{yNumber})"
            p2Dest.append(str_correlate)
            newCol = strConvert(xLetter)
            board[newCol][int(yNumber) - 1] = "#"
            shipLoc2 = input("Please enter the value of a cell touching yours either vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = parkedShip2[1]
            str_correlate2 = f"({xLetter2},{yNumber})"
            p2Dest.append(str_correlate2)
            newCol = strConvert(xLetter2)
            board[newCol][int(yNumber2) -1] = "#"
            printBoard(board)


    elif player == "Player 2":
        if placementType == 1:
        #horVert = random.randint(0,1)
        # if horVert= 0:
        #   generate  coordinates horizontally
        # elif horVert = 1:
        #   generate coordinates vertically 
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvertc(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p1Dest.append(str_correlate)
        elif placementType == 0 and playType == 2:
            shipLoc = input("Please input a location to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]
            str_correlate = f"({xLetter},{yNumber})"
            print(str_correlate)
            p1Dest.append(str_correlate)
            strConvert(xLetter)
        elif placementType == 0 and playType == 1:
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p1Dest.append(str_correlate)

def createSub(gridSize, placementType):
    if player == "Player 1":
        if placementType == 1:
            # horVert = random.randint(0,1)
            # if horVert == 0:
                
            # elif horVert == 1:

            #generate coordinates vertically 
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p2Dest.append(str_correlate)
        elif placementType == 0:
            shipLoc = input("Please input a location to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]
            str_correlate = f"({xLetter},{yNumber})"
            print(str_correlate)
            p2Dest.append(str_correlate)
    elif player == "Player 2":
        if placementType == 1:
        #horVert = random.randint(0,1)
        # if horVert= 0:
        #   generate  coordinates horizontally
        # elif horVert = 1:
        #   generate coordinates vertically 
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p1Dest.append(str_correlate)
        elif placementType == 0 and playType == 2:
            shipLoc = input("Please input a location to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]
            str_correlate = f"({xLetter},{yNumber})"
            print(str_correlate)
            p1Dest.append(str_correlate)
        elif placementType == 0 and playType == 1:
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p1Dest.append(str_correlate)

def createCruise():
    print()

def createBattle():
    print()

def createAirC():
    print()

def strConvert(col):

    keysLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    newCol = keysLetters.index(col)



    return newCol

def gameEnding():
    if len(p1HitList) >= 5:
        playing = False
        print("Your enemy managed to escape! You gotta be quicker next time! ")
        return playing
    elif len(shipsSunk) == numShips:
        playing = False
        print("You banished all your opponents! Your name will go down in history as a great seamen")
        return playing
    else:
        playing = True
        return playing

# def listint():

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
                                 |_____/""")
        time.sleep(.3)
        print("""
                                 ___|___
                 ---------}===>  |     |
                                 |_____/""")
        time.sleep(.3)
        print("""
                                 ___|___
                 ---------BOOOMM )     |
                                 |_____/""")

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
    gameMode = int(input("Enter 1 for singleplayer, 2 for co-op: "))
    return gameMode

def compTarget(board):
    bombX = random.randint(0,gridSize - 1)
    xLetter = strConvertc(bombX)
    bombY = random.randint(1,gridSize - 1)
    placeholdc = f"({xLetter},{bombY})"
    print("we are doing this too " + placeholdc)
    if placehold in p2HitList or placehold in p2HitsHit:
        print("You've already hit this space! ")
        compTarget(board)
    if placeholdc not in p2Dest and placehold not in p2Sub and placehold not in p2Cruise and placehold not in p2Battle and placehold not in p2Air:

        board[bombX][bombY - 1] = "X"
        printBoard(board)
        p2HitList.append(placeholdc)
        missileLaunchO


            # if xLetter == "A" or xLetter == "a":

            #     board[0][int(bombY) - 1] = "X"
            #     printBoard(board)
            #     p2HitList.append(userBomb)
            #     missileLaunchO()

            # if xLetter == "B" or xLetter == "b":

            #     board[1][int(bombY)- 1] = "X"
            #     printBoard(board)
            #     p2HitList.append(userBomb)
            #     missileLaunchO()

            # if xLetter == "C" or xLetter == "c":

            #     board[2][int(bombY)- 1] = "X"
            #     printBoard(board)
            #     p2HitList.append(userBomb)
            #     missileLaunchO()

            # if xLetter == "D" or xLetter == "d":

            #     board[3][int(bombY)- 1] = "X"
            #     printBoard(board)
            #     p2HitList.append(userBomb)
            #     missileLaunchO()

            # if xLetter == "E" or xLetter == "e":

            #     board[4][int(bombY)- 1] = "X"
            #     printBoard(board)
            #     p2HitList.append(userBomb)
            #     missileLaunchO()

    elif placeholdc in p2Dest or placehold in p2Sub or placehold in p2Cruise or placehold  in p2Battle or placehold  in p2Air:

        board[bombX][bombY - 1] = "X"
        printBoard(board)
        p2HitList.append(placeholdc)
        misslieLaunchS()

            # if xLetter == "A" or xLetter == "a":

            #     board[0][int(bombY) - 1] = Fore.RED + "~" + Fore.RESET
            #     printBoard(board)
            #     p2HitsHit.append(userBomb)
            #     misslieLaunchS()
            #     print("You Hit!")
                

            # if xLetter == "B" or xLetter == "b":

            #     board[1][int(bombY)- 1] = "~"
            #     printBoard(board)
            #     p2HitsHit.append(userBomb)
            #     misslieLaunchS()
            #     print("You Hit!")
                

            # if xLetter == "C" or xLetter == "c":

            #     board[2][int(bombY)- 1] = "~"
            #     printBoard(board)
            #     p2HitsHit.append(userBomb)
            #     misslieLaunchS()
            #     print("You Hit!")
                

            # if xLetter == "D" or xLetter == "d":

            #     board[3][int(bombY)- 1] = "~"
            #     printBoard(board)
            #     p2HitsHit.append(userBomb) 
            #     misslieLaunchS()
            #     print("You Hit!")
                

            # if xLetter == "E" or xLetter == "e":

            #     board[4][int(bombY)- 1] = "~"
            #     printBoard(board)
            #     p2HitsHit.append(userBomb)
            #     misslieLaunchS()
            #     print("You Hit!")

def strConvertc(col):
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    newCol = keys[col]
    print("I am in here" + str(newCol))

    return newCol





gooping = True
playing = gooping
placehold = None
playType = None
newCol = None
newColn = None



p1Dest = []
p1Sub = []
p1Cruise = []
p1Battle = []
p1Air = []
p1Ship2 = []


p2Dest = []
p2Sub = []
p2Cruise = []
p2Battle = []
p2Air = []
p2Ship2 = []

p2Ship1 = []
p2Ship2 = []

p1HitList = []
p2HitList = []

p1HitsHit = []
p2HitsHit= []

shipsSunk = []

    


playType = gmode()

print("\nWelcome to BattleShip!\n")
print("In BattleShip, two players engage in a turn-based battle, competing to sink all of the opponent's ships before they lose all of their own.\n")
print("Player 1 will start first. If an opposing ship is hit, your turn will continue. Otherwise, player 2's turn will begin.\n")

print("Ships that are " + Fore.BLUE + "sailing" + Fore.RESET + " will be " + Fore.GREEN + "Green" + Fore.RESET + " and ships that have been " + Fore.YELLOW + "sunk " + Fore.RESET + "are "+ Fore.RED + "Red.\n" + Fore.RESET)
  
gridSize = int(input("\nEnter your grid size (# input)[26 Max]: "))
board1TransferDef = createP1BoardDef(gridSize)
board1TransferAtk = createP1BoardAtk(gridSize)
board2TransferDef = createP2BoardDef(gridSize)
board2TransferAtk = createP2BoardAtk(gridSize)

numShips = int(input("How many ships would you like to have? (Max 5): "))

placementType = int(input("Type 1 to automatically place ships or 0 to manually place ships: "))

player = "Player 1"
shipCreateS(numShips,  gridSize, player, board1TransferDef, newCol)

player = "Player 2"
shipCreateS(numShips,  gridSize, player, board2TransferDef, newCol)

player = "Player 1"

while(gooping):

    if playType == 1:
 
        print(f"\nIt is {player}'s turn.\n")

        userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
        bombTarget(userBomb, board1TransferAtk)
        time.sleep(.7)
        aresenal()
        gooping = gameEnding()
        if player == "Player 1":
            player = "Player 2"
        elif player == "Player 2":
            player = "player 1"
        compTarget(board1TransferDef)
        gooping = gameEnding()


    
    # print("\nPress space when you are ready to end your turn\n")

    # player = "Player 2"
    # print("\nIt is player 2's turn.\n")

    # userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
    # bombTarget(userBomb, boardTransfer)
    # # bombTarget(userBomb, board2Transfer)


    # print("\nPress space when you are ready to end your turn\n")

    # continue


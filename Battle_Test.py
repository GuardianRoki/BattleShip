import random
import os
import time
from colorama import Fore, Back, Style


# Creates a board for player 1's ships & what the enemy has hit

def createP1BoardDef(gridSize):

    board = [['O'] * int(gridSize) for col in range(int(gridSize))]    

    return board


# Creates a board for player 1's attack coordinates

def createP1BoardAtk(gridSize):

    grid = [['O'] * int(gridSize) for col in range(int(gridSize))]    

    return grid


# Creates a board for player 2 (or computer) ships & What the enemy has hit

def createP2BoardDef(gridSize):
    
    field = [['O'] * int(gridSize) for col in range(int(gridSize))]
    
    return field


# Creates a board for player 2 (or computer) attack coordinates

def createP2BoardAtk(gridSize):
    
    domain = [['O'] * int(gridSize) for col in range(int(gridSize))]
    
    return domain


# Prints a formatted board based on argument input

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

# Uses player argument & user input to "bomb" location on respective board, marks X if miss and ~ if hit.

def bombTarget(userBomb, board, player):
    if userBomb in p1HitList or userBomb in p2HitList:
        print("You've already hit this space! ")
        userBomb = input("Please select a section to hit with your artilery: ")

    # Splits coordinates into two indexes, letter[0] and number[1]

    targetLoc = userBomb.split(",")
    yPos = targetLoc[0]
    xPos = targetLoc[1]
    placehold = f"({yPos},{xPos})"
    print(placehold)

    # Checks to see if placehold (formatted coordinate pair) was a miss

    if placehold not in p1Dest and placehold not in p1Sub and placehold not in p1Cruise and placehold not in p1Battle and placehold not in p1Air and placehold not in p2Dest and placehold not in p2Sub and placehold not in p2Cruise and placehold not in p2Battle and placehold not in p2Air:

        boardpos = strConvert(yPos)
        board[boardpos][int(xPos) - 1] = "X"
        printBoard(board)
        p1HitList.append(userBomb)
        missileLaunchO()

    # Otherwise, updates the board to display the hit & prints a hit statement depending on which ship was hit & which player hit it.

    elif player == "Player 1":

        if placehold in p1Dest:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p1Dest.remove(placehold)

        elif placehold in p1Sub:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p1Sub.remove(placehold)

        elif placehold in p1Cruise:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p1Cruise.remove(placehold)

        elif placehold in p1Battle:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p1Battle.remove(placehold)

        elif placehold in p1Air:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p1Air.remove(placehold)

    elif player == "Player 2":

        if placehold in p2Dest:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p2Dest.remove(placehold)

        elif placehold in p2Sub:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p2Sub.remove(placehold)

        elif placehold in p2Cruise:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p2Cruise.remove(placehold)

        elif placehold in p2Battle:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p2Battle.remove(placehold)

        elif placehold in p2Air:

            boardpos = strConvert(yPos)
            board[boardpos][int(xPos) - 1] = "~"
            printBoard(board)
            p1HitList.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            p2Air.remove(placehold)

# Creates ships depending on the input (desired number of ships) asked at the start

def shipCreateS(numShips, gridSize, player, board, newCol, ):

    if numShips == 1:

        createDest(player, gridSize, placementType, newCol, board)

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

# Creates a set of 2 points to represent the destroyer (Smallest ship), updates ship lists depending on player argument

def createDest(player, gridSize, placementType, newCol, board):

    if player == "Player 1":

        if placementType == 1:

            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvertc(generateX)
            generateY = gridSize - random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            p2Dest.append(str_correlate)

            shipName = input(f"\n{player}, Name your ship: ")
            p1Destid.append(shipName)

            if orientation == 1:

                Ysubstitute = generateY - 1
                #vertical

                if generateX == 0:

                    board[generateX][Ysubstitute] = "1#"
                    board[generateX + 1][Ysubstitute] = "2#"

                    xLetter3 = strConvertc(generateX + 1)
                    str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                    printBoard(board)

                elif generateX == (gridSize - 1):

                    board[generateX][Ysubstitute] = "3#"
                    board[generateX - 1][Ysubstitute] = "4#"

                    xLetter3 = strConvertc(generateX - 1)
                    str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                    printBoard(board)

                else:

                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][Ysubstitute] = "5#"
                        board[generateX - 1][Ysubstitute] = "6#"
                        
                        xLetter3 = strConvertc(generateX - 1)
                        str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][Ysubstitute] = "7#"
                        board[generateX + 1][Ysubstitute] = "8#"

                        xLetter3 = strConvertc(generateX + 1)
                        str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                        
                        printBoard(board)

            elif orientation == 0:

                #horiz
                Ysubstitute = generateY - 1

                if generateY == 1:

                    board[generateX][Ysubstitute] = "9#"
                    board[generateX][Ysubstitute + 1] = "0#"
                    str_correlate3 = f"({xLetter},{Ysubstitute +2})"
                    
                    printBoard(board)

                elif generateY == (gridSize - 1):

                    board[generateX][Ysubstitute] = "A#"
                    board[generateX][Ysubstitute + 1] = "B#"
                    str_correlate3 = f"({xLetter},{Ysubstitute + 2})"
                    
                    printBoard(board)

                else:

                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][Ysubstitute] = "C#"
                        board[generateX][Ysubstitute + 1] = "D#"
                        str_correlate3 = f"({xLetter},{Ysubstitute + 2})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #left
                        board[generateX][Ysubstitute] = "E#"
                        board[generateX][Ysubstitute + 1] = "F#"
                        str_correlate3 = f"({xLetter},{Ysubstitute + 2})"
                        
                        printBoard(board)

            p2Dest.append(str_correlate3)

        elif placementType == 0:

            #Manual Placement
            printBoard(board)
            shipName = input(f"\n{player}, Name your ship: ")
            p1Destid.append(shipName)

            # Converts coordinates to indexes, Letter[0] & number[1]
            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]

            # Formats the coordinates & adds them to the destroyer list
            str_correlate = f"({xLetter},{yNumber})"
            p2Dest.append(str_correlate)
            newCol = strConvert(xLetter)

            board[newCol][int(yNumber) - 1] = "#"
            shipLoc2 = input("Enter the coordinates of a cell touching yours either vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = parkedShip2[1]
            str_correlate2 = f"({xLetter2},{yNumber})"
            p2Dest.append(str_correlate2)

            newCol = strConvert(xLetter2)
            board[newCol][int(yNumber2) -1] = "#"

    elif player == "Player 2":

        if placementType == 1:

            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvertc(generateX)
            generateY = random.randint(1,gridSize - 1)

            shipName = input(f"\n{player}, Name your ship: ")
            p1Destid.append(shipName)

            str_correlate = f"({xLetter},{generateY})"
            p2Dest.append(str_correlate)
            print(str_correlate)

            if orientation == 1:

                Ysubstitute = generateY - 1
                #vertical

                if generateX == 0:

                    board[generateX][Ysubstitute] = "1#"
                    board[generateX + 1][Ysubstitute] = "2#"

                    xLetter3 = strConvertc(generateX + 1)
                    str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                    
                    printBoard(board)

                elif generateX == (gridSize - 1):

                    board[generateX][Ysubstitute] = "3#"
                    board[generateX - 1][Ysubstitute] = "4#"

                    xLetter3 = strConvertc(generateX - 1)
                    str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                    
                    printBoard(board)

                else:

                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][Ysubstitute] = "5#"
                        board[generateX - 1][Ysubstitute] = "6#"
                        
                        xLetter3 = strConvertc(generateX - 1)
                        str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][Ysubstitute] = "7#"
                        board[generateX + 1][Ysubstitute] = "8#"

                        xLetter3 = strConvertc(generateX + 1)
                        str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                        
                        printBoard(board)

            elif orientation == 0:

                #horiz
                Ysubstitute = generateY - 1

                if generateY == 1:

                    board[generateX][Ysubstitute] = "9#"
                    board[generateX][Ysubstitute + 1] = "0#"
                    str_correlate3 = f"({xLetter},{Ysubstitute + 2})"
                    
                    printBoard(board)

                elif generateY == (gridSize - 1):

                    board[generateX][Ysubstitute] = "A#"
                    board[generateX][Ysubstitute - 1] = "B#"
                    str_correlate3 = f"({xLetter},{Ysubstitute + 2})"
                    
                    printBoard(board)

                else:

                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][Ysubstitute] = "C#"
                        board[generateX][Ysubstitute + 1] = "D#"
                        str_correlate3 = f"({xLetter},{Ysubstitute + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #left
                        board[generateX][Ysubstitute] = "E#"
                        board[generateX][Ysubstitute - 1] = "F#"
                        str_correlate3 = f"({xLetter},{Ysubstitute + 1})"
                        
                        printBoard(board)

            p1Dest.append(str_correlate)
            p1Dest.append(str_correlate3)
            

        elif placementType == 0 and playType == 2:

            #Manual Placement
            printBoard(board)
            shipName = input(f"\n{player}, Name your ship: ")
            p1Destid.append(shipName)

            # Converts coordinates to indexes, Letter[0] & number[1]
            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]

            # Formats the coordinates & adds them to the destroyer list
            str_correlate = f"({xLetter},{yNumber})"
            p1Dest.append(str_correlate)
            newCol = strConvert(xLetter)

            board[newCol][int(yNumber) - 1] = "#"
            shipLoc2 = input("Enter the coordinates of a cell touching yours either vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = parkedShip2[1]
            str_correlate4 = f"({xLetter2},{yNumber})"
            p1Dest.append(str_correlate4)

            newCol = strConvert(xLetter2)
            board[newCol][int(yNumber2) -1] = "#"

        elif placementType == 0 and playType == 1:

            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            if orientation == 1:

                Ysubstitute = generateY - 1
                #vertical

                if generateX == 0:

                    board[generateX][Ysubstitute] = "1#"
                    board[generateX + 1][Ysubstitute] = "2#"

                    xLetter3 = strConvertc(generateX + 1)
                    str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                    
                    printBoard(board)

                elif generateX == (gridSize - 1):

                    board[generateX][Ysubstitute] = "3#"
                    board[generateX - 1][Ysubstitute] = "4#"

                    xLetter3 = strConvertc(generateX - 1)
                    str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                    
                    printBoard(board)

                else:

                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][Ysubstitute] = "5#"
                        board[generateX - 1][Ysubstitute] = "6#"
                        
                        xLetter3 = strConvertc(generateX - 1)
                        str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][Ysubstitute] = "7#"
                        board[generateX + 1][Ysubstitute] = "8#"

                        xLetter3 = strConvertc(generateX + 1)
                        str_correlate3 = f"({xLetter3},{Ysubstitute + 1})"
                        
                        printBoard(board)

            elif orientation == 0:

                #horiz
                Ysubstitute = generateY - 1

                if generateY == 1:

                    board[generateX][Ysubstitute] = "9#"
                    board[generateX][Ysubstitute + 1] = "0#"
                    str_correlate3 = f"({xLetter},{Ysubstitute +2})"
                    
                    printBoard(board)

                elif generateY == (gridSize - 1):

                    board[generateX][Ysubstitute] = "A#"
                    board[generateX][Ysubstitute - 1] = "B#"
                    str_correlate3 = f"({xLetter},{Ysubstitute - 2})"
                    
                    printBoard(board)

                else:

                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][Ysubstitute] = "C#"
                        board[generateX][Ysubstitute + 1] = "D#"
                        str_correlate3 = f"({xLetter},{Ysubstitute + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #left
                        board[generateX][Ysubstitute] = "E#"
                        board[generateX][Ysubstitute - 1] = "F#"

                        str_correlate3 = f"({xLetter},{Ysubstitute + 1})"
                        
                        printBoard(board)

            p1Dest.append(str_correlate)

# Creates a set of 3 (2 for now) points to represent the submarine, (medium sized ship) updates ship list based on arguments 

def createSub(gridSize, placementType):

    if player == "Player 1":

        if placementType == 1:

            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p2Dest.append(str_correlate)

        elif placementType == 0:

            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]
            str_correlate = f"({xLetter},{yNumber})"
            print(str_correlate)
            p2Dest.append(str_correlate)

    elif player == "Player 2":

        if placementType == 1:

            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            print(str_correlate)
            p1Dest.append(str_correlate)

        elif placementType == 0 and playType == 2:

            shipLoc = input("Input a coordinate to sail your ship: ")
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

def gameEnding(playerwin):

    if len(p1HitList) >= 5:

        gooping = False
        print("Your enemy managed to escape! You gotta be quicker next time! ")
        return gooping
    
    elif len(shipsSunk) == numShips:

        if playerwin == "Player 1":
            gooping = False
            print("You banished all your opponents! Your name will go down in history as a great seamen")
            print("Player 1 wins!! ")
            return gooping
        
        elif playerwin == "Player 2":

            gooping = False
            print("You banished all your opponents! Your name will go down in history as a great seamen")
            print("Player 2 wins!! ")
            return gooping
        
    else:

        gooping = True
        return gooping

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
    gameMode = int(input("\nInput 1 for singleplayer, 2 for co-op: "))
    return gameMode

def compTarget(board):

    bombX = random.randint(0,gridSize - 1)
    xLetter = strConvertc(bombX)
    bombY = random.randint(1,gridSize - 1)
    placeholdc = f"({xLetter},{bombY})"
    print(f"Computer Hit: {placeholdc}")

    if placehold in p2HitList or placehold in p2HitsHit:
        print("You've already hit this space! ")
        compTarget(board)

    if placeholdc not in p2Dest and placehold not in p2Sub and placehold not in p2Cruise and placehold not in p2Battle and placehold not in p2Air:

        board[bombX][bombY - 1] = "X"
        printBoard(board)
        p2HitList.append(placeholdc)
        missileLaunchO

    elif placeholdc in p2Dest or placehold in p2Sub or placehold in p2Cruise or placehold  in p2Battle or placehold  in p2Air:

        board[bombX][bombY - 1] = "X"
        printBoard(board)
        p2HitList.append(placeholdc)
        misslieLaunchS()

def listInt():
    if numShips == 1:
        if len(p1Dest) == 0:
            shipsSunk.append("X")
            print(f"You have sunk: {p1Destid[0]}")
            playerwin = "Player 1"
            return playerwin
        elif len(p2Dest) == 0:
            shipsSunk.append("X")
            print(f"You have sunk: {p2Destid[0]}")
            playerwin = "Player 2"
            return playerwin
    # elif numShips == 2:

    # elif numShips == 3:

    # elif numShips == 4:

    # elif numShips == 5:
    
def strConvertc(col):
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    newCol = keys[col]

    return newCol

gooping = True
placehold = None
playType = None
newCol = None
newColn = None
playerwin = None

p1Dest = []
p1Destid = []
p1Sub = []
p1Cruise = []
p1Battle = []
p1Air = []
p1Ship2 = []

p2Dest = []
p2Destid = []
p2Sub = []
p2Cruise = []
p2Battle = []
p2Air = []
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

numShips = int(input("\nHow many ships are you playing with? (Max 5): "))

placementType = int(input("\nInput 1 to automatically place ships or 0 to manually place ships: "))

player = "Player 1"
shipCreateS(numShips,  gridSize, player, board1TransferDef, newCol)

player = "Player 2"
shipCreateS(numShips,  gridSize, player, board2TransferDef, newCol)

def main(gooping):

    while gooping == True:

        if playType == 1:

            player = "Player 1"
            print(f"\nIt is {player}'s turn.\n")

            userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
            bombTarget(userBomb, board1TransferAtk, player)
            time.sleep(.7)
            aresenal()
            listInt()
            gooping = gameEnding(player)

            if gooping == False:
                break
            player = "Player 2"
            print(f"\nIt is {player}'s turn.\n")

            compTarget(board1TransferDef)
            listInt()
            gooping = gameEnding(player)

            if gooping == False:
                break
            
            continue

        elif playType == 2:

            player = "Player 1"
            print(f"\nIt is {player}'s turn.\n")

            userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
            bombTarget(userBomb, board1TransferAtk)
            time.sleep(.7)
            aresenal()
            listInt()
            gooping = gameEnding(player)

            player = "Player 2"
            print(f"\nIt is {player}'s turn.\n")

            userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
            bombTarget(userBomb, board1TransferAtk)
            time.sleep(.7)
            aresenal()
            listInt()
            gooping = gameEnding(player)
            continue
            
main(gooping)
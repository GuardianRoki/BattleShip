import random
import os
import time
from colorama import Fore, Back, Style

# Creates a board for the player or computer

def createBoard(gridSize):

    board = [['O'] * int(gridSize) for col in range(int(gridSize))]    

    return board

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

#Allows user and computer to shoot at eachothers ships ||| Doesn't work yet, shooting doesn't "hit"

def bombTarget(userBomb, board, player,shipID1, shipID2, destName, destName2, subName, subName2):
        
        if player == "Player 1":

            keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

            targetLoc = userBomb.split(",")
            xPos = targetLoc[0]
            yPos = int(targetLoc[1])
            placehold = f"({xPos},{yPos})"
        
            scoordlist = shipID2.get(destName2)
            sscoordlist = shipID2.get(subName2)
            print(sscoordlist)

            for i in range(0, len(keys)):

                if placehold not in scoordlist or sscoordlist:

                    if xPos == keys[i]:

                        board[i][yPos - 1] = Fore.CYAN + "X" + Fore.RESET
                        missileLaunchMiss()
                        printBoard(board)


                elif placehold in scoordlist:

                    if xPos == keys[i]:

                        board[i][yPos - 1] = Fore.RED + "~" + Fore.RESET
                        scoordlist.remove(placehold)
                        missileLaunchStrike()
                        printBoard(board)
                        print("You Hit!")
                        shipID2.update({destName2: scoordlist})
                
                elif placehold in sscoordlist:

                    if xPos == keys[i]:

                        board[i][yPos - 1] = Fore.RED + "~" + Fore.RESET
                        sscoordlist.remove(placehold)
                        missileLaunchStrike()
                        printBoard(board)
                        print("You Hit!")
                        shipID2.update({subName2: sscoordlist})
            
        elif player == "Player 2":

            keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

            bombX = random.randint(0, gridSize - 1)
            xLetter = strConvert(bombX)
            bombY = random.randint(0,gridSize - 1)
            placeholdc = f"({xLetter},{bombY})"

            scoordlist2 = shipID1.get(destName)
            sscoordlist2 = shipID1.get(subName)
            


            if placeholdc not in scoordlist2 or sscoordlist2:

                    for i in range(0, len(keys)):

                        if xLetter == keys[i]:

                            board[i][bombY] = Fore.CYAN + "X" + Fore.RESET
                            missileLaunchMiss()
                            printBoard(board)

            elif placeholdc in scoordlist2:

                    for i in range(0, len(keys)):

                        if xLetter == keys[i]:

                            board[i][bombY - 1] = Fore.RED + "~" + Fore.RESET
                            scoordlist2.remove(placeholdc)
                            missileLaunchStrike()
                            printBoard(board)
                            print("You Hit!")
                            shipID1.update({destName: scoordlist2})
                
            elif placeholdc in sscoordlist2:

                    if xLetter == keys[i]:

                        board[i][bombY - 1] = Fore.RED + "~" + Fore.RESET
                        sscoordlist2.remove(placehold)
                        missileLaunchStrike()
                        printBoard(board)
                        print("You Hit!")
                        shipID2.update({subName2: sscoordlist2})

#Creates ships

def createDest(gridSize, placementType, board, player, shipID1, shipID2):
        
    if placementType == 1:

        if player == "Player 1":
            
            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            destName = input("\nName your first ship: ")
            

            if orientation == 1:
            
            #vertical orientation & extremes

                if generateX == 0:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    
                    printBoard(board)

                else:
                    
                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    
                    printBoard(board)

                elif generateY == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    
                    printBoard(board)

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        printBoard(board)
                        
                    
            coordlist = [str_correlate,str_correlate2]
            shipID1.update({destName: coordlist})
            print(shipID1)
            return destName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            shipNameChoice = random.randint(0,5)
            destName2 = f"USS {shipNamePoss[shipNameChoice]}"

            if orientation == 1:
            
            #vertical orientation & extremes

                if generateX == 0:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"


                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    

                else:
                    
                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    

                elif generateY == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        
            coordlist2 = [str_correlate,str_correlate2]
            shipID2[destName2] = coordlist2
            return destName2
        
    elif placementType == 0:

        if player == "Player 1":

            #Manual Placement
            printBoard(board)
            destName = input("\nName your ship: ")

            # Converts coordinates to indexes, Letter[0] & number[1]
            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = int(parkedShip[1])

            # Formats the coordinates & adds them to the destroyer list
            str_correlate = f"({xLetter},{yNumber})"
            newCol = strConvert(xLetter)

            board[newCol][yNumber - 1] = Fore.GREEN + "#" + Fore.RESET
            shipLoc2 = input("Enter the coordinates of an adjacent cell vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = int(parkedShip2[1])
            str_correlate2 = f"({xLetter2},{yNumber})"

            newCol = strConvert(xLetter2)
            board[newCol][yNumber2 -1] = Fore.GREEN + "#" + Fore.RESET
            coordlist = [(str_correlate,str_correlate2)]
            shipID2[destName] = coordlist
            print(shipID1)
            return destName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            shipNameChoice = random.randint(0,5)
            destName2 = f"USS {shipNamePoss[shipNameChoice]}"

            if orientation == 1:
            
            #vertical orientation & extremes

                if generateX == 0:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"


                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    

                else:
                    
                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    

                elif generateY == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"

            coordlist2 = [(str_correlate,str_correlate2)]
            shipID2[destName2] = coordlist2
            return destName2

#Creates Subs

def createSub(gridSize, placementType, board, player, shipID1, shipID2):

    if placementType == 1:
        str_correlate3 = ""
        if player == "Player 1":

            orientation = random.randint(0,1)
            generateX2 = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX2)

            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            subName = input("\nName your second ship: ")


            if orientation == 1:

                #vertical orientation & extremes

                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                        print("\nYour second ship was auto-generated at the same location as the first one. Please Restart.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    printBoard(board)

                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET

                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

            elif orientation == 0:

                #horizontal extremes

                if generateY == 1:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"

                    printBoard(board)

                elif generateY == (gridSize - 1):

                    #bottom

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY - 2] == "#":

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"

                    printBoard(board)

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right

                        if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                            #left

                            if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                                print("\nYour second ship was auto-generated at the same location as the first one.\n")
                                createSub(gridSize, placementType, board, player, shipID1, shipID2)

                            board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                            board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET

                            xLetter2 = strConvert(generateX2)
                            str_correlate2 = f"({xLetter2},{generateY - 1})"
                            printBoard(board)
    

            coordlist = [str_correlate,str_correlate2]
            shipID1.update({subName: coordlist})
            print(shipID1)
            return subName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX2 = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX2)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            if orientation == 1:

                print(orientation)

                #vertical orientation & extremes
                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate3 = f"({xLetter2},{generateY})"


                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate3 = f"({xLetter2},{generateY})"


                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate3 = f"({xLetter2},{generateY})"

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate3 = f"({xLetter2},{generateY})"


            elif orientation == 0:

                #horizontal extremes

                if generateY == 1:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate3 = f"({xLetter2},{generateY + 1})"


                elif generateY == (gridSize - 1):

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY - 2] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate3 = f"({xLetter2},{generateY - 1})"


                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right

                        if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate3 = f"({xLetter2},{generateY + 1})"

                    elif toporbottom == 1:

                        #left

                        if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY - 2] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate3 = f"({xLetter2},{generateY - 1})"

            subName2 = "sub"
            coordlist2 = [str_correlate,str_correlate3]
            shipID2.update({subName2: coordlist2})
            return subName2

    elif placementType == 0:

        if player == "Player 1":

            #Manual Placement
            printBoard(board)
            subName = input("\nName your second ship: ")

            # Converts coordinates to indexes, Letter[0] & number[1]
            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = int(parkedShip[1])

            # Formats the coordinates & adds them to the ship list
            str_correlate = f"({xLetter},{yNumber})"
            newCol = reverseConvert(xLetter)

            if board[newCol][yNumber] == "#":

                print("\nYou are trying to place your second ship atop your first. Restart.\n")
                createSub(gridSize, placementType, board, player, shipID1, shipID2)

            board[newCol][yNumber - 1] = "#"
            shipLoc2 = input("Enter the coordinates of an adjacent cell vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = int(parkedShip2[1])
            str_correlate2 = f"({xLetter2},{yNumber})"

            newCol = reverseConvert(xLetter2)

            if board[newCol][yNumber2] == "#":

                print("\nYou are trying to place your second ship atop your first. Restart.\n")
                createSub(gridSize, placementType, board, player, shipID1, shipID2)


            board[newCol][yNumber2 -1] = "#"
            coordlist = [(str_correlate,str_correlate2)]
            shipID1.update({subName: coordlist})
            print(shipID1)
            return subName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX2 = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX2)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            if orientation == 1:

                #vertical orientation & extremes
                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] or board[generateX2 - 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] or board[generateX2 + 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"


            elif orientation == 0:

                #horizontal extremes

                if generateY == 1:

                    if board[generateX2][generateY - 1] or board[generateX2][generateY] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"


                elif generateY == (gridSize - 1):

                    if board[generateX2][generateY - 1] or board[generateX2][generateY - 2] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:    

                        #right

                        if board[generateX2][generateY - 1] or board[generateX2][generateY] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"

                    elif toporbottom == 1:

                        #left

                        if board[generateX2][generateY - 1] or board[generateX2][generateY - 2] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"

            shipNameChoice = random.randint(0,5)
            subName2 = subName2 = f"USS {subNamePoss[shipNameChoice]}"
            coordlist2 = [str_correlate,str_correlate2]
            shipID2.update({subName2: coordlist2})
            return subName2

# Animations for a hit on a ship

def missileLaunchStrike():
        
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

# Animations for a miss 

def missileLaunchMiss():

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

# Converts a number to a letter

def strConvert(col):
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    newCol = keys[col]

    return newCol

#Checks for wins

def wincond(gooping, shipID1, shipID2, destName, destName2, subName, subName2):
    p1DestSunk = shipID2.get(destName2)
    p1SubSunk = shipID2.get(subName2)
    p2DestSunk = shipID1.get(destName)
    p2SubSunk = shipID1.get(subName)

    if len(p1DestSunk) == 0:
        print(f"{destName2} is sunk! ")
    if len(p1SubSunk) == 0:
        print(f"{subName2} is sunk!")
    if len(p2DestSunk) == 0:
        print(f"{destName} is sunk! ")
    if len(p2SubSunk) == 0:
        print(f"{subName} is sunk! ")
    

    if len(p1DestSunk) == 0 and len(p1SubSunk) == 0:
        gooping = False
        print("Player One Wins!")
    elif len(p2DestSunk) == 0 and len(p2SubSunk) == 0:
        gooping = False
        print("Player Two Wins!")
    return gooping

def reverseConvert(col):

    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    newCol = keys.index(col)

    return newCol

gooping = True

shipID1 = {}

shipID2 = {}

coordlist = []

shipNamePoss = ["Glizzy Gang", "Chud Man", "Big Chungus", "Sussy Sigma", "Sleepy Joe", "Skibidi Slicer"]

subNamePoss = ["Lebonbon", "Boe Jiden", "Tonald Drump", "Fortiniteylababag", "marccantcode", "I hate ben"]

destName = ""

destName2 = ""

subName = ""

subName2 = ""


player = "Player 1"

# Basic standard welcome info 

print("\nWelcome to BattleShip!\n")
print("In BattleShip, two players engage in a turn-based battle, competing to sink all of the opponent's ships before they lose all of their own.\n")
print("Player 1 will start first. If an opposing ship is hit, your turn will continue. Otherwise, player 2's turn will begin.\n")

print("Ships that are " + Fore.BLUE + "sailing" + Fore.RESET + " will be " + Fore.GREEN + "Green" + Fore.RESET + " and ships that have been " + Fore.YELLOW + "sunk " + Fore.RESET + "are "+ Fore.RED + "Red.\n" + Fore.RESET)
  
gridSize = 10 # int(input("\nEnter your grid size (# input)[26 Max]: "))


# First Board for player 1, shows ships & enemy attack coordinates
board = createBoard(gridSize)

# Board for computer's info
grid = createBoard(gridSize)


numShips = 1 # int(input("\nHow many ships are you playing with? (Max 5): "))

placementType = int(input("\nInput 1 to automatically place ships or 0 to manually place ships: "))

if placementType < 0 or placementType > 1:
    while placementType < 0 or placementType > 1:
        placementType = int(input("\nInvalid input. 1 - Automatic | 0 - Manual Placement: "))

player = "Player 1"
destName = createDest(gridSize, placementType, board, player, shipID1, shipID2)
subName =createSub(gridSize, placementType, board, player, shipID1, shipID2)

# createSub(gridSize, placementType, board, player)

player = "Player 2"
destName2 = createDest(gridSize, placementType, grid, player, shipID1, shipID2)
subName2 = createSub(gridSize, placementType, grid, player, shipID1, shipID2)


while(gooping):

    player = "Player 1"
    print(f"\nIt is {player}'s turn.\n")

    userBomb = input(f"\n{player}, Please select a section to hit with your artillery: ")
    bombTarget(userBomb, board, player,shipID1, shipID2, destName, destName2, subName, subName2)
    gooping = wincond(gooping, shipID1, shipID2, destName, destName2, subName, subName2)

    if gooping == False:
        break

    # Sets player to computer

    player = "Player 2"
    print(f"\nIt is the computer's turn.\n")

    bombTarget(userBomb, grid, player,shipID1, shipID2, destName, destName2, subName, subName2)
    gooping = wincond(gooping ,shipID1, shipID2, destName, destName2, subName, subName2)
    
    if gooping == False:
        break
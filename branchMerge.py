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

#Allows user and computer to shoot at eachothers ships

# Receives input from the player to target a location on the board

def bombTarget(userBomb, board, player, shipID2, destName, destName2, subName):
    
    if player == "Player 1":
        
        for x in range(0, gridSize):
            for i in range(1, gridSize + 1):

                xLetter = strConvert(x)
                if f"{xLetter},{str(i)}" == userBomb:
                    print("You have already hit this space!")
                    userBomb = input("Select a coordinate to strike with your artillery: ")
                    bombTarget(userBomb, board, player, shipID2, destName, destName2, subName)

        keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        targetLoc = userBomb.split(",")
        xPos = targetLoc[0]
        yPos = int(targetLoc[1])
        placehold = f"({xPos},{yPos})"
        print(placehold)
        print(destName)
        print(shipID2)
      
        scoordlist = shipID2.get(destName2)
        print(type(scoordlist))
        print("skibidi")
        # print(type(scoordlist))
        # print(type(placehold))
        # print(scoordlist)

        scoordlist = shipID2.get(destName2)
        print("nah")
        
        for i in range(0, len(keys)):

            if placehold not in scoordlist:

                if xPos == keys[i]:

                    board[i][yPos - 1] = "X"
                    print("Sigma")
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
                    
        print(shipID2)
        
    # elif player == "Player 2":
        # bombX = random.randint(0, gridSize - 1)
        # xLetter = strConvert(bombX)
        # bombY = random.randint(0,gridSize - 1)
        # placeholdc = f"({xLetter},{bombY})"


        # keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#         for x in range(0, gridSize):
#             for i in range(0, gridSize):

#                 xLetter = strConvert(x)
#                 if f"({xLetter},{i})" == placeholdc:
#                     player = "Player 2"
#                     bombTarget(userBomb, board, player, shipID2, destName, destName2, subName)

        # if placeholdc not in coordlist2:

        #         for i in range(0, len(keys)):

        #             if xLetter == keys[i]:

        #                 board[i][bombY] = "X"
        #                 p2MovesList.append(placeholdc)
        #                 missileLaunchMiss()
        #                 printBoard(board)

        # elif placeholdc in coordlist2:

        #         for i in range(0, len(keys)):

        #             if xLetter == keys[i]:

        #                 board[i][bombY - 1] = Fore.RED + "~" + Fore.RESET
        #                 coordlist2.remove(placeholdc)
        #                 missileLaunchStrike()
        #                 printBoard(board)
        #                 print("You Hit!")



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

                        board[generateX][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "2#" + Fore.RESET
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "4#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    
                    printBoard(board)

                else:
                    
                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "6#" + Fore.RESET

                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "8#" + Fore.RESET 
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    board[generateX][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "2#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    
                    printBoard(board)

                elif generateY == (gridSize - 1):

                            #bottom

                    board[generateX][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX][generateY - 2] = Fore.GREEN + "4#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    
                    printBoard(board)

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "6#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "8#" + Fore.RESET

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

                    board[generateX][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "2#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "4#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "6#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "8#" + Fore.RESET
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"

                        printBoard(board)

        elif orientation == 0:

          #horizontal extremes

            if generateY == 1:


                board[generateX][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                board[generateX][generateY] = Fore.GREEN + "2#" + Fore.RESET
                xLetter2 = strConvert(generateX)
                str_correlate2 = f"({xLetter2},{generateY + 1})"

                printBoard(board)

            elif generateY == (gridSize - 1):

                board[generateX][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                board[generateX][generateY - 2] = Fore.GREEN + "4#" + Fore.RESET
                xLetter2 = strConvert(generateX)
                str_correlate2 = f"({xLetter2},{generateY - 1})"
                
                printBoard(board)

            else:

                # centered horizontal
                toporbottom = random.randint(0,1)

                if toporbottom == 0:

                    #right
                    board[generateX][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "6#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    printBoard(board)

                elif toporbottom == 1:

                    #left
                    board[generateX][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                    board[generateX][generateY - 2] =Fore.GREEN + "8#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    printBoard(board)

            coordlist2 = [str_correlate,str_correlate2]
            shipID2[destName2] = coordlist2
            print(shipID2)
            return destName2
          
    elif placementType == 0:
      
        if player == "Player 1":
          
            #Manual Placement
            printBoard(board)
            destName = input("\nName your first ship: ")

            # Converts coordinates to indexes, Letter[0] & number[1]
            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = parkedShip[1]

            # Formats the coordinates & adds them to the destroyer list
            str_correlate = f"({xLetter},{yNumber})"
            newCol = strConvert(xLetter)

            board[newCol][int(yNumber) - 1] = "#"
            shipLoc2 = input("Enter the coordinates of an adjacent cell vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = parkedShip2[1]
            str_correlate2 = f"({xLetter2},{yNumber})"

            newCol = strConvert(xLetter2)
            board[newCol][int(yNumber2) -1] = "#"
            coordlist = [(str_correlate,str_correlate2)]
            shipID2[destName2] = coordlist
            print(shipID2)
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

                    board[generateX][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "2#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "4#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "6#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = "7#"
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "8#" + Fore.RESET
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"

                        printBoard(board)

              elif orientation == 0:

                #horizontal extremes

                if generateY == 1:


                    board[generateX][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "2#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"

                    printBoard(board)

                elif generateY == (gridSize - 1):

                        board[generateX][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "4#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        
                        printBoard(board)

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "6#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] =Fore.GREEN + "7#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "8#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        printBoard(board)
                coordlist2 = [str_correlate,str_correlate2]
                shipID2[destName2] = coordlist2
                print(shipID2)
                return destName2
              

def createSub(gridSize, placementType, board, player, shipID1, shipID2):
        
    if placementType == 1:

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

                        board[generateX2][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "2#" + Fore.RESET
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "4#" + Fore.RESET
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

                        board[generateX2][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "6#" + Fore.RESET

                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "8#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "2#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    
                    printBoard(board)

                elif generateY == (gridSize - 1):

                    #bottom

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY - 2] == "#":

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "4#" + Fore.RESET
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

                        board[generateX2][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX2][generateY] = Fore.GREEN + "6#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                        printBoard(board)

                    elif toporbottom == 1:

                        #left

                        if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                        board[generateX2][generateY - 2] = Fore.GREEN + "8#" + Fore.RESET

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

              shipNameChoice = random.randint(0,5)
              subName2 = f"USS {shipNamePoss[shipNameChoice]}"

              if orientation == 1:

                #vertical orientation & extremes
                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "2#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "4#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "6#" + Fore.RESET
                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "8#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"

                        printBoard(board)

        elif orientation == 0:

          #horizontal extremes

            if generateY == 1:

                if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                    createSub(gridSize, placementType, board, player, shipID1, shipID2)

                board[generateX2][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                board[generateX2][generateY] = Fore.GREEN + "2#" + Fore.RESET
                xLetter2 = strConvert(generateX2)
                str_correlate2 = f"({xLetter2},{generateY + 1})"

                printBoard(board)

            elif generateY == (gridSize - 1):

                if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY - 2] == "#":

                    createSub(gridSize, placementType, board, player, shipID1, shipID2)

                board[generateX2][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                board[generateX2][generateY - 2] = Fore.GREEN + "4#" + Fore.RESET
                xLetter2 = strConvert(generateX2)
                str_correlate2 = f"({xLetter2},{generateY - 1})"
                
                printBoard(board)

            else:

                # centered horizontal
                toporbottom = random.randint(0,1)

                if toporbottom == 0:

                    #right

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "6#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    printBoard(board)

                elif toporbottom == 1:

                    #left

                    if board[generateX2][generateY - 1] == "#" or board[generateX2][generateY - 2] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "8#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    printBoard(board)

            coordlist2 = [str_correlate,str_correlate2]
            shipID2[subName2] = coordlist2
            print(shipID2)
            return subName2
          
    elif placementType == 0:
      
        if player == "Player 1":
          
            #Manual Placement
            printBoard(board)
            destName = input("\nName your second ship: ")

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
            shipID2[subName2] = coordlist
            print(shipID2)
            return destName

        elif player == "Player 2":

              orientation = random.randint(0,1)
              generateX2 = random.randint(0,gridSize - 1)
              xLetter = strConvert(generateX2)
              generateY = random.randint(1,gridSize - 1)
              str_correlate = f"({xLetter},{generateY})"

              shipNameChoice = random.randint(0,5)
              subName2 = f"USS {shipNamePoss[shipNameChoice]}"

              if orientation == 1:

                #vertical orientation & extremes
                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 + 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "2#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == "#" or board[generateX2 - 1][generateY - 1] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "4#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                    printBoard(board)

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] or board[generateX2 - 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "6#" + Fore.RESET
                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        printBoard(board)

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] or board[generateX2 + 1][generateY - 1] == "#":

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "8#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"

                        printBoard(board)

        elif orientation == 0:

          #horizontal extremes

            if generateY == 1:

                if board[generateX2][generateY - 1] or board[generateX2][generateY] == "#":

                    createSub(gridSize, placementType, board, player, shipID1, shipID2)

                board[generateX2][generateY - 1] = Fore.GREEN + "1#" + Fore.RESET
                board[generateX2][generateY] = Fore.GREEN + "2#" + Fore.RESET
                xLetter2 = strConvert(generateX2)
                str_correlate2 = f"({xLetter2},{generateY + 1})"

                printBoard(board)

            elif generateY == (gridSize - 1):

                if board[generateX2][generateY - 1] or board[generateX2][generateY - 2] == "#":

                    createSub(gridSize, placementType, board, player, shipID1, shipID2)

                board[generateX2][generateY - 1] = Fore.GREEN + "3#" + Fore.RESET
                board[generateX2][generateY - 2] = Fore.GREEN + "4#" + Fore.RESET
                xLetter2 = strConvert(generateX2)
                str_correlate2 = f"({xLetter2},{generateY - 1})"
                
                printBoard(board)

            else:

                # centered horizontal
                toporbottom = random.randint(0,1)

                if toporbottom == 0:

                    #right

                    if board[generateX2][generateY - 1] or board[generateX2][generateY] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "5#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "6#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    printBoard(board)

                elif toporbottom == 1:

                    #left

                    if board[generateX2][generateY - 1] or board[generateX2][generateY - 2] == "#":

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "7#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "8#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    printBoard(board)

            coordlist2 = [str_correlate,str_correlate2]
            shipID2[subName2] = coordlist2
            print(shipID2)
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

def reverseConvert(col):

    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    newCol = keys.index(col)

    return newCol



gooping = True



shipID1 = {}

shipID2 = {}

coordlist = []

shipNamePoss = ["Glizzy Gang", "Chud Man", "Big Chungus", "Sussy Sigma", "Sleepy Joe", "Skibidi Slicer"]

destName = ""

destName2 = ""

subName = ""

subName2 = ""

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

placementType = int(input("\nInput 1 to automatically place ships or 0 to manually place ships: "))

# Main function, runs core code

# Creating Ships:

player = "Player 1"
destName = createDest(gridSize, placementType, board, player, shipID1, shipID2)
subName = createSub(gridSize, placementType, board, player, shipID1, shipID2)

# createSub(gridSize, placementType, board, player)

player = "Player 2"
destName2 = createDest(gridSize, placementType, grid, player, shipID1, shipID2)
subName2 = createSub(gridSize, placementType, grid, player, shipID1, shipID2)

# While loop to maintain runtime, main function w/ core code

while gooping == True:
  
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    player = "Player 1"
    print(f"\nIt is {player}'s turn.\n")
    try:

        userBomb = input(f"\n{player}, Select a coordinate to strike with your artillery (Y,X): ")
        synCheck = userBomb.split(",")
        xCheck = synCheck[0]
        yCheck = synCheck[1]

        if xCheck not in keys or yCheck in keys or int(yCheck) > gridSize - 1 or int(yCheck) < 1:
            print(Fore.RED + "\nInvalid input. Enter a valid coordinate." + Fore.RESET)
            break

        # bombTarget(userBomb, board, player, shipID2, destName, destName2, subName)
        print("Obv bomb target issue")
        print(shipID2)

        # These are for animations & Don't affect functionality
        # time.sleep(.7)
        # arsenal()
        # listInt()

        # Win check
        # gooping = gameEnding(player)

        # if gooping == False:
        #     break

        # Sets player to computer

        # player = "Player 2"
        # print(f"\nIt is the computer's turn.\n")

        # bombTarget(userBomb, grid, player, shipID2, p1MovesList, p2MovesList, destName, destName2, subName)
        # listInt()

        # Win check
        # gooping = gameEnding(player)

        # if gooping == False:
        #     break

    except TypeError:
        pass
    except ValueError:
        pass
    
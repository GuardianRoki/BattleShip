import random

def bombTarget(userBomb, board):
  
    if userBomb in p1ShipInfo or userBomb in p2ShipInfo:
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
            printBoard(board)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "B" or yPos == "b":

            board[1][int(xPos)- 1] = "X"
            printBoard(board)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "C" or yPos == "c":

            board[2][int(xPos)- 1] = "X"
            printBoard(board)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "D" or yPos == "d":

            board[3][int(xPos)- 1] = "X"
            printBoard(board)
            p1HitList.append(userBomb)
            missileLaunchO()

        if yPos == "E" or yPos == "e":

            board[4][int(xPos)- 1] = "X"
            printBoard(board)
            p1HitList.append(userBomb)
            missileLaunchO()


    elif placehold in p1Dest or placehold in p1Sub or placehold in p1Cruise or placehold  in p1Battle or placehold  in p1Air:

        if yPos == "A" or yPos == "a":

            board[0][int(xPos) - 1] = Fore.RED + "~" + Fore.RESET
            printBoard(board)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "B" or yPos == "b":

            board[1][int(xPos)- 1] = "~"
            printBoard(board)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "C" or yPos == "c":

            board[2][int(xPos)- 1] = "~"
            printBoard(board)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "D" or yPos == "d":

            board[3][int(xPos)- 1] = "~"
            printBoard(board)
            p1HitsHit.append(userBomb) 
            misslieLaunchS()
            print("You Hit!")
            

        if yPos == "E" or yPos == "e":

            board[4][int(xPos)- 1] = "~"
            printBoard(board)
            p1HitsHit.append(userBomb)
            misslieLaunchS()
            print("You Hit!")
            



        return targetLoc and board

def shipCreateS(numShips,  gridSize, player, board):

    if numShips == 1:

        createDest(player, gridSize, placementType)
        printBoard(board)

    if numShips == 2:

        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        printBoard(board)

    if numShips == 3:
        
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        printBoard(board)

    if numShips == 4:
        
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        createBattle(player, gridSize , placementType)
        printBoard(board)
    
    if numShips == 5:
    
        createDest(player, gridSize, placementType)
        createSub(player, gridSize, placementType)
        createCruise(player, gridSize, placementType)
        createBattle(player, gridSize, placementType)
        createAirC(player, gridSize, placementType)
        printBoard(board)


# P2's Ships will be added to p2ShipInfo, p1's attack coordinates will check p2's list & vice versa.


def createDest(gridSize, placementType, board, player, p1ShipInfo, p2ShipInfo):
        
        if placementType == 1:

            if player == "Player 1":
                
                orientation = random.randint(0,1)
                generateX = random.randint(0,gridSize - 1)
                xLetter = strConvert(generateX)
                generateY = random.randint(1,gridSize - 1)
                str_correlate = f"({xLetter},{generateY})"
                p1ShipInfo.append(str_correlate)

                if orientation == 1:
                
                #vertical orientation & extremes

                    if generateX == 0:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX + 1][generateY - 1] = "2#"
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        p1ShipInfo.append(str_correlate2)

                    elif generateX == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX - 1][generateY - 1] = "4#"
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        p1ShipInfo.append(str_correlate2)

                    else:
                        
                        # centered vertical
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #top
                            board[generateX][generateY - 1] = "5#"
                            board[generateX - 1][generateY - 1] = "6#"
                            xLetter2 = strConvert(generateX - 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            p1ShipInfo.append(str_correlate2)

                        elif toporbottom == 1:

                            #bottom
                            board[generateX][generateY - 1] = "7#"
                            board[generateX + 1][generateY - 1] = "8#" 
                            xLetter2 = strConvert(generateX + 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            p1ShipInfo.append(str_correlate2)

                elif orientation == 0:

                #horizontal extremes
            
                    if generateY == 1:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX][generateY] = "2#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        p1ShipInfo.append(str_correlate2)

                    elif generateY == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX][generateY - 2] = "4#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        p1ShipInfo.append(str_correlate2)

                    else:

                        # centered horizontal
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #right
                            board[generateX][generateY + 1] = "5#"
                            board[generateX][generateY + 2] = "6#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY + 1})"
                            p1ShipInfo.append(str_correlate2)

                        elif toporbottom == 1:

                            #left
                            board[generateX][generateY - 1] = "7#"
                            board[generateX][generateY - 2] = "8#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY - 1})"
                            p1ShipInfo.append(str_correlate2)

            elif player == "Player 2":

                orientation = random.randint(0,1)
                generateX = random.randint(0,gridSize - 1)
                xLetter = strConvert(generateX)
                generateY = random.randint(1,gridSize - 1)
                str_correlate = f"({xLetter},{generateY})"
                p2ShipInfo.append(str_correlate)

                if orientation == 1:
                
                #vertical orientation & extremes

                    if generateX == 0:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX + 1][generateY - 1] = "2#"
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        p2ShipInfo.append(str_correlate2)

                    elif generateX == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX - 1][generateY - 1] = "4#"
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        p2ShipInfo.append(str_correlate2)

                    else:
                        
                        # centered vertical
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #top
                            board[generateX][generateY - 1] = "5#"
                            board[generateX - 1][generateY - 1] = "6#"
                            xLetter2 = strConvert(generateX - 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            p2ShipInfo.append(str_correlate2)

                        elif toporbottom == 1:

                            #bottom
                            board[generateX][generateY - 1] = "7#"
                            board[generateX + 1][generateY - 1] = "8#" 
                            xLetter2 = strConvert(generateX + 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            p2ShipInfo.append(str_correlate2)

                elif orientation == 0:

                #horizontal extremes
            
                    if generateY == 1:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX][generateY] = "2#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        p2ShipInfo.append(str_correlate2)

                    elif generateY == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX][generateY - 2] = "4#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        p2ShipInfo.append(str_correlate2)

                    else:

                        # centered horizontal
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #right
                            board[generateX][generateY + 1] = "5#"
                            board[generateX][generateY + 2] = "6#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY + 1})"
                            p2ShipInfo.append(str_correlate2)

                        elif toporbottom == 1:

                            #left
                            board[generateX][generateY - 1] = "7#"
                            board[generateX][generateY - 2] = "8#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY - 1})"
                            p2ShipInfo.append(str_correlate2)

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
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    newCol = keys[col]

    return newCol

def compTarget(board):
    bombX = random.randint(0,gridSize - 1)
    xLetter = strConvert(bombX)
    bombY = random.randint(0,gridSize - 1)
    placeholdc = f"({xLetter},{bombY})"
    if placehold in p2HitList or placehold in p2HitsHit:
        print("You've already hit this space! ")
        compTarget(board)
    if placeholdc not in p2Dest and placehold not in p2Sub and placehold not in p2Cruise and placehold not in p2Battle and placehold not in p2Air:

            if xLetter == "A" or xLetter == "a":

                board[0][int(bombY) - 1] = "X"
                printBoard(board)
                p2HitList.append(userBomb)
                missileLaunchO()

            if xLetter == "B" or xLetter == "b":

                board[1][int(bombY)- 1] = "X"
                printBoard(board)
                p2HitList.append(userBomb)
                missileLaunchO()

            if xLetter == "C" or xLetter == "c":

                board[2][int(bombY)- 1] = "X"
                printBoard(board)
                p2HitList.append(userBomb)
                missileLaunchO()

            if xLetter == "D" or xLetter == "d":

                board[3][int(bombY)- 1] = "X"
                printBoard(board)
                p2HitList.append(userBomb)
                missileLaunchO()

            if xLetter == "E" or xLetter == "e":

                board[4][int(bombY)- 1] = "X"
                printBoard(board)
                p2HitList.append(userBomb)
                missileLaunchO()

    elif placeholdc in p2Dest or placehold in p2Sub or placehold in p2Cruise or placehold  in p2Battle or placehold  in p2Air:

            if xLetter == "A" or xLetter == "a":

                board[0][int(bombY) - 1] = Fore.RED + "~" + Fore.RESET
                printBoard(board)
                p2HitsHit.append(userBomb)
                misslieLaunchS()
                print("You Hit!")
                

            if xLetter == "B" or xLetter == "b":

                board[1][int(bombY)- 1] = "~"
                printBoard(board)
                p2HitsHit.append(userBomb)
                misslieLaunchS()
                print("You Hit!")
                

            if xLetter == "C" or xLetter == "c":

                board[2][int(bombY)- 1] = "~"
                printBoard(board)
                p2HitsHit.append(userBomb)
                misslieLaunchS()
                print("You Hit!")
                

            if xLetter == "D" or xLetter == "d":

                board[3][int(bombY)- 1] = "~"
                printBoard(board)
                p2HitsHit.append(userBomb) 
                misslieLaunchS()
                print("You Hit!")
                

            if xLetter == "E" or xLetter == "e":

                board[4][int(bombY)- 1] = "~"
                printBoard(board)
                p2HitsHit.append(userBomb)
                misslieLaunchS()
                print("You Hit!")




gridSize = 5

numShips = int(input("How many ships would you like to have? (Max 5): "))

placementType = int(input("Type 1 to automatically place ships or 0 to manually place ships: "))

player = "Player 1"
# shipCreateS(numShips, gridSize, player, board)

player = "Player 2"
#mshipCreateS(numShips,  gridSize, player, grid)


player = "Player 1"
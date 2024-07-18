import random

def compTarget(board, p1ShipInfo, compMoveList):

    bombX = random.randint(0, gridSize - 1)
    xLetter = strConvert(bombX)
    bombY = random.randint(0,gridSize - 1)

    placeholdc = f"({xLetter},{bombY})"

    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    if placeholdc in compMoveList:

        compTarget(board, p1ShipInfo, compMoveList)

    if placeholdc not in p1ShipInfo:

            for i in range(0, len(keys)):

                if xLetter == keys[i]:

                    board[i][bombY] = "X"
                    compMoveList.append(placeholdc)
                    missileLaunchMiss()
                    printBoard(board)

    elif placeholdc in p1ShipInfo:

            for i in range(0, len(keys)):

                if xLetter == keys[i]:

                    board[0][bombY - 1] = Fore.RED + "~" + Fore.RESET
                    compMoveList.append(placeholdc)
                    p1ShipInfo.remove(placeholdc)
                    missileLaunchStrike()
                    printBoard(board)
                    print("You Hit!")
                    
                

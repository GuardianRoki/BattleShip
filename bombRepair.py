

def bombTarget(userBomb, board, p2ShipInfo, p1MovesList):
  
    if userBomb in p1MovesList:

        print("You've already hit this space! ")
        userBomb = input("Select a coordinate to strike with your artilery: ")
        bombTarget(userBomb, board, p2ShipInfo, p1MovesList)

    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    targetLoc = userBomb.split(",")
    xPos = targetLoc[0]
    yPos = int(targetLoc[1])
    placehold = f"({xPos},{yPos})"


    for i in range(0, len(keys)):


        if placehold not in p2ShipInfo:

            if xPos == keys[i]:

                board[i][yPos - 1] = "X"
                p1ShipInfo.append(placehold)
                # missileLaunchMiss()
                # printBoard(board)


        elif placehold in p2ShipInfo:

            if xPos == keys[i]:

                board[i][yPos - 1] = Fore.RED + "~" + Fore.RESET
                p2ShipInfo.remove(placehold)
                # missileLaunchStrike()
                # printBoard(board)
                print("You Hit!")
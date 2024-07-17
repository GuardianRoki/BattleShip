import random

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

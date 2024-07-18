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


def bombTarget(userBomb, board, player, shipID2, p1MovesList, p2MovesList, DestName, DestName2, SubName):
    if player == "player 1":
        if userBomb in p1MovesList:


            print("You've already hit this space! ")
            userBomb = input("Select a coordinate to strike with your artilery: ")
            bombTarget(userBomb, board, shipID2, p1MovesList)

        keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        targetLoc = userBomb.split(",")
        xPos = targetLoc[0]
        yPos = int(targetLoc[1])
        placehold = f"({xPos},{yPos})"

        scoordlist = shipID2.get(DestName2)
        


        
        # coordlist2 = shipID2.get(DestName2)

        for i in range(0, len(keys)):


            if placehold not in scoordlist:

                if xPos == keys[i]:

                    board[i][yPos - 1] = "X"
                    print("Sigma")
                    p1MovesList.append(placehold)
                    missileLaunchMiss()
                    printBoard(board)


            elif placehold in scoordlist:

                if xPos == keys[i]:

                    board[i][yPos - 1] = Fore.RED + "~" + Fore.RESET
                    scoordlist.remove(placehold)
                    missileLaunchStrike()
                    printBoard(board)
                    print("You Hit!")
                    shipID2.update({DestName2: scoordlist})
        print(shipID2)
    elif player == "Player 2":
        bombX = random.randint(0, gridSize - 1)
        xLetter = strConvert(bombX)
        bombY = random.randint(0,gridSize - 1)
        placeholdc = f"({xLetter},{bombY})"

        keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        if placeholdc in p2MovesList:

            bombTarget(userBomb, board, player, shipID2, p1MovesList, p2MovesList, DestName, SubName)

        if placeholdc not in coordlist2:

                for i in range(0, len(keys)):

                    if xLetter == keys[i]:

                        board[i][bombY] = "X"
                        p2MovesList.append(placeholdc)
                        missileLaunchMiss()
                        printBoard(board)

        elif placeholdc in coordlist2:

                for i in range(0, len(keys)):

                    if xLetter == keys[i]:

                        board[i][bombY - 1] = Fore.RED + "~" + Fore.RESET
                        p2MoveList.append(placeholdc)
                        coordlist2.remove(placeholdc)
                        missileLaunchStrike()
                        printBoard(board)
                        print("You Hit!")

def createDest(gridSize, placementType, board, player):
        
        if placementType == 1:

            if player == "Player 1":
                
                orientation = random.randint(0,1)
                generateX = random.randint(0,gridSize - 1)
                xLetter = strConvert(generateX)
                generateY = random.randint(1,gridSize - 1)
                str_correlate = f"({xLetter},{generateY})"
                destName = input("What would you like to name your ship? ")
                

                if orientation == 1:
                
                #vertical orientation & extremes

                    if generateX == 0:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX + 1][generateY - 1] = "2#"
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        printBoard(board)

                    elif generateX == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX - 1][generateY - 1] = "4#"
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

                    else:
                        
                        # centered vertical
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #top
                            board[generateX][generateY - 1] = "5#"
                            board[generateX - 1][generateY - 1] = "6#"
                            xLetter2 = strConvert(generateX - 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            
                            printBoard(board)

                        elif toporbottom == 1:

                            #bottom
                            board[generateX][generateY - 1] = "7#"
                            board[generateX + 1][generateY - 1] = "8#" 
                            xLetter2 = strConvert(generateX + 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            
                            printBoard(board)

                elif orientation == 0:

                #horizontal extremes
            
                    if generateY == 1:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX][generateY] = "2#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                        printBoard(board)

                    elif generateY == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX][generateY - 2] = "4#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        
                        printBoard(board)

                    else:

                        # centered horizontal
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #right
                            board[generateX][generateY - 1] = "5#"
                            board[generateX][generateY] = "6#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY + 1})"
                            
                            printBoard(board)

                        elif toporbottom == 1:

                            #left
                            board[generateX][generateY - 1] = "7#"
                            board[generateX][generateY - 2] = "8#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY - 1})"
                            
                            printBoard(board)
                coordlist = [(str_correlate,str_correlate2)]
                shipID1[destName] = coordlist
                print(shipID1)

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

                        board[generateX][generateY - 1] = "1#"
                        board[generateX + 1][generateY - 1] = "2#"
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"

                        printBoard(board)

                    elif generateX == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX - 1][generateY - 1] = "4#"
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

                    else:
                        
                        # centered vertical
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #top
                            board[generateX][generateY - 1] = "5#"
                            board[generateX - 1][generateY - 1] = "6#"
                            xLetter2 = strConvert(generateX - 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            
                            printBoard(board)

                        elif toporbottom == 1:

                            #bottom
                            board[generateX][generateY - 1] = "7#"
                            board[generateX + 1][generateY - 1] = "8#" 
                            xLetter2 = strConvert(generateX + 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            
                            printBoard(board)

                elif orientation == 0:

                #horizontal extremes
            
                    if generateY == 1:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX][generateY] = "2#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                        printBoard(board)

                    elif generateY == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX][generateY - 2] = "4#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        
                        printBoard(board)

                    else:

                        # centered horizontal
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #right
                            board[generateX][generateY + 1] = "5#"
                            board[generateX][generateY + 2] = "6#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY + 1})"
                            
                            printBoard(board)

                        elif toporbottom == 1:

                            #left
                            board[generateX][generateY - 1] = "7#"
                            board[generateX][generateY - 2] = "8#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY - 1})"
                            printBoard(board)
                coordlist2 = [(str_correlate,str_correlate2)]
                shipID2[destName2] = coordlist2
                print(shipID2)
        elif placementType == 0:
            if player == "Player 1":
                #Manual Placement
                printBoard(board)
                destName = input("What would you like to name your ship")

                # Converts coordinates to indexes, Letter[0] & number[1]
                shipLoc = input("Input a coordinate to sail your ship: ")
                parkedShip = shipLoc.split(",")
                xLetter = parkedShip[0]
                yNumber = parkedShip[1]

                # Formats the coordinates & adds them to the destroyer list
                str_correlate = f"({xLetter},{yNumber})"
                newCol = strConvert(xLetter)

                board[newCol][int(yNumber) - 1] = "#"
                shipLoc2 = input("Enter the coordinates of a cell touching yours either vertically or horizontally: ")
                parkedShip2 = shipLoc2.split(",")
                xLetter2 = parkedShip2[0]
                yNumber2 = parkedShip2[1]
                str_correlate2 = f"({xLetter2},{yNumber})"

                newCol = strConvert(xLetter2)
                board[newCol][int(yNumber2) -1] = "#"
                coordlist = [(str_correlate,str_correlate2)]
                shipID2[destName2] = coordlist
                print(shipID2)
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

                        board[generateX][generateY - 1] = "1#"
                        board[generateX + 1][generateY - 1] = "2#"
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"

                        printBoard(board)

                    elif generateX == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX - 1][generateY - 1] = "4#"
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                        printBoard(board)

                    else:
                        
                        # centered vertical
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #top
                            board[generateX][generateY - 1] = "5#"
                            board[generateX - 1][generateY - 1] = "6#"
                            xLetter2 = strConvert(generateX - 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            
                            printBoard(board)

                        elif toporbottom == 1:

                            #bottom
                            board[generateX][generateY - 1] = "7#"
                            board[generateX + 1][generateY - 1] = "8#" 
                            xLetter2 = strConvert(generateX + 1)
                            str_correlate2 = f"({xLetter2},{generateY})"
                            
                            printBoard(board)

                elif orientation == 0:

                #horizontal extremes
            
                    if generateY == 1:

                        board[generateX][generateY - 1] = "1#"
                        board[generateX][generateY] = "2#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                        printBoard(board)

                    elif generateY == (gridSize - 1):

                        board[generateX][generateY - 1] = "3#"
                        board[generateX][generateY - 2] = "4#"
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        
                        printBoard(board)

                    else:

                        # centered horizontal
                        toporbottom = random.randint(0,1)

                        if toporbottom == 0:

                            #right
                            board[generateX][generateY + 1] = "5#"
                            board[generateX][generateY + 2] = "6#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY + 1})"
                            
                            printBoard(board)

                        elif toporbottom == 1:

                            #left
                            board[generateX][generateY - 1] = "7#"
                            board[generateX][generateY - 2] = "8#"
                            xLetter2 = strConvert(generateX)
                            str_correlate2 = f"({xLetter2},{generateY - 1})"
                            printBoard(board)
                coordlist2 = [(str_correlate,str_correlate2)]
                shipID2[destName2] = coordlist2
                print(shipID2)
        

        

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



gooping = True



shipID1 = {}

shipID2 = {}

coordlist = []

p1MovesList = []

p2MovesList = []

shipNamePoss = ["Glizzy Gang", "Chud Man", "Big Chungus", "Sussy Sigma", "Sleepy Joe", "Skibidi Slicer"]

destName = None

destName2 = None

subName = None


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

# Second Board for player 1, shows what they've attacked
domain = createBoard(gridSize)

numShips = 1 # int(input("\nHow many ships are you playing with? (Max 5): "))

placementType = int(input("\nInput 1 to automatically place ships or 0 to manually place ships: "))




# Main function, runs core code

def main(gooping, player):
    # Creating Ships:
        player = "Player 1"
        createDest(gridSize, placementType, board, player)
        # createSub(gridSize, placementType, board, player)
        player = "Player 2"
        createDest(gridSize, placementType, grid, player)
        # createSub(gridSize, placementType, board, player)


        # While loop to maintain runtime

        while gooping == True:

            player = "Player 1"
            print(f"\nIt is {player}'s turn.\n")

            userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
            bombTarget(userBomb, board, player, shipID2, p1MovesList, p2MovesList, destName, destName2, subName)
            print(shipID2)

            # These are for animations & Don't affect functionality
            # time.sleep(.7)
            # arsenal()
            # listInt()

            # Win check
            # gooping = gameEnding(player)

            if gooping == False:
                break

            # Sets player to computer

            player = "Player 2"
            print(f"\nIt is the computer's turn.\n")

            # compTarget(grid)
            # listInt()

            # Win check
            # gooping = gameEnding(player)

            if gooping == False:
                break
            
            continue

main(gooping, player)


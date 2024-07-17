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

p1ShipInfo = []

p2ShipInfo = []

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

# player = "Player 1"
# shipCreateS(numShips, gridSize, player, board)

# player = "Player 2"
# shipCreateS(numShips, gridSize, player, grid)


# Main function, runs core code

def main(gooping):

    # While loop to maintain runtime

    while gooping == True:

        player = "Player 1"
        print(f"\nIt is {player}'s turn.\n")

        userBomb = input(f"\n{player}, Please select a section to hit with your artilery: ")
        # bombTarget(userBomb, board, player)

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

main(gooping)


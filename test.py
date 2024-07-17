"""

1 & 2 - O
3 & 4 - O
5 & 6 - O
7 & 8 - O
9 & 0 - O
A & B - O
C & D - O
E & F - O



















"""



shipLoc = input("Please input a location to sail your ship: ")
                parkedShip = shipLoc.split(",")
                xLetter = parkedShip[0]
                yNumber = parkedShip[1]
                str_correlate = f"({xLetter},{yNumber})"
                print(str_correlate)
                p2ShipInfo.append(str_correlate)
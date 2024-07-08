Requirements:
Create a 5x5 grid
Generate random coordinates within the grid to place the battleship.
Prompt the user to input their guess for the row and column where they think the battleship is located.
Maintain a list of lists to store the user's guesses and update the grid accordingly.
Display the updated grid to the user and inform them whether their guess hit the battleship or not.
PLAN:
	List of List for grid (XS)
	Rand Ship (1 for now) placement (S)
		Store the ships location in a list
		Set up a function which allows random selection
	User Bomb Drop
		list of hit locations (1 list for each user)
		Checks whether or not the hit location is in the computers ship list.
	Display ocean function
		Win cond or repeat

from copy import deepcopy

class gameState:
	def __init__(self):

		# Initial empty grid. The Numpy package is useful for this in proper implementations.
		self.grid = [[' ',' ',' '],
					 [' ',' ',' '],
					 [' ',' ',' ']]

		self.player = 0
		return

	def possibleMoves(self):

		# Returns an array of possible moves from this gameState

		out = []

		for x, row in enumerate(self.grid):
			for y, cell in enumerate(row):
				if(cell == ' '):
					out.append((x,y))

		return out

	def possibleGameStates(self):

		# Returns an array of possible gameStates from this gameState

		out = []

		for moves in self.possibleMoves():
			state = deepcopy(self)

			# Add move on grid
			state.grid[moves[0]][moves[1]] = self.getCurrentPlayerSymbol()

			# Flip player
			state.player = (1,0)[state.player]

			out.append(state)

		return out


	def getCurrentPlayerSymbol(self):
		# Player 0 is O and player 1 is X
		return ('O','X')[self.player]

	def __str__(self):
		rows = []
		for row in self.grid:
			rows.append("|".join(row) + "\n")

		return "-----\n".join(rows)

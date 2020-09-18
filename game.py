from copy import deepcopy
from functools import lru_cache

class gameState:
	def __init__(self, grid = None):

		# Initial grid. The Numpy package is useful for this in proper implementations.
		self.grid = grid or \
					[[None,None,None],
					 [None,None,None],
					 [None,None,None]]

		self.player = 0

		return

	def possibleMoves(self):

		# Returns an array of possible moves from this gameState

		out = []

		for x, row in enumerate(self.grid):
			for y, cell in enumerate(row):
				if(cell == None):
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

	@lru_cache
	def isWonGameState(self):

		for line in self.winnableLines():
			if(len(set(line)) == 1 and line[0] != None):
				return True

		return False

	@lru_cache
	def isTiedGameState(self):
		return len(self.possibleMoves()) == 0 and not self.wonGameState

	def winnableLines(self):
		# Horizontals
		yield from self.grid

		# Verticals
		yield from [[item[cell] for item in self.grid] for cell in range(3)]

		# Diagonals
		yield [self.grid[i][i] for i in range(3)]
		yield [self.grid[i][abs(i-2)] for i in range(3)]

	def getCurrentPlayerSymbol(self):
		# Player 0 is O and player 1 is X
		return ('O','X')[self.player]

	def __str__(self):
		rows = []
		for row in self.grid:
			rows.append("|".join(map(lambda x : x or " ", row)) + "\n")

		return "-----\n".join(rows)

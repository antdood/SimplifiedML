from math import log, sqrt
import random

class node:
	def __init__(self, gameState, model):
		self.gameState = gameState
		self.model = model
		self.isRoot = False

		if(data := self.getData()):
			# Data from model if it exists
			self.visits = data["visits"]
			self.score = data["score"]
		else:
			# Initial values for unexplored nodes
			self.visits = 0
			self.score = 0

		return

	def isLeaf(self):
		# Root node is never leaf
		if(self.isRoot):
			return False

		# Any child not in modeldata
		return (not all(map(lambda x : x in self.model.modelData, self.gameState.possibleGameStates())))

	def isExplored(self):
		return (self.gameState in self.model.modelData)

	def getData(self):
		if(self.isExplored()):
			return self.model.modelData[self.gameState]
		else:
			return {}

	def getChildren(self):
		return [node(gameState, self.model) for gameState in self.gameState.possibleGameStates()]

	def bestChildForSelection(self):
		children = self.getChildren()

		# This can also simply be the total visits of the parent (this). However, that will not work in cases where there are multiple ways to reach the same gameState. Calculating this independantly of the parent also allows us to start the training from any gameState instead of only the root.
		totalVisitsAtLevel = sum([child.visits for child in children])

		def computeSelectionScoreForChild(child):
			# We use the UCB1 formula here

			score = child.score
			visits = child.visits

			if(visits == 0):
				return float('inf')

			return score + 1.0 * sqrt(log(totalVisitsAtLevel)/visits)


		return max(children, key = computeSelectionScoreForChild)

	def rollout(self):
		# Randomly plays out the game until a terminal state is reached

		currentNode = self

		state = currentNode.gameState.isTerminal()

		while(not state[0]):
			possibleGameStates = list(currentNode.gameState.possibleGameStates())
			chosen = random.choice(possibleGameStates)
			currentNode = node(chosen, self.model)
			state = currentNode.gameState.isTerminal()

		# Score of the game in terminal state
		return state[1]

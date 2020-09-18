import yaml
import pickle
import game

class model: 
	def __init__(self, modelPath = "model.yml"):
		with open(modelPath) as modelFile:
			self.model = yaml.safe_load(modelFile) or {}
		return

	def evaluate(self, gameState):

		# Returns the probability of winning given a gameState

		if(isinstance(gameState, game.gameState)):
			gameState = pickle.dumps(gameState)

		if(gameState in self.model.keys()):
			return self.model[gameState]
		else:
			return self.initialize(gameState)

	def initialize(self, gameState):

		# Initializes the probability to win of a given gameState

		self.model[gameState] = 0.5

		return self.model[gameState]

	def save(self, modelPath = "model.yml"):
		with open(modelPath, "w") as modelFile:
			yaml.dump(self.model, modelFile)




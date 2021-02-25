import yaml
import pickle
import game
import node

class model: 
	def __init__(self, modelPath = "model.yml"):
		with open(modelPath) as modelFile:
			self.modelData = yaml.safe_load(modelFile) or {}

		self.rootNode = node.node(game.gameState(), self)
		self.rootNode.isRoot = True
		self.nodePath = []

		return

	def clean(self):
		for node in self.nodePath:
			self.modelData[pickle.dumps(node.gameState)] = {'visits' : node.visits, 'score' : node.score}

		self.rootNode.isRoot = True
		self.nodePath = []

	def save(self, modelPath = "model.yml"):
		with open(modelPath, "w") as modelFile:
			yaml.dump(self.modelData, modelFile)

	def select(self):
		# Recursively travels down the tree of nodes while maximizing UCB1 until a leaf node is reached
		current = self.rootNode

		while(not current.isLeaf()):
			self.nodePath.append(current)

			if(current.gameState.isTerminal()[0]):
				return current

			current = current.bestChildForSelection()

		self.nodePath.append(current)

		return current

	def rollout(self):
		#If no leaf node has been selected for rollout yet
		if(not self.nodePath):
			self.select()

		return self.nodePath[-1].rollout()

	def backprop(self, rolloutValue):

		for node in reversed(self.nodePath):
			node.updateScore(rolloutValue)
			node.visits += 1

			print("Updating")
			print(node.gameState)
			print("Visits : " + str(node.visits))
			print("Score : " + str(node.score))


		return 0



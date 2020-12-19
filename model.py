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

	def save(self, modelPath = "model.yml"):
		with open(modelPath, "w") as modelFile:
			yaml.dump(self.modelData, modelFile)


	def select(self):
		# Recursively travels down the tree of nodes while maximizing UCB1 until a leaf node is reached
		current = self.rootNode

		while(not current.isLeaf()):
			self.nodePath.append(current)
			current = current.bestChildForSelection()

		self.nodePath.append(current)

		return current



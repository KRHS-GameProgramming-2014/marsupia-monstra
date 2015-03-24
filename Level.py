class Level():
	def __init__(self, level, screenSize):
		self.screenSize = screenSize
		self.screenWidth = screenSize[0]
		self.screenHeight = screenSize[1]
		self.blocks = []
		
		self.levelChangeAreas = []
		self.enemies = []
		
		self.players = []
		
		self.blockSize = 50
		self.level = level
		self.load(level)
	
	def 

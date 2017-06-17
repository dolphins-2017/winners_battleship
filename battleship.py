class Game:

	def __init__(self):
		self.board = []
		self.gen = []
		self.columns = ["   1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
	
	def genBoard(self):
		for waves in range(10):
			self.gen.append(["|~|"]*10)
		
		top = "   ".join(self.columns)
		A = "A " + " ".join(self.gen[0])
		B = "B " + " ".join(self.gen[1])
		C = "C " + " ".join(self.gen[2])
		D = "D " + " ".join(self.gen[3])
		E = "E " + " ".join(self.gen[4])
		F = "F " + " ".join(self.gen[5])
		G = "G " + " ".join(self.gen[6])
		H = "H " + " ".join(self.gen[7])
		I = "I " + " ".join(self.gen[8])
		J = "J " + " ".join(self.gen[9])
		breakdown = [top, A, B, C, D, E, F, G, H, I, J]
		for i in breakdown:
			self.board.append(i)

	def printBoard(self):
		for i in  self.board:
			print(i)

	def insertShips(self):
		x = 1
		y = 3
		submarine = ["S", "S", "S"]
		splitlist = list(self.board[x])
		for i in submarine:
			splitlist[y] = i
			newlist = "".join(splitlist)
			self.board[x] = newlist
			x += 1
		self.printBoard()




def main():
	# gameBoard = Game()
	# gameBoard.genBoard()
	# gameBoard.printBoard()
	pass
	
main()

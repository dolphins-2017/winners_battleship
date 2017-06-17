from random import randint

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
		submarine = ["S", "S", "S"]
		destroyer = ["D", "D", "D", "D"]
		small_ship = ["T", "T"]
		aircraft_carrier = ['A', 'A', 'A', 'A', 'A']

		ships = [submarine, destroyer, small_ship, aircraft_carrier]
		#y = 1
		
		for ship in ships:
			desiredrow = (input("What row do you want to place your shipin?\n")).lower()
			if desiredrow == "a":
				y = 1
			z = int(input("What column you want to place your ship in?\n"))
			x = (3*z) +(z-1)
			for i in ship:
				splitlist = list(self.board[y])
				splitlist[x] = i
				newlist = "".join(splitlist)
				self.board[y] = newlist
				y += 1
			x += 3
			self.printBoard()

	def hitOrMiss(self, coords):
		both = list(coords)
		x = both[0].lower()
		y = int(both[1])
		if x == "a":
			x = list(self.board[1])
		if x == "b":
			x = list(self.board[2])
		if x == "c":
			x = list(self.board[3])
		if x == "d":
			x = list(self.board[4])
		if x == "e":
			x = list(self.board[5])
		if x == "f":
			x = list(self.board[6])
		if x == "g":
			x = list(self.board[7])
		if x == "h":
			x = list(self.board[8])
		if x == "i":
			x = list(self.board[9])
		if x == "j":
			x = list(self.board[10])
		if y > 1:
			pos = 4 + 3*(y-1)
		if y == 1:
			pos = 3


		if x[pos] == "~":
			x[pos] = "W"
			newlist = "".join(x)
			self.board[y] = newlist
			return "Miss!"
		else:
			x[pos] = "R"
			newlist = "".join(x)
			self.board[y] = newlist
			return "Hit!"


def main():
	# gameBoard = Game()
	# gameBoard.genBoard()
	# gameBoard.printBoard()
	pass
	
main()

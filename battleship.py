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

		for ship in ships:
			y = 1
			x = 3
			splitlist = list(self.board[y])
			for i in ship:
				splitlist[x] = i
				newlist = "".join(splitlist)
				self.board[y] = newlist
				y += 1
			x += 4
			self.printBoard()

	def hitOrMiss(self, coords):
		both = list(coords)
		x = both[0].lower()
		y = int(both[1])
		if x == "a":
			x = self.board[1]
		if x == "b":
			x = self.board[2]
		if x == "c":
			x = self.board[3]
		if x == "d":
			x = self.board[4]
		if x == "e":
			x = self.board[5]
		if x == "f":
			x = self.board[6]
		if x == "g":
			x = self.board[7]
		if x == "h":
			x = self.board[8]
		if x == "i":
			x = self.board[9]
		if x == "j":
			x = self.board[10]
		if y > 1:
			pos = 3 + (4*y)
		if y == 1:
			pos = 3

		if x[pos] == "~":
			return "Miss!"
		else:
			x[pos] = "X"
			return "Hit!"


def main():
	# gameBoard = Game()
	# gameBoard.genBoard()
	# gameBoard.printBoard()
	pass
	
main()

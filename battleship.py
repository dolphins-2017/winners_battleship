class Game:

	def __init__(self):
		self.board = []
		self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
		self.columns = ["   1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
	
	def genBoard(self):
		for waves in range(10):
			self.board.append(["|~|"]*10)
		
		print("   ".join(self.columns))
		A = "A " + " ".join(self.board[0])
		B = "B " + " ".join(self.board[1])
		C = "C " + " ".join(self.board[2])
		D = "D " + " ".join(self.board[3])
		E = "E " + " ".join(self.board[4])
		F = "F " + " ".join(self.board[5])
		G = "G " + " ".join(self.board[6])
		H = "H " + " ".join(self.board[7])
		I = "I " + " ".join(self.board[8])
		J = "J " + " ".join(self.board[9])
		print(A)
		print(B)
		print(C)
		print(D)
		print(E)
		print(F)
		print(G)
		print(H)
		print(I)
		print(J)



class Ship:

	def __init__(self):
		self.submarine = "SSS"
		self.aircraft_carrier = "AAAAA"
		self.battleship = "BBBB"
		self.small = "QQ"
		self.destroyer = "DDD"



def main():
	gameBoard = Game()
	gameBoard.genBoard()

	
main()


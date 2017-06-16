class Game:

	def __init__(self):
		self.board = []
		self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
		self.columns = ["  1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
	
	def print_board(self):
		for waves in range(10):
			self.board.append(["~"]*10)
		print(self.columns)
		row = 0
		while row <= 8:
			print(self.rows[row], self.board[row])
			row += 1

def main():
	gameBoard = Game()
	gameBoard.print_board()

main()


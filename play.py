def main():
	print("Welcome to Tic Tac Toe")
	board = Board()
	board.print_board() 

	while not board.is_full():
		winner = board.check_winner()
		if winner is not False:
			print("Winner is {}".format(winner))
			break 

	if board.is_full():
		print("Tie Game")


class Board(object):
	def __init__(self):
		self.positions = [' ' for x in range(9)]

	def insert_move(self, pos, letter):
		if self.is_space_free(pos):
			self.positions[pos] = letter

	def print_board(self):
		for i in range(3):
			print('-----------')
			print(' {0} | {1} | {2} '.format(
				self.positions[3*i+0],
				self.positions[3*i+1],
				self.positions[3*i+2]
				))
		print('-----------')

	def is_space_free(self, pos):
		return self.positions[pos] == ' '

	def check_winner(self):
		winning_positions = [
			[0, 1, 2],
			[3, 4, 5],
			[6, 7, 8],
			[0, 3, 6],
			[1, 4, 7],
			[2, 5, 8],
			[0, 4, 8],
			[2, 4, 6]
		]
		for positions in winning_positions:
			a,b,c = positions
			if self.positions[a] is not None and self.positions[a] == self.positions[b] and self.positions[a] == self.positions[c]:
				return self.positions[a]  

		return False 

	def is_full(self):
		if self.positions.count(' ') == 0:
			return True
		else:
			return False 

if __name__ == "__main__":
	main()

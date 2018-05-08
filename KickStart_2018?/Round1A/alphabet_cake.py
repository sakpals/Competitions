class Direction():
	direction = 'DRUL' 
	opp_direction = {'D': 'U', 'U': 'D', 'R': 'L', 'L':'R'}
	next_dir = {'D': 'R', 'R': 'U', 'U': 'L', 'L': 'D'}

	def opposite(self, char):
		return opp_dir[char]

	def next(self, char):
		return next_dir[char]

	def get_dir_index(self, dir, i, j):
		if dir == 'U':
			i -= 1
		elif dir == 'D':
			i += 1
		elif dir == 'R':
			j += 1
		elif dir == 'L':
			j -= 1
		return i, j

class AlphabetCake():
	T = 0
	R = 0
	C = 0

	def read_input(self):
		self.T = int(input())
		for i in range(self.T):
			r, c = input().split(' ')
			self.R, self.C = int(r), int(c)
			# 2D array with list comprehension
			cake = [['?' for i in range(self.R)] for j in range(self.C)]
			
			# input into 2D array
			for i in range(self.R):
				row = input()
				for j in range(self.C):
					cake[i][j] = row[j] 
			self.apply_algo(cake, self.R, self.C)

	def apply_algo(self, cake, r, c):
		d = Direction()
		for i in r:
			for j in c:
				curr = cake[i][j]
				for direction in d.direction:
					t_i, t_j = d.get_dir_index(direction, i, j)
					if cake[t_i][t_j] == curr:
						continue
					
					cake[i][j]
if __name__ == '__main__':
	A = AlphabetCake()
	A.read_input()

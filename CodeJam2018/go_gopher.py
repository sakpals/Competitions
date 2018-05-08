import sys
import random

class GoGopher():
	num_tests = 0
	size = 0
	
	in_i = 10
	in_j = 10

	actual_plots = {}

	def get_num_tests(self):
		self.num_tests = int(input())

	def get_size(self):
		self.size = int(input())

	def first_try(self):
		print(10, 10)
		sys.stdout.flush()

	def bot(self):
		self.in_i, self.in_j = input().split(' ')
		sys.stdin.flush()
		self.actual_plots[(int(self.in_i), int(self.in_j))] = self.adjacent_plots(int(self.in_i), int(self.in_j))
		if self.in_i == -1 and self.in_j == -1:
			sys.exit(1)
		elif self.in_i == 0 and self.in_j == 0:
			sys.exit(0)
		else:
			(a,b) = self.intersecting_adjacent_plots()
			print(a, b)
			sys.stdout.flush()

	def adjacent_plots(self, i, j):
		adj = []
		adj.append([i+1, j])
		adj.append([i, j+1])
		adj.append([i+1, j+1])
		adj.append([i-1, j])
		adj.append([i, j-1])
		adj.append([i-1, j-1])
		adj.append([i-1,j+1])
		adj.append([i+1, j-1])
		return sorted(adj)

	def intersecting_adjacent_plots(self):
		ready_plots = self.actual_plots.keys()
		possible_plots = self.actual_plots.values()

		common_plots = []
		for lst in possible_plots:
			common_plots += lst

		common_plots = sorted(common_plots)

		tally_common_plots = {}
		for [a,b] in common_plots:
			if (a,b) not in tally_common_plots.keys():
				tally_common_plots[(a,b)] = 0
			else:
				tally_common_plots[(a,b)] = tally_common_plots[(a,b)]+1
		
		curr_max = next(iter(tally_common_plots))
		for [a,b] in tally_common_plots.keys():
			if tally_common_plots[(a,b)] > tally_common_plots[curr_max]:
				curr_max = (a,b)
		return curr_max
	

if __name__ == '__main__':
	G = GoGopher()
	G.get_num_tests()
	G.get_size()
	G.first_try()
	while True:
		G.bot()
	#G.actual_plots = {(10,10): [[9, 9], [9, 10], [9, 11], [10, 9], [10, 11], [11, 9], [11, 10], [11, 11]], (10,11): [[9, 10], [9, 11], [9, 12], [10, 10], [10, 12], [11, 10], [11, 11], [11, 12]]}
	#print(G.intersecting_adjacent_plots())
	#print(G.adjacent_plots(10,11))
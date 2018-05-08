class ChocolateFactory():

	def get_input(self):
		t = int(input())
		for i in range(t):
			g, p = [int(x) for x in input().split(' ')]
			groups = sorted([int(x) for x in input().split(' ')], key= lambda x: p - (x%p), reverse=True)
			print(self.calculate_fresh_groups(groups, p))

	def calculate_fresh_groups(self, groups, p):
		num_fresh = 1
		while(len(groups) > 1):
			group_num = groups.pop(0)
			left_over = 0
			if group_num < p:
				left_over = p - group_num
			else:
				left_over = group_num%p
			print(left_over)
			if groups[0]%(p+left_over) == 0:
				num_fresh += 1
		return num_fresh

if __name__ == '__main__':
	C = ChocolateFactory()
	C.get_input()


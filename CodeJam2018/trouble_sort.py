class TroubleSort():
	input_lsts = []
	def bad_index(self, lst):
		for i in range(len(lst)-1):
			if lst[i+1] < lst[i]:
				return i


	def trouble_sort(self, lst):
		done = False
		for i in range(2*len(lst)):
			for i in range(len(lst)-2):
				if lst[i] > lst[i+2]:
					done = False

					# reverse
					first = lst[i]
					last = lst[i+2]
					lst[i] = last
					lst[i+2] = first
				if lst == sorted(lst):
					return True, None
		if not done:
			j = self.bad_index(lst)
			return False, j

	def read_input(self):
		input_lsts = []
		num_test_cases = int(input())
		for i in range(num_test_cases):
			lst = []
			num_elements = int(input())
			for i in range(num_elements):
				for i in input().split(' '):
					lst.append(int(i))
				break
			self.input_lsts.append(lst)

			
	def output(self):
		count = 0
		for lst in self.input_lsts:
			count += 1
			success, index = self.trouble_sort(lst)
			if success:
				print('Case #{}: OK'.format(count))
			else:
				print('Case #{}: {}'.format(count, index))


if __name__ == '__main__':
	T = TroubleSort()
	T.read_input()
	T.output()
	

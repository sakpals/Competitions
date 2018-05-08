
import math

class MaplePancake():
	T = 0
	N = 0
	K = 0
	final_output = []

	def calculate(self, case_num, num_to_sel, vals):
		exposed_SA = 0
		sorted_vals = sorted(vals, key= lambda x: x[2])
		sorted_vals.sort(reverse=True, key=lambda x:x[2])
		vals = sorted_vals[0:num_to_sel]
		if num_to_sel > 1:
			for i in range(len(vals)-1):
				if i == 0:
					exposed_SA += vals[i][2] + vals[i+1][2] - (math.pi*math.pow(vals[i+1][0],2))
				else:
					exposed_SA += vals[i+1][2] - (math.pi*math.pow(vals[i][0],2))
		else:
			exposed_SA = vals[0][2]
		self.final_output.append((case_num, round(exposed_SA,9)))

	def read_input(self):
		self.T = int(input())
		for i in range(self.T):
			n, k = input().split(' ')
			self.N = int(n)
			self.K = int(k)
			vals = []
			for j in range(self.N):
				r, h = input().split(' ')
				SA = math.pi*math.pow(int(r), 2) + (2*math.pi*int(r)*int(h))
				vals.append((int(r), int(h), SA))
			self.calculate(i+1, self.K, vals)
		self.result()

	def result(self):
		for (n, sa) in self.final_output:
			print('Case #{}: {}'.format(n, sa))

if __name__ == '__main__':
	P = MaplePancake()
	P.read_input()

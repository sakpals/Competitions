
class RobotHack():

	damage = []
	program = []

	def read_input(self):
		t = int(input())
		for i in range(t):
			dam, pro = input().split(' ')
			self.damage.append(dam)
			self.program.append(pro)

	def count_damage(self, p):
		chrg = 1
		dam = 0
		for command in p:
			if command == 'C':
				chrg *= 2
			else:
				dam += chrg
		return dam

	def hack(self, d, p):
		for i in range(len(p)):
			if i != (len(p)-1):
				if  p[i] == 'C' and p[i+1] == 'S':
					p = list(p)
					p[i], p[i+1] = p[i+1], p[i]
					''.join(p)
					return p
		return 'IMPOSSIBLE'

	def check_program(self):
		for i in range(len(self.damage)):
			if self.count_damage(self.program[i]) <= int(self.damage[i]):
				print('Case #{}: {}'.format(i+1, 0))
			else:
				num_hacks = 0
				self.program[i] = self.hack(self.damage[i], self.program[i])
				num_hacks += 1
				if self.program[i] != 'IMPOSSIBLE':
					while(self.count_damage(self.program[i]) > int(self.damage[i])):
						trials -= 1
						self.program[i] = self.hack(self.damage[i], self.program[i])
						num_hacks += 1
						if self.program[i] == 'IMPOSSIBLE':
							print('Case #{}: {}'.format(i+1, 'IMPOSSIBLE'))
					print('Case #{}: {}'.format(i+1, num_hacks))
				else:
					print('Case #{}: {}'.format(i+1, 'IMPOSSIBLE'))



if __name__ == '__main__':
	r = RobotHack()
	r.read_input()
	r.check_program()
	
	
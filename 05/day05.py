import numpy as np

def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().splitlines()	
	input = []
	for f in file_puzzle_input:
		temp = f.split(" ")
		temp.remove('->')
		for t in temp:
			temp_t = tuple(int(num) for num in t.split(','))
			input.append(temp_t)
	integers = [*zip(input[::2], input[1::2])]
	return integers

#grid size
def calc_max(input):
	x = set()
	y = set()
	for i in input:
		for p in i:
			x.add(p[0])
			y.add(p[1])
	return max(y) + 1, max(x) + 1

#find answer
def calc(vents):
	ans = (vents > 1).sum()
	return ans

def plot_vents(input, part):
	vents = np.zeros(shape=(calc_max(input)))
	for p in input:
		#horizontal
		if p[0][0] == p[1][0]:
			h_sorted = tuple(sorted(p, key = lambda x: x[1]))
			i = h_sorted[0][1]
			while i <= h_sorted[1][1]:
				vents[i, h_sorted[0][0]] += 1
				i += 1
		#vertical
		elif p[0][1] == p[1][1]:
			v_sorted = tuple(sorted(p, key = lambda x: x[0]))
			i = v_sorted[0][0]
			while i <= v_sorted[1][0]:
				vents[v_sorted[0][1], i] += 1
				i += 1
		#diagonal 45 degree angle
		elif abs(p[0][0] - p[1][0]) == abs(p[0][1] - p[1][1]) and part == 2:
			h_sorted = tuple(sorted(p, key = lambda x: x[0]))
			i = h_sorted[0][1]
			j = h_sorted[0][0]
			while j <= h_sorted[1][0]:
				vents[i, j] += 1
				if h_sorted[0][1] > h_sorted[1][1]:
					i -= 1
				else:
					i += 1
				j += 1
		else:
			continue
	return calc(vents)

def main():
	input = read_input()
	print("the answer to part 1 is: " + str(plot_vents(input, 1)))
	print("the answer to part 2 is: " + str(plot_vents(input, 2)))

if __name__ == "__main__":
	main()
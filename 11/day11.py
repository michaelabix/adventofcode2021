import copy

def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
	input = []
	for f in file_puzzle_input:
		input.append(list(int(x) for x in str(f)))
	return input

def part1(input, steps):
	grid = copy.deepcopy(input)
	count = 0
	flashes = 0
	col = len(grid)
	length = len(grid[0])
	while count < steps:
		#increase power level of each octopus by 1
		for index, i in enumerate(grid):
			for ind, j in enumerate(i):
				grid[index][ind] += 1
		#octopus flash - create list and append each new flash to the end
		flash = []
		for index, i in enumerate(grid):
			for ind, j in enumerate(i):
				if j > 9:
					flash.append((index, ind))
					flashes += 1
		#check surrounding
		for f in flash:
			grid[f[0]][f[1]]
			around = [(f[0], f[1] - 1), (f[0], f[1] + 1), (f[0] - 1, f[1]), (f[0] + 1, f[1]), (f[0] - 1, f[1] - 1), (f[0] + 1, f[1] - 1), (f[0] - 1, f[1] + 1), (f[0] + 1, f[1] + 1)]
			#check neighbors
			for a in around:
				if a[0] >= 0 and a[0] < col and a[1] >= 0 and a[1] < length:
					grid[a[0]][a[1]] += 1
					if grid[a[0]][a[1]] > 9 and a not in flash:
						flashes += 1
						flash.append(a)
		#set flashed to zero
		for index, i in enumerate(grid):
			for ind, j in enumerate(i):
				if j > 9:
					grid[index][ind] = 0
		count += 1
	return flashes

#copy now, refactor later
def part2(input, steps):
	grid = copy.deepcopy(input)
	count = 0
	flashes = 0
	col = len(grid)
	length = len(grid[0])
	while count < steps:
		flashes_at_once = 0
		#increase power level of each octopus by 1
		for index, i in enumerate(grid):
			for ind, j in enumerate(i):
				grid[index][ind] += 1
		#octopus flash - create list and append each new flash to the end
		flash = []
		for index, i in enumerate(grid):
			for ind, j in enumerate(i):
				if j > 9:
					flash.append((index, ind))
					flashes += 1
					flashes_at_once += 1
		#check surrounding
		for f in flash:
			grid[f[0]][f[1]]
			around = [(f[0], f[1] - 1), (f[0], f[1] + 1), (f[0] - 1, f[1]), (f[0] + 1, f[1]), (f[0] - 1, f[1] - 1), (f[0] + 1, f[1] - 1), (f[0] - 1, f[1] + 1), (f[0] + 1, f[1] + 1)]
			#check neighbors
			for a in around:
				if a[0] >= 0 and a[0] < col and a[1] >= 0 and a[1] < length:
					grid[a[0]][a[1]] += 1
					if grid[a[0]][a[1]] > 9 and a not in flash:
						flashes += 1
						flashes_at_once += 1
						flash.append(a)
		#set flashed to zero
		for index, i in enumerate(grid):
			for ind, j in enumerate(i):
				if j > 9:
					grid[index][ind] = 0
		#check if flashed simultaneously
		if flashes_at_once == col * length:
			return count + 1 
		count += 1

def main():
	input = read_input()
	print("the answer to part 1 is: " + str(part1(input, 100)))
	print("the answer to part 2 is: " + str(part2(input, 10000)))

if __name__ == "__main__":
	main()
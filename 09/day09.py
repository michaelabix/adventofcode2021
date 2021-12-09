def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
	input = []
	for f in file_puzzle_input:
		temp = []
		for i in f:
			temp.append(int(i))
		input.append(temp)
	return input

def get_low_points(input):
	low_points = []
	columns = len(input)
	coordinates = []
	for ind, i in enumerate(input):
		items = len(i)
		for ind2, j in enumerate(i):
			around = []
			if (ind - 1) < columns and (ind - 1) >= 0:
				around.append(input[ind - 1][ind2])
			if (ind + 1) < columns and (ind + 1) >= 0:
				around.append(input[ind + 1][ind2])
			if (ind2 - 1) < items and (ind2 - 1) >= 0:
				around.append(input[ind][ind2 - 1])
			if (ind2 + 1) < items and (ind2 + 1) >= 0:
				around.append(input[ind][ind2 + 1])
			if min(around) > j:
				low_points.append(j)
				coordinates.append((ind, ind2))
	return low_points, coordinates

def part1(input):
	low_points, coordinates = get_low_points(input)
	answer = 0
	for l in low_points:
		answer += (l + 1)
	return answer, coordinates

def get_basin(input, c):
	columns = len(input)
	items = len(input[0])
	coords = []
	coords.append(c)
	for s in coords:
		top = (s[0] - 1, s[1])
		bottom = (s[0] + 1, s[1])
		left = (s[0], s[1] - 1)
		right = (s[0], s[1] + 1)
		if top[0] < columns and top[0] >= 0:
			if input[top[0]][top[1]] != 9 and top not in coords:
				coords.append(top)
		if bottom[0] < columns and bottom[0] >= 0:
			if input[bottom[0]][bottom[1]] != 9 and bottom not in coords:
				coords.append(bottom)
		if left[1] < items and left[1] >= 0:
			if input[left[0]][left[1]] != 9 and left not in coords:
				coords.append(left)
		if right[1] < items and right[1] >= 0:
			if input[right[0]][right[1]] != 9 and right not in coords:
				coords.append(right)
	return len(coords)
	
def part2(input, coordinates):
	sums = []
	for c in coordinates:
		sums.append(get_basin(input, c))
	sums.sort(reverse = True)
	return sums[0] * sums[1] * sums[2]

def main():
	input = read_input()
	answer, coordinates = part1(input)
	print("the answer to part 1 is: " + str(answer))
	print("the answer to part 2 is: " + str(part2(input, coordinates)))

if __name__ == "__main__":
	main()
def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
	return file_puzzle_input

def part1(input):
	x = 0
	length = len(input[0])
	gamma = ""
	epsilon = ""
	while x < length:
		temp = []
		for i in input:
			temp.append(i[x])
		positive = temp.count("1")
		zero = temp.count("0")
		if positive > zero:
			gamma += "1"
			epsilon += "0"
		elif zero > positive:
			gamma += "0"
			epsilon += "1"
		else:
			print("something went wrong or positives and zero cannot be equal")
		x += 1
	return int(gamma, 2) * int(epsilon, 2)

def rating(values, gas):
	input = values.copy()
	x = 0
	length = len(input[0])
	while (x < length) and (len(input) > 1):
		temp = []
		keep = "0"
		for i in input:
			temp.append(i[x])
		positive = temp.count("1")
		zero = temp.count("0")
		if (positive > zero or positive == zero) and gas == "o":
			keep = "1"
		elif positive < zero and gas == "c":
			keep = "1"
		for index, i in reversed(list(enumerate(input))):
			if i[x] != keep:
				input.pop(index)
		x += 1
	return int(input[0], 2)
	
def part2(input):
	o2 = rating(input, "o")
	c = rating(input, "c")
	return c * o2
	
def main():
	input = read_input()
	print("the answer to part 1 is: " + str(part1(input)))
	print("the answer to part 2 is: " + str(part2(input)))

if __name__ == "__main__":
	main()
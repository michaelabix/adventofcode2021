def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().strip().split(",")
	input = []
	for f in file_puzzle_input:
		input.append(int(f))
	return input

def calc(input, p):
	mx = max(input)
	counter = 0
	lowest = mx
	lowest_gas = mx * mx * mx * len(input)
	while counter <= mx:
		gas = 0
		for i in input:
			if p == 2:
				temp = abs(i - counter)
				gas += int((temp * (temp + 1)) / 2)
			else:
				gas += abs(i - counter)
		if gas < lowest_gas:
			lowest = counter
			lowest_gas = gas
		counter += 1
	return lowest, lowest_gas

def main():
	input = read_input()
	print("the answer to part 1 is: " + str(calc(input, 1)))
	print("the answer to part 2 is: " + str(calc(input, 2)))

if __name__ == "__main__":
	main()
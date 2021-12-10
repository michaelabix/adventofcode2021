from statistics import median 

def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
	return file_puzzle_input

def parse(input, vals):
	invalid_char = []
	incomplete = []
	for i in input:
		last_open = []
		corr = 0
		for char in i:
			if char in vals.keys():
				last_open.append(char)
			elif last_open and char in vals.values():
				if char == vals[last_open[-1]]:
					last_open.pop()
				else:
					corr = 1
					invalid_char.append(char)
					break
		if corr == 0:
			incomplete.append(i)
	return invalid_char, incomplete

def part1(invalid):
	scores = {')' : 3, ']' : 57 , '}' : 1197, '>' : 25137}
	answer = 0
	for i in invalid:
		answer += scores[i]
	return answer

def part2(incomplete, vals):
	scores = {'(' : 1, '[' : 2 , '{' : 3, '<' : 4}
	answers = []
	for i in incomplete:
		answer = 0
		last_open = []
		close = ""
		for char in i:
			if char in vals.keys():
				last_open.append(char)
			elif last_open and char in vals.values():
				if char == vals[last_open[-1]]:
					last_open.pop()
		for l in reversed(last_open):
			answer *= 5
			answer += scores[l]
		answers.append(answer)
	return median(answers)

def main():
	input = read_input()
	vals = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
	invalid_chars, incomplete = parse(input, vals)
	print("the answer to part 1 is: " + str(part1(invalid_chars)))
	print("the answer to part 2 is: " + str(part2(incomplete, vals)))

if __name__ == "__main__":
	main()
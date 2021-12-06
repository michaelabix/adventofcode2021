from collections import deque

def read_input():
	with open("puzzle_input", 'r') as f:
  		input = [int(i) for l in f for i in list(l) if i.isnumeric()]
	return input

def calc(input, num):
	counter = 0
	l = []
	while counter < 9:
		l.append(input.count(counter))
		counter += 1
	counter = 0
	l = deque(l)
	while counter < num:
		l.rotate(-1)
		l[6] += l[-1]
		counter += 1
	return sum(l)

def main():
	input = read_input()
	print("the answer to part 1 is: " + str(calc(input,80)))
	print("the answer to part 2 is: " + str(calc(input,256)))

if __name__ == "__main__":
	main()
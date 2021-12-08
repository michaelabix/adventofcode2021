def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
	input = []
	for f in file_puzzle_input:
		input.append(tuple(f.split('|')))
	return input

def part1(input):
	counts = dict()
	for i in input:
		digits = i[1].split()
		for d in digits:
			length = len(d)
			if length == 2 or length == 3 or length == 4 or length == 7:
				if length in counts:
					counts[length] += 1
				else:
					counts[length] = 1
	answer = sum(counts.values())
	return answer

def find_digits(input, length, iteration):
	l = input.split()
	sets = []
	for i in l:
		if len(i) == length and iteration != 1:
			values = set(i)
			#for char in i:
			#	values.add(char)
			sets.append(values)
		elif len(i) == length and iteration == 1:
			values = set(i)
			#for char in i:
			#	values.add(char)
			return values
		else:
			continue
	return sets

def find(input):
	key = dict()
	top = ""
	middle = ""
	top_left = ""
	bottom_left = ""
	legend = {'1':2, '7':3, '4':4, '8':7, 'x':6, 'y':5}
	for l in legend:
		if l.isnumeric():
			key[l] = find_digits(input, legend[l], 1)
		else:
			key[l] = find_digits(input, legend[l], 0)
	#find 7 and compare to 1 to find top
	top = key['7'].difference(key['1'])
	#find 3 and compare to 4 to find middle and top
	for ind, i in enumerate(key['y']):
		if(key['7'].issubset(i)):
			key['3'] = i
			middle = key['4'].intersection(i.difference(key['7']))
			top_left = key['4'].difference(i)
			del key['y'][ind]
			break
		else:
			continue
	if top and top_left and middle:
		for i in key['x']:
			if not middle.issubset(i):
				key['0'] = i
				key['x'].remove(i)
		for i in key['y']:
			if top_left.issubset(i):
				key['5'] = i
			elif not top_left.issubset(i):
				key['2'] = i
			else:
				print("something weird happened")
		key.pop('y')
		for i in key['x']:
			if (key['5'] | key['1']) == i:
				key['9'] = i
			elif not (key['5'] | key['1']) == i:
				key['6'] = i
			else:
				print("something weird happened")
		key.pop('x')
	else:
		print("something went wrong")
	return key

def part2(input):
	ans = 0
	for i in input:
		#print(i)
		key = find(i[0])
		values = i[1].split()
		nums = ""
		for v in values:
			for k, val in key.items():
				if set(v) == val:
					nums = nums + str(k)
		ans += int(nums)
	return ans

def main():
	input = read_input()
	print("the answer to part 1 is: " + str(part1(input)))
	print("the answer to part 2 is: " + str(part2(input,)))

if __name__ == "__main__":
	main()
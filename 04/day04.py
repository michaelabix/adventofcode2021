import re
import copy

class bingo_card:
	def __init__(self, card):
		self.card = card
		self.track_card = copy.deepcopy(card)
		self.score = 0
		self.turns = 0
	
	def check_num(self, num, turns):
		self.turns = turns
		#check for and track number
		for i, c in enumerate(self.card):
			for j, n in enumerate(c):
				if n == num:
					self.track_card[i][j] = -1
		self.check_bingo(num)

	def check_bingo(self, num):
		#check for bingo
		x = len(self.track_card[0])
		y = len(self.track_card)
		i = 0
		j = 0
		c_bingo = 0
		#check horizontal
		for c in self.track_card:
			if all(element == -1 for element in c):
				self.set_score(num)
				c_bingo = 1
				break
		#check vertical
		while i < y:
			count_v = 0
			while j < x:
				if self.track_card[j][i] == -1:
					count_v += 1
					if count_v == y:
						self.set_score(num)
						c_bingo = 1
						count_v = 0
						break
					else:
						j += 1
						continue
				else:
					break
			i += 1	
		return c_bingo
	
	def set_score(self, num):
		count = 0
		for tc in self.track_card:
			count += sum(x for x in tc if x not in [-1])
		self.score = count * num

	def get_score(self):
		return self.score
	
	def get_turns(self):
		return self.turns

	def print_card(self):
		for c in self.card:
			print(c)
		print("\n")
		for t in self.track_card:
			print(t)
		print("\n")

def read_input():
	file_puzzle_input = open("puzzle_input", 'r').read().split("\n\n")
	return file_puzzle_input

def parse_bingo():
	values = read_input()
	nums = values[0].split(",")
	cards = []
	values.pop(0)
	for v in values:
		lines = []
		temp_lines = re.sub(r' {2,}' , ' ', v).splitlines()
		for t in temp_lines:
			new_temp = t.strip().split(' ')
			lines.append([int(x) for x in new_temp])
		card = bingo_card(lines)
		cards.append(card)
	return nums, cards

def play(nums, bingo):
	#play game
	for b in bingo:
		for i, n in enumerate(nums):
			turns = i
			if not b.get_score():
				b.check_num(int(n), turns)
	lowest = 0
	highest = 0
	previous = bingo[0].get_score()
	for i, b in enumerate(bingo):
		if b.get_turns() < previous:
			lowest = i
			previous = b.get_turns()

	for i, b in enumerate(bingo):
		if b.get_turns() > previous:
			highest = i
			previous = b.get_turns()
	return bingo[lowest].get_score(), bingo[highest].get_score()

def main():
	nums, bingo = parse_bingo()
	answers = play(nums, bingo)
	print("the answer to part 1 is: " + str(answers[0]))
	print("the answer to part 2 is: " + str(answers[1]))

if __name__ == "__main__":
	main()
instructions = []

def read_input():
    file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
    for f in file_puzzle_input:
        instructions.append(f)
        
def part1():
    forward = 0
    depth = 0
    for i in instructions:
        temp = i.split(' ')
        if temp[0] == 'forward':
            forward += int(temp[1])
        elif temp[0] == 'up':
            depth -= int(temp[1])
        elif temp[0] == 'down':
            depth += int(temp[1])
        else:
            print("invalid input")
    return forward * depth

def part2():
    forward = 0
    depth = 0
    aim = 0
    for i in instructions:
        temp = i.split(' ')
        if temp[0] == 'forward':
            forward += int(temp[1])
            depth += aim * int(temp[1])
        elif temp[0] == 'up':
            aim -= int(temp[1])
        elif temp[0] == 'down':
            aim += int(temp[1])
        else:
            print("invalid input")
    return depth * forward

def main():
    read_input()
    print("the answer for part 1 is: " + str(part1()))
    print("the answer for part 2 is: " + str(part2()))

if __name__ == "__main__":
     main()

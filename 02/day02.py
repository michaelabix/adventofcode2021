instructions = []

def read_input():
    file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
    for f in file_puzzle_input:
        instructions.append(f)
        
def calculate():
    forward = 0
    forward2 = 0
    depth = 0
    depth2 = 0
    aim = 0
    for i in instructions:
        temp = i.split(' ')
        if temp[0] == 'forward':
            forward += int(temp[1])
            forward2 += int(temp[1])
            depth2 += aim * int(temp[1])
        elif temp[0] == 'up':
            depth -= int(temp[1])
            aim -= int(temp[1])
        elif temp[0] == 'down':
            depth += int(temp[1])
            aim += int(temp[1])
        else:
            print("invalid input")
    return forward * depth, depth2 * forward2

def main():
    read_input()
    answer = calculate()
    print("the answer for part 1 is: " + str(answer[0]))
    print("the answer for part 2 is: " + str(answer[1]))

if __name__ == "__main__":
     main()

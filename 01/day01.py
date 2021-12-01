#import

#set global variables
measurements = []

def read_input():
    file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
    for f in file_puzzle_input:
        measurements.append(int(f))

def part1():
    last = 0
    counter = -1
    for m in measurements:
        if m > last:
            counter += 1
        last = m
    return counter

def part2():
    last = 0
    counter = -1
    i = 0
    while i < (len(measurements) - 2):
        num = measurements[i] + measurements[i + 1] + measurements[i + 2]
        if num > last:
            counter += 1
        last = num
        i += 1
    return counter

def main():
    read_input()
    print("the answer for part 1 is: " + str(part1()))
    print("the answer for part 2 is: " + str(part2()))

if __name__ == "__main__":
    main()

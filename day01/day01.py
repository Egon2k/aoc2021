def part1(data):
    pass

def part2(data):
    pass

if __name__ == "__main__":
    data = []

    with open('day01/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))
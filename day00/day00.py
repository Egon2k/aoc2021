def part1():
    pass

def part2():
    pass

if __name__ == "__main__":
    data = []

    with open('data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))
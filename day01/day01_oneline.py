def part1(data):
    return sum(1 for i in range(len(data)-1) if data[i+1]>data[i])

def part2(data):
    return sum(1 for i in range(len(data)-3) if sum(data[i+1:i+4])>sum(data[i:i+3]))

if __name__ == "__main__":
    data = []

    with open('day01/data.txt') as f:
        for line in f:
            data.append(int(line.strip()))

    print(part1(data))
    print(part2(data))
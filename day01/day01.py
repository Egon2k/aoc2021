def part1(data):
    count = 0
    for i,nmbr in enumerate(data[:-1]):
        if int(data[i+1]) > int(data[i]):
            count = count +1
    return count

def part2(data):
    count = 0
    for i,nmbr in enumerate(data[:-3]):
        if (int(data[i+1]) + int(data[i+2]) + int(data[i+3])) > \
            int(data[i  ]) + int(data[i+1]) + int(data[i+2]):
            count = count +1
    return count

if __name__ == "__main__":
    data = []

    with open('day01/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))
def part1(data):
    depth = 0
    pos = 0
    
    for line in data:
        cmd = line.split()

        if cmd[0] == "forward":
            pos += int(cmd[1])
        elif cmd[0] == "down":
            depth += int(cmd[1])
        elif cmd[0] == "up":
            depth -= int(cmd[1])

    return depth * pos

def part2(data):
    depth = 0
    pos = 0
    aim = 0
    
    for line in data:
        cmd = line.split()

        if cmd[0] == "forward":
            pos += int(cmd[1])
            depth += int(cmd[1]) * aim
        elif cmd[0] == "down":
            aim += int(cmd[1])
        elif cmd[0] == "up":
            aim -= int(cmd[1])

    return depth * pos
    
if __name__ == "__main__":
    data = []

    with open('day02/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))
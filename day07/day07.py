'''''''''''''''''''''
Ey, nicht spicken :P 
'''''''''''''''''''''
def part1_stats(data):
    from statistics import median

    median = int(median(data))
    result = 0
    for crab in data:
        result += abs(median - crab)
    return result

def part2_stats(data):
    from statistics import mean

    mean = int(mean(data))
    result = 0
    for crab in data:
        result += abs(mean - crab) * (abs(mean - crab) + 1) // 2
    return result

def part1(data):
    distances = list()
    for x in range(min(data), max(data) + 1):
        sum = 0
        for crab in data:
            sum += abs(x - crab)
        distances.append(sum)
    return min(distances)

def part2(data):
    distances = list()
    for x in range(min(data), max(data) + 1):
        sum = 0
        for crab in data:
            sum += abs(x - crab) * (abs(x - crab) + 1) // 2
        distances.append(sum)
    return min(distances)
    
if __name__ == "__main__":
    with open('day07/data.txt') as f:
        for line in f:
            data = [int(i) for i in line.strip().split(',')]

    print(part1_stats(data))
    print(part2_stats(data))
    print(part1(data))
    print(part2(data))
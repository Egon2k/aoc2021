'''''''''''''''''''''
Ey, nicht spicken :P 
'''''''''''''''''''''
def part1(data):
    count = 0
    for line in data:
        for digit in line[line.index('|'):]:
            if len(digit) in [2,3,4,7]:
                count += 1
    return count

def part2(data):
    pass
    
if __name__ == "__main__":
    data = []

    with open('day08/data.txt') as f:
        for line in f:
            data.append(line.strip().split())

    print(part1(data))
    print(part2(data))
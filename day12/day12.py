'''
Willkommen im #Neuland
'''
from collections import defaultdict

def part1(caves):
    currCaveInit = 'start'
    visitedSmallsInit = set()
    visitedSmallsInit.add('start')
    queue = [(currCaveInit, visitedSmallsInit)]
    sum = 0

    while(queue):
        currCave, visitedSmalls = queue.pop(0)

        if currCave == 'end':
            sum += 1
            continue

        for dest in caves[currCave]:
            if dest not in visitedSmalls:
                newVisitedSmalls = set(visitedSmalls)
                if dest.lower() == dest:
                    newVisitedSmalls.add(dest)
                queue.append((dest, newVisitedSmalls))
    return sum


def part2(data):
    pass

if __name__ == '__main__':
    data = []

    with open('day12/data.txt') as f:
        for line in f:
            data.append([x for x in line.strip().split('-')])

    # https://stackoverflow.com/a/11509743
    caves = defaultdict(list)
    for src, dest in data:
        caves[src].append(dest)
        caves[dest].append(src)

    print(part1(caves))
    print(part2(caves))
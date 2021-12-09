'''''''''''''''''''''''''''''''''
Wer das hier liest ist doof :P
'''''''''''''''''''''''''''''''''
def getNeighbor(data, row, col, dir):
    '''
    returns the neighbors value according to the direction 
    for the given coordinates - returns 9 in case of edge
    0 = up, 1 = down, 2 = left, 3 = right
    '''
    if dir == 0: # up
        if col > 0:
            return data[row][col-1]
    elif dir == 1: # down
        if col < len(data[0])-1:
            return data[row][col+1]
    elif dir == 2: # left
        if row > 0:
            return data[row-1][col]
    elif dir == 3: # right
        if row < len(data)-1:
            return data[row+1][col]
    return 9

def getNeighborsLess9(data, row, col):
    '''
    returns a list of all neighbors of the given coords 
    that are lower than 9
    '''
    neighbors = list()
    if getNeighbor(data, row, col, 0) < 9:
        neighbors.append((row, col-1))
    if getNeighbor(data, row, col, 1) < 9:
        neighbors.append((row, col+1))
    if getNeighbor(data, row, col, 2) < 9:
        neighbors.append((row-1, col))
    if getNeighbor(data, row, col, 3) < 9:
        neighbors.append((row+1, col))
    return neighbors

def getBasinSize(data, row, col):
    '''
    goes through all parts of basin until no new 
    neighbar < 9 is found
    '''
    origin = (row, col)
    basin = [origin]
    a = True
    while(a):
        for i in basin:
            neighbors = getNeighborsLess9(data, i[0], i[1])
            for neighbor in neighbors:
                if neighbor not in basin:
                    basin.append(neighbor)

        for i in basin:
            neighbors = getNeighborsLess9(data, i[0], i[1])
            # no new neighbors found if all found neighbors are part of basin
            for x in neighbors:
                if x not in basin:
                    break
        a = False
    return len(basin)

def part1(data):
    sum = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if all(data[row][col] < getNeighbor(data, row, col, x) for x in range(4)):
                sum += data[row][col] + 1
    return sum


def part2(data):
    basinSizes = list()
    for row in range(len(data)):
        for col in range(len(data[0])):
            if all(data[row][col] < getNeighbor(data, row, col, x) for x in range(4)):
                basinSizes.append(getBasinSize(data, row, col))

    # sort and return the product of the last/biggest 3 basins
    basinSizes.sort()
    return basinSizes[-3] * basinSizes[-2] * basinSizes[-1]

if __name__ == "__main__":
    data = []

    with open('day09/data.txt') as f:
        for line in f:
            data.append([int(x) for x in line.strip()])

    print(part1(data))
    print(part2(data))
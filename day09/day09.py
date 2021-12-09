'''''''''''''''''''''''''''''''''
Wer das hier liest, ist doof :P 
'''''''''''''''''''''''''''''''''
def getNeighbor(data, row, col, dir):
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

def part1(data):
    sum = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            dirs = [False, False, False, False]
            if data[row][col] < getNeighbor(data, row, col, 0): # up
                dirs[0] = True
            if data[row][col] < getNeighbor(data, row, col, 1): # down
                dirs[1] = True
            if data[row][col] < getNeighbor(data, row, col, 2): # left
                dirs[2] = True
            if data[row][col] < getNeighbor(data, row, col, 3): # right
                dirs[3] = True
            
            if all(dirs):
                sum += data[row][col] + 1
    return sum

def part2(data):
    pass

if __name__ == "__main__":
    data = []

    with open('day09/data.txt') as f:
        for line in f:
            data.append([int(x) for x in line.strip()])

    print(part1(data))
    print(part2(data))

'''''''''''''''''''''
Ey, nicht spicken :P 
'''''''''''''''''''''
def count(grid, threshold):
    count = 0
    for line in grid:
        for nmbr in line:
            if nmbr > threshold:
                count += 1
    return count

def sortCoords(instr):
    i = instr[:]
    if i[0] > i[2]:
        temp = i[2]
        i[2] = i[0]
        i[0] = temp
    
    if i[1] > i[3]:
        temp = i[3]
        i[3] = i[1]
        i[1] = temp
    return i

def solve(instrs, part):
    dim = 1000
    grid = [[0]*dim for i in range(dim)] # create grid with dim x dim
    
    for instr in instrs:
        if instr[0] == instr[2]: # x coords are the same
            i = sortCoords(instr)
            for y in range(i[1],i[3]+1):
                grid[y][i[0]] += 1
        elif instr[1] == instr[3]: # y coords are the same
            i = sortCoords(instr)
            for x in range(i[0],i[2]+1):
                grid[i[1]][x] += 1
        else:
            if part == 1:
                # ignore for now (and we all know it will be important in part2)
                pass
            else:
                i = sortCoords(instr)
                x = instr[0]
                y = instr[1]
                for _ in range(i[2] - i[0] + 1):
                    grid[y][x] += 1
                    if instr[0] < instr[2]:
                        x += 1
                    else:
                        x -= 1
                    if instr[1] < instr[3]:
                        y += 1
                    else:
                        y -= 1
           
    return count(grid, 1)
    
def part1(instrs):
    return solve(instrs, 1)

def part2(instrs):
    return solve(instrs, 2)

def prepareData(data):
    instr = list()
    for line in data:
        instr.append([int(i) for i in line.replace(' -> ', ',').split(',')])
    return instr

if __name__ == "__main__":
    data = []

    with open('day05/data.txt') as f:
        for line in f:
            data.append(line.strip())
      
    # prepare data for processing
    instrs = prepareData(data)
        
    print(part1(instrs))
    print(part2(instrs))
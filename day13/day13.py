'''
Ich hasse Montage
'''
def transpose(i):
    '''
    returns the transpose of a given matrix i
    '''
    return list(map(list, zip(*i)))

def fold(sheet, pos):
    new_sheet = list()
    for row in range(pos):
        new_row = list()
        for i in range(len(sheet[0])):
            new_row.append(sheet[row][i] or sheet[-(row+1)][i])
        new_sheet.append(new_row)
    return new_sheet

def fold_x(sheet, x_pos):
    return fold(transpose(sheet), x_pos)

def fold_y(sheet, y_pos):
    return fold(sheet, y_pos)

def count(sheet):
    sum = 0
    for row in sheet:
        for col in row:
            if col == 1:
                sum += 1
    return sum

def solve(sheet, instr):
    dir, pos = instr
    if dir == 'x':
        folded = fold_x(sheet, pos)
    elif dir == 'y':
        folded = fold_y(sheet, pos)
    return folded

def part1(sheet, instr):
    return count(solve(sheet, instr))

def part2(sheet, instrs):
    pass

if __name__ == '__main__':
    coords = []
    instrs = []

    with open('day13/data.txt') as f:
        for line in f:
            #data.append([x for x in line.strip().split('-')])
            if line.startswith("fold along "):
                dir, pos = line.split()[-1].split('=')
                instrs.append((dir,int(pos)))
            elif line != "\n":
                x,y = line.strip().split(',')
                coords.append((int(x),int(y)))

    # calc sheet dimensions
    x_max = max([x for x, _ in coords]) + 1
    y_max = max([y for _, y in coords]) + 1

    sheet = grid = [[0] * x_max for i in range(y_max)]
    for x, y in coords:
        sheet[y][x] = 1        

    print(part1(sheet, instrs[0]))
    print(part2(sheet, instrs))
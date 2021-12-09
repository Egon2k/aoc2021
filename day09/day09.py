'''''''''''''''''''''''''''''''''
Wer das hier liest, ist doof :P 
'''''''''''''''''''''''''''''''''
def part1(data):
    sum = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            dirs = [False, False, False, False]
            # up
            if col > 0:
                if data[row][col] < data[row][col-1]:
                    dirs[0] = True
            else:
                dirs[0] = True
            # down
            if col < len(data[0])-1:
                if data[row][col] < data[row][col+1]:
                    dirs[1] = True
            else:
                dirs[1] = True
            # left
            if row > 0:
                if data[row][col] < data[row-1][col]:
                    dirs[2] = True
            else:
                dirs[2] = True
            # right
            if row < len(data)-1:
                if data[row][col] < data[row+1][col]:
                    dirs[3] = True
            else:
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

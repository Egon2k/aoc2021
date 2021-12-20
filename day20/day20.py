def get_pixel(row, col, input, switch):
    if row < 0 or col < 0 or row >= len(input) or col >= len(input[0]):
        return switch
    else:
        return input[row][col]

def get_neighbors(row, col, input, switch):
    out = [[0,0,0] for i in range(3)]

    for r, rr in enumerate(range(row - 1,row + 2)):
        for c, cc in enumerate(range(col - 1,col + 2)):
            out[r][c] = get_pixel(rr, cc, input, switch)
    return out

def solve(algo, input, switch):
    output_rows = len(input) + 2
    output_cols = len(input[0]) + 2

    output = [[0]*(output_rows) for i in range(output_cols)]

    for row in range(output_rows):
        for col in range(output_cols):
            idx = get_neighbors(row - 1, col - 1, input, switch)
            idx_str = ""
            for x in range(len(idx)):
                for y in range(len(idx[0])):
                    idx_str += str(idx[x][y])

            output[row][col] = algo[int(idx_str,2)]

    return output

def print_picture(input):
    for row in input:
        for col in row:
            if col == '0':
                print('.', end='')
            else:
                print('#', end='')
        print('')
    print('')

def part1(algo, input):
    output = input
    print_picture(output)
    for x in range(2):
        output = solve(algo, output, x % 2)
        print_picture(output)

    ans = 0
    for row in output:
        ans += row.count('1')
    return ans


def part2(algo, input):
    pass

if __name__ == '__main__':
    algo = ""
    input = list()

    with open('day20/data.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                algo = list(line.strip().replace('.', '0').replace('#', '1'))
            elif i > 1:
                input.append(list(line.strip().replace('.', '0').replace('#', '1')))

    print(part1(algo, input))
    print(part2(algo, input))

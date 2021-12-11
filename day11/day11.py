'''
──────────▄▄▄▄▄▄▄▄▄▄▄──────────
─────▄▄▀▀▀▀──────────▀▀▄▄──────
───▄▀───────────────────▀▀▄────
──█────────────────────────█───
─█─────────────────────▄▀▀▀▀▀█▄
█▀────────────────────█────▄███
█─────────────────────█────▀███
█─────▄▀▀██▀▄─────────█───────█
█────█──████─█─────────▀▄▄▄▄▄█─
█────█──▀██▀─█───────────────█─
█────█───────█──────────────▄▀─
█────▀▄─────▄▀──▄▄▄▄▄▄▄▄▄───█──
█──────▀▀▀▀▀────█─█─█─█─█──▄▀──
─█──────────────▀▄█▄█▄█▀──▄▀───
──█──────────────────────▄▀────
───▀▀▀▄──────────▄▄▄▄▄▄▀▀──────
────▄▀─────────▀▀──▄▀──────────
──▄▀───────────────█───────────
─▄▀────────────────█──▄▀▀▀█▀▀▄─
─█────█──█▀▀▀▄─────█▀▀────█──█─
▄█────▀▀▀────█─────█────▀▀───█─
█▀▄──────────█─────█▄────────█─
█──▀▀▀▀▀█▄▄▄▄▀─────▀█▀▀▀▄▄▄▄▀──
█───────────────────▀▄───────── 
'''

def getNeighbors(r, c, rLim, cLim):
    n = []
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            if (row, col) != (r, c):
                if (0 <= row <= (rLim - 1)) and \
                   (0 <= col <= (cLim - 1)):
                    n.append((row, col))
    return n

def step(data):
    nines = list()
    changes = list()
    for row in range(len(data)):
        for col in range(len(data[0])):
            data[row][col] += 1
            if data[row][col] > 9:
                changes.append((row, col))
                if (row, col) not in nines:
                    nines.append((row, col))

    while changes:
        changesNew = list()
        for row, col in changes:
            n = getNeighbors(row, col, len(data), len(data[0]))
            for n_row, n_col in n:
                if (n_row, n_col) in nines:
                    continue

                data[n_row][n_col] +=1

                if data[n_row][n_col] > 9:
                    changesNew.append((n_row, n_col))
                    if (n_row, n_col) not in nines:
                        nines.append((n_row, n_col))
        changes = changesNew

    for row, col in nines:
        data[row][col] = 0
    return len(nines), data

def part1(data):
    origin = data[:]
    sum = 0
    for _ in range(100):
        flashes, origin = step(origin)
        sum += flashes
    return sum

def part2(data):
    origin = data[:]
    i = 1
    while True:
        flashes, origin = step(origin)
        if flashes == 100:
            return i
        i += 1

if __name__ == '__main__':
    data = []

    with open('day11/data.txt') as f:
        for line in f:
            data.append([int(x) for x in line.strip()])

    print(part1(data))
    print(part2(data))
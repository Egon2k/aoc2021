def transposeSet(set):
    '''
    returns the transpose of a given set
    '''
    return list(map(list, zip(*set)))

def checkLine(set):
    '''
    checks if one line a set contains only maked numbers = winning condition
    '''
    for line in set:
        for nmbr in line:
            # check complete line
            if nmbr != -1:
                return False
        return True

def calcSumOfNonMarked(set):
    '''
    returns the sum of all unmarkted numbers in a given set
    '''
    count = 0
    for line in set:
        for nmbr in line:
            if nmbr != -1:
                count += nmbr
    return count

def checkWinning(sets):
    '''
    checks if one of the given sets is a winner and returns its index
    returns -1 in case of no winner
    '''
    for i, set in enumerate(sets):
        if checkLine(set) or checkLine(transposeSet(set)):
            return i
    return -1

def part1(draws, sets):
    for draw in draws:
        for set in sets:
            for line in set:
                if draw in line:
                    # if draw in line, replace with -1
                    line[line.index(draw)] = -1
                    break

        # after each draw, check winning condition
        winningSet = checkWinning(sets)

        if winningSet != -1:
            return draw * calcSumOfNonMarked(sets[winningSet])

def part2(draws, sets):
    pass
            
if __name__ == "__main__":
    data = []

    with open('day04/data.txt') as f:
        for line in f:
            data.append(line.strip())
        data.append("") # append empty line to make data processing detect last set

    # prepare data for processing
    draws = [int(i) for i in data[0].split(',')]
    sets = list()
    set = list()

    for i, line in enumerate(data[2:]):
        if line == "":
            sets.append(set)
            set = []
        else:
            set.append([int(i) for i in line.split()])

    print(part1(draws, sets))
    print(part2(draws, sets))
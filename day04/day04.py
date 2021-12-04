def transposeSet(set):
    '''
    returns the transpose of a given set
    '''
    return list(map(list, zip(*set)))

def checkLinesInSet(set):
    '''
    checks if one line a set contains only maked numbers = winning condition
    '''
    win = False
    for line in set:
        #check if all elements are -1
        if line.count(-1) == len(line):
            return True
    return False


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

def checkWinningSet(set):
    return checkLinesInSet(set) or checkLinesInSet(transposeSet(set))

def checkWinningFirst(sets):
    '''
    checks if one of the given sets is a winner and returns its index
    returns -1 in case of no winner
    '''
    for i, set in enumerate(sets):
        if checkWinningSet(set):
            return i
    return -1

def checkWinningLast(sets):
    '''
    checks if all of the given sets are a winner and returns its index
    returns -1 in case of no winner
    '''
    count = 0
    idx = 0
    for i, set in enumerate(sets):
        if checkWinningSet(set) != -1:
            count += 1
            break
            
    if count == len(sets):
        return idx
    else:
        return -1

def part1(draws, sets):
    localSets = sets[:]
    for draw in draws:
        for set in localSets:
            for line in set:
                if draw in line:
                    # if draw in line, replace with -1
                    line[line.index(draw)] = -1
                    break

        # after each draw, check winning condition
        winningSet = checkWinningFirst(localSets)

        if winningSet != -1:
            return draw * calcSumOfNonMarked(localSets[winningSet])

def part2(draws, sets):
    localSets = sets[:]
    for draw in draws:
        for set in localSets:
            for line in set:
                if draw in line:
                    # if draw in line, replace with -1
                    line[line.index(draw)] = -1
                    break

        # after each draw, check winning condition
        if draw == 13:
            draw = draw

        winningSet = checkWinningLast(localSets)

        if winningSet != -1:
            return draw * calcSumOfNonMarked(localSets[winningSet])
            
def prepareData(data):
    draws = [int(i) for i in data[0].split(',')]
    sets = list()
    set = list()

    for i, line in enumerate(data[2:]):
        if line == "":
            sets.append(set)
            set = []
        else:
            set.append([int(i) for i in line.split()])
    return draws,sets

if __name__ == "__main__":
    data = []

    with open('day04/testdata.txt') as f:
        for line in f:
            data.append(line.strip())
        data.append("") # append empty line to make data processing detect last set

    # prepare data for processing
    draws, sets = prepareData(data)
    print(part1(draws, sets))

    draws, sets = prepareData(data)
    print(part2(draws, sets))
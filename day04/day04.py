'''''''''''''''''''''
Ey, nicht spicken :P 
'''''''''''''''''''''

def transposeSet(set):
    '''
    returns the transpose of a given set
    '''
    return list(map(list, zip(*set)))

def checkLinesInSet(set):
    '''
    checks if one line a set contains only marked numbers = winning condition
    '''
    win = False
    for line in set:
        #check if all elements are -1
        if line.count(-1) == len(line):
            return True
    return False

def calcSumOfNonMarked(set):
    '''
    returns the sum of all unmarked numbers in a given set
    '''
    count = 0
    for line in set:
        for nmbr in line:
            if nmbr != -1:
                count += nmbr
    return count

def checkWinningSet(set):
    '''
    returns True in case of winning condition (colume or row with only -1) 
    '''
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

def checkWinningSecondLast(sets):
    '''
    checks if all but one set are winners and return the index of the last 
    not-winner - else returns -1
    '''
    count = 0
    idx = 0
    for i, set in enumerate(sets):
        if checkWinningSet(set):
            count += 1
        else:
            idx = i
            
    if count == len(sets)-1:
        return idx
    else:
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
        winningSet = checkWinningFirst(sets)

        if winningSet != -1:
            return draw * calcSumOfNonMarked(sets[winningSet])

def part2(draws, sets):
    for i, draw in enumerate(draws[:-1]):
        for set in sets:
            for line in set:
                if draw in line:
                    # if draw in line, replace with -1
                    line[line.index(draw)] = -1
                    break
        
        # after each draw, check winning condition
        winningSet = checkWinningSecondLast(sets)

        if winningSet != -1:
            return draws[i+1] * (calcSumOfNonMarked(sets[winningSet]) - draws[i+1])
            
def prepareData(data):
    draws = [int(i) for i in data[0].split(',')]
    sets = list()
    set = list()

    for i, line in enumerate(data[2:]):
        if line == "":
            # append set to sets and clear set for next
            sets.append(set)
            set = []
        else:
            # convert strings to int and append to set
            set.append([int(i) for i in line.split()])
    return draws,sets

if __name__ == "__main__":
    data = []

    with open('day04/data.txt') as f:
        for line in f:
            data.append(line.strip())
        data.append("") # append empty line to make data processing detect last set

    # prepare data for processing
    draws, sets = prepareData(data)
    print(part1(draws, sets))

    draws, sets = prepareData(data)
    print(part2(draws, sets))
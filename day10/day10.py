'''''''''''''''''''''''''''''''''''
Zicke zacke zicke zacke hoi hoi hoi
'''''''''''''''''''''''''''''''''''
def processLine(line):
    '''
    first return value contains the first wrong closing bracket
    returns None in case of incomplete line
    second return value contains a list of all uncompleted
    opening brackets, retuns None in case of corrupted line
    '''
    matchingBrackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

    brackets = list()
    for currBracket in line:
        if currBracket in '([{<':
            brackets.append(currBracket)
        else:
            lastBracket = ""
            if brackets:
                lastBracket = brackets.pop()
            if currBracket != matchingBrackets[lastBracket]:
                return currBracket, None
    return None, brackets

def part1(data):
    sum = 0
    for line in data:
        corruptedBracket, _ = processLine(line)
        if corruptedBracket == ')':
            sum += 3
        elif corruptedBracket == ']':
            sum += 57
        elif corruptedBracket == '}':
            sum += 1197
        elif corruptedBracket == '>':
            sum += 25137
    return sum

def part2(data):
    sums = list()
    for line in data:
        sum = 0
        _, incomplete = processLine(line)

        while(incomplete):
            lastBracket = incomplete.pop()
            if lastBracket == '(':
                sum = sum * 5 + 1
            elif lastBracket == '[':
                sum = sum * 5 + 2
            elif lastBracket == '{':
                sum = sum * 5 + 3
            elif lastBracket == '<':
                sum = sum * 5 + 4

        # sum = 0 means line was not incomplete
        if sum:
            sums.append(sum)

    sums.sort()
    return sums[(len(sums) - 1) // 2]

if __name__ == "__main__":
    data = []

    with open('day10/data.txt') as f:
        for line in f:
            data.append([x for x in line.strip()])

    print(part1(data))
    print(part2(data))
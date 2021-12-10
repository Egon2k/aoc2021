'''''''''''''''''''''''''''''''''''
Zicke zacke zicke zacke hoi hoi hoi
'''''''''''''''''''''''''''''''''''
def processLine(line):
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
                return currBracket
    return

def part1(data):
    sum = 0
    for line in data:
        corruptedBracket = processLine(line)
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
    pass

if __name__ == "__main__":
    data = []

    with open('day10/data.txt') as f:
        for line in f:
            data.append([x for x in line.strip()])

    print(part1(data))
    print(part2(data))
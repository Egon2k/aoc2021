'''''''''''''''''''''''''''
Spicken ist für Loser :P 
'''''''''''''''''''''''''''
def part1(data):
    count = 0
    for line in data:
        for digit in line[line.index('|'):]:
            if len(digit) in [2,3,4,7]:
                count += 1
    return count

def part2(data):
    sum = 0
    sortedData = sortData(data)

    for line in sortedData:
        digitZero = ""  # 6 seg
        digitOne = ""   # 2 seq (unique)
        digitTwo = ""   # 5 seg
        digitThree = "" # 5 seg
        digitFour = ""  # 4 seg (unique)
        digitFive = ""  # 5 seg
        digitSix = ""   # 6 seg
        digitSeven = "" # 3 seg (unique)
        digitEight = "" # 7 seg (unique)
        digitNine = ""  # 6 seg

        # identify uniques
        for digit in line[:line.index('|')]:
            if len(digit) == 2:
                digitOne = digit
            if len(digit) == 3: 
                digitSeven = digit
            if len(digit) == 4: 
                digitFour = digit
            if len(digit) == 7: 
                digitEight = digit

        # all 7 segments       digitFour without digitOne equals segBD
        #   
        #   aaaa               
        #  b    c              b    c               c          b 
        #  b    c              b    c               c          b
        #   dddd                dddd       -             =      dddd
        #  e    f                   f               f
        #  e    f                   f               f
        #   gggg    
                 
        segBD = digitFour.replace(digitOne[0], '').replace(digitOne[1], '')
        segCF = digitOne
        
        # identify others
        for digit in line[:line.index('|')]:
            if len(digit) == 6: # digitZero or digitSix or digitNine
                if all(x in digit for x in segBD):
                    # digitSix or digitNine
                    if all(x in digit for x in segCF):
                        digitNine = digit
                    else:
                        digitSix = digit
                else:
                    digitZero = digit
            if len(digit) == 5: # digitTwo or digitThree or digitFive
                if all(x in digit for x in segBD):
                    digitFive = digit
                else:
                    if all(x in digit for x in segCF):
                        digitThree = digit
                    else:
                        digitTwo = digit
        
        number = 0
        for digit in line[line.index('|'):]:
            number *= 10
            if digitZero == digit:
                number += 0
            elif digitOne == digit:
                number += 1
            elif digitTwo == digit:
                number += 2
            elif digitThree == digit:
                number += 3
            elif digitFour == digit:
                number += 4
            elif digitFive == digit:
                number += 5
            elif digitSix == digit:
                number += 6
            elif digitSeven == digit:
                number += 7
            elif digitEight == digit:
                number += 8
            elif digitNine == digit:
                number += 9
        
        sum += number
            
    return sum

def sortString(str):
    sortedChars = sorted(str)
    return "".join(sortedChars)

def sortData(data):
    sortedData = list()
    for line in data:
        sortedLine = list()
        for digit in line:
            sortedLine.append(sortString(digit))
        sortedData.append(sortedLine)
    return sortedData
    
if __name__ == "__main__":
    data = []

    with open('day08/data.txt') as f:
        for line in f:
            data.append(line.strip().split())

    print(part1(data))
    print(part2(data))

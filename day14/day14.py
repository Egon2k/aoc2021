'''
Bazinga!
'''
from collections import Counter

def solve(pol, rules, loops):
    tuples = Counter()
    
    # count every char tuple in polynom
    for char in range(len(pol)-1):
        tuples[pol[char] + pol[char + 1]] += 1
    
    for _ in range(loops):
        # each loop only follows the rules once so create new counter
        new_tuples = Counter()
        for tuple in tuples:
            # rule "AB -> C" results in AC and CB
            new_tuples[tuple[0] + rules[tuple]] += tuples[tuple]
            new_tuples[rules[tuple] + tuple[1]] += tuples[tuple]
        tuples = new_tuples

    # count single chars since we only have tuples of chars
    single_chars = Counter()

    for tuple in tuples:
        single_chars[tuple[0]] += tuples[tuple]
    # last char in polynom is not counted, since we only considered tuples
    # so add 1 for the last char in polynom
    single_chars[pol[-1]] += 1

    return max(single_chars.values()) - min(single_chars.values())

def part1(pol, rules):
    return solve(pol, rules, 10)
    
def part2(pol, rules):
    return solve(pol, rules, 40)

if __name__ == '__main__':
    pol = ""
    rules = dict()

    with open('day14/data.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                pol = line.strip()
            elif i > 1:
                x = line.strip().split(' -> ')
                rules[x[0]] = x[1] 

    print(part1(pol, rules))
    print(part2(pol, rules))
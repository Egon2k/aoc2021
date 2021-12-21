def roll_dice(last):
    return (last + 3) % 100, [s % 100 + 1 for s in [last, last+1, last+2]]

def part1(init):
    space = init
    score = [0,0]
    last_roll = 0
    rolls = 0
    p2 = False # start with player 1
    while (max(score) < 1000):
        last_roll, eyes = roll_dice(last_roll)
        space[p2] += sum(eyes)
        space[p2] = (space[p2] - 1) % 10 + 1
        score[p2] += space[p2]
        rolls += 3
        p2 = not p2

    return score[p2] * rolls

def part2(init):
    pass

if __name__ == '__main__':
    #init = [4,8] # testdata
    init = [3,7]

    print(part1(init))
    print(part2(init))

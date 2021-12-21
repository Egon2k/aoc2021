def roll_dice(last):
    return (last + 3) % 100, [s % 100 + 1 for s in [last, last+1, last+2]]

def part1(init):
    space = init[:]
    score = [0,0]
    last_roll = 0
    rolls = 0
    active_player = 0 # start with player 1
    while (max(score) < 1000):
        last_roll, eyes = roll_dice(last_roll)
        space[active_player] += sum(eyes)
        space[active_player] = (space[active_player] - 1) % 10 + 1
        score[active_player] += space[active_player]
        rolls += 3
        active_player ^= 1

    return score[active_player] * rolls

def part2(init):
    states = {}
    
    def calc_wins(space_p1, space_p2, score_p1, score_p2):
        state = (space_p1, space_p2, score_p1, score_p2)
        
        if score_p1 >= 21:
            return (1, 0)

        if score_p2 >= 21:
            return (0, 1)

        if state in states:
            return states[state] # already simulated
        
        wins = (0,0)

        for dice1 in [1,2,3]:
            for dice2 in [1,2,3]:
                for dice3 in [1,2,3]:
                    new_score_p1 = (space_p1 + dice1 + dice2 + dice3 - 1) % 10 + 1
                    new_space_p1 = score_p1 + new_score_p1

                    wins_p1, wins_p2 = calc_wins(space_p2, new_score_p1, score_p2, new_space_p1)
                    wins = (wins[0] + wins_p2, wins[1] + wins_p1)

        states[(space_p1, space_p2, score_p1, score_p2)] = wins
        return wins

    return max(calc_wins(init[0], init[1], 0, 0))

if __name__ == '__main__':
    #init = [4,8] # testdata
    init = [3,7]

    print(part1(init))
    print(part2(init))
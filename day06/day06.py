'''''''''''''''''''''
Ey, nicht spicken :P 
'''''''''''''''''''''
def solve(data, days):
    fishes = data[:]
    
    # create table with amount of fish of all possible days 
    # left until reproduction (0-8)
    daysLeft = list()
    for _ in range(9):
        daysLeft.append(0)

    # count the number of fishes each day until reproduction
    for fish in fishes:
        daysLeft[fish] += 1

    amount = len(fishes)

    for _ in range(days):
        new = daysLeft[0] 
        amount += new # add amount of fish that reproduced

        for n in range(8):
            daysLeft[n] = daysLeft[n + 1]

        daysLeft[6] += new # reset all fish that replicated back to 6
        daysLeft[8] = new # add new amount of fish with 8 days left

    return amount

def part1(data):
    return solve(data, 80)

def part2(data):
    return solve(data, 256)

if __name__ == "__main__":
    with open('day06/data.txt') as f:
        for line in f:
            data = [int(i) for i in line.strip().split(',')]

    print(part1(data))
    print(part2(data))
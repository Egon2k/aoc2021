'''
Gewalt ist auch eine Lösung!
'''
def shoot(x_start, y_start):
    pos = list((0, 0))
    y_max = 0
    x = x_start
    y = y_start
    while (not(x > 161 or y < -154)):
        pos[0] += x
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        pos[1] += y
        y -= 1

        if pos[1] > y_max:
            y_max = pos[1]

        if 111 <= pos[0] <= 161 and -154 <= pos[1] <= -101:
            return y_max, True
    
    return 0, False
        
def part12():
    y_hits = list()
    
    for x in range(165):
        for y in range(-155, 1000):
            y_max, hit = shoot(x, y)
            if hit:
                y_hits.append(y_max)
                print(max(y_hits), len(y_hits))
        
    return max(y_hits), len(y_hits)

if __name__ == '__main__':
    data = []

    with open('day17/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(f'final = {part12()}')

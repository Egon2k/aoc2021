'''
Gewalt ist auch eine Lösung!
'''
def shoot(x_start, y_start, x_target, y_target):
    pos = list((0, 0))
    y_max = 0
    x = x_start
    y = y_start
    while (not(x > max(x_target) or y < min(y_target))):
        pos[0] += x
        if x > 0:
            x -= 1
        elif x == 0:
            pass
        else:
            x += 1
        pos[1] += y
        y -= 1

        if pos[1] > y_max:
            y_max = pos[1]

        if pos[0] in x_target and pos[1] in y_target:
            return y_max, True
    
    return 0, False
        
def part12(x_target, y_target):
    y_hits = list()
    
    for x in range(161):
        for y in range(-154,1000):
            y_max, hit = shoot(x, y, x_target, y_target)
            if hit:
                y_hits.append(y_max)
                print(max(y_hits), len(y_hits))
        
    return max(y_hits), len(y_hits)

if __name__ == '__main__':
    data = []

    with open('day17/data.txt') as f:
        for line in f:
            data.append(line.strip())

    x_target = range( 111, 161)
    y_target = range(-154,-101)    

    print(f'final = {part12(x_target, y_target)}')
